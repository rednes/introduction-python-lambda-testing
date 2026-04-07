import json

import responses
import requests
import pytest

from conftest import PAYMENT_API_URL
from app.exceptions import PaymentAPIError, PaymentTimeoutError
from app.gateways.payment_gateway import PaymentGateway


@responses.activate
def test_process_success():
    """正常系: 決済APIが成功レスポンスを返す"""
    responses.post(
        PAYMENT_API_URL,
        json={"transaction_id": "txn-001", "status": "completed"},
        status=200,
    )
    gw = PaymentGateway(PAYMENT_API_URL)
    result = gw.process("order-001", 9000)
    assert result["transaction_id"] == "txn-001"
    assert result["status"] == "completed"
    body = json.loads(responses.calls[0].request.body)
    assert body["order_id"] == "order-001"
    assert body["amount"] == 9000


@responses.activate
def test_process_api_error():
    """異常系: 決済APIが500エラーを返す → PaymentAPIError に変換する"""
    responses.post(PAYMENT_API_URL, json={"error": "internal"}, status=500)
    gw = PaymentGateway(PAYMENT_API_URL)
    with pytest.raises(PaymentAPIError) as exc_info:
        gw.process("order-001", 9000)
    assert exc_info.value.status_code == 500


@responses.activate
def test_process_timeout():
    """異常系: 決済APIがタイムアウトする → PaymentTimeoutError に変換する"""
    responses.post(PAYMENT_API_URL, body=requests.exceptions.Timeout("timed out"))
    gw = PaymentGateway(PAYMENT_API_URL)
    with pytest.raises(PaymentTimeoutError):
        gw.process("order-001", 9000)


def test_custom_timeout():
    """タイムアウト値をコンストラクタで指定できる"""
    gw = PaymentGateway(PAYMENT_API_URL, timeout=10)
    assert gw._timeout == 10


@responses.activate
def test_retry_on_timeout_then_success():
    """タイムアウト後にリトライして成功する"""
    responses.add(responses.POST, PAYMENT_API_URL, body=requests.Timeout("timed out"))
    responses.add(
        responses.POST,
        PAYMENT_API_URL,
        json={"transaction_id": "txn-001", "status": "completed"},
        status=200,
    )
    gw = PaymentGateway(PAYMENT_API_URL, max_retries=3)
    result = gw.process("order-001", 9000)
    assert result["transaction_id"] == "txn-001"
    assert len(responses.calls) == 2


@responses.activate
def test_retry_on_5xx_then_success():
    """5xxエラー後にリトライして成功する"""
    responses.add(responses.POST, PAYMENT_API_URL, json={"error": "internal"}, status=500)
    responses.add(
        responses.POST,
        PAYMENT_API_URL,
        json={"transaction_id": "txn-001", "status": "completed"},
        status=200,
    )
    gw = PaymentGateway(PAYMENT_API_URL, max_retries=3)
    result = gw.process("order-001", 9000)
    assert result["transaction_id"] == "txn-001"
    assert len(responses.calls) == 2


@responses.activate
def test_no_retry_on_4xx():
    """4xxエラーはリトライしない → PaymentAPIError に変換する"""
    responses.post(PAYMENT_API_URL, json={"error": "bad request"}, status=400)
    gw = PaymentGateway(PAYMENT_API_URL, max_retries=3)
    with pytest.raises(PaymentAPIError) as exc_info:
        gw.process("order-001", 9000)
    assert exc_info.value.status_code == 400
    assert len(responses.calls) == 1


@responses.activate
def test_retry_exhausted():
    """リトライ上限を超えたら PaymentTimeoutError を送出する"""
    responses.post(PAYMENT_API_URL, body=requests.Timeout("timed out"))
    gw = PaymentGateway(PAYMENT_API_URL, max_retries=3)
    with pytest.raises(PaymentTimeoutError):
        gw.process("order-001", 9000)
    assert len(responses.calls) == 3
