from unittest.mock import MagicMock, patch

from app.exceptions import PaymentAPIError, PaymentTimeoutError
from controller import handler

_GET_GATEWAY = "controller.get_payment_gateway"


def _mock_gateway(side_effect=None, return_value=None):
    gw = MagicMock()
    if side_effect is not None:
        gw.process.side_effect = side_effect
    else:
        gw.process.return_value = return_value
    return gw


def test_handler_success():
    gw = _mock_gateway(return_value={"transaction_id": "txn-001", "status": "completed"})
    with patch(_GET_GATEWAY, return_value=gw):
        result = handler({"order_id": "order-001", "amount": 9000}, {})
    assert result["statusCode"] == 200
    assert result["body"]["data"]["transaction_id"] == "txn-001"


def test_handler_api_500():
    gw = _mock_gateway(side_effect=PaymentAPIError(500))
    with patch(_GET_GATEWAY, return_value=gw):
        result = handler({"order_id": "order-001", "amount": 9000}, {})
    assert result["statusCode"] == 500
    assert "決済APIエラー" in result["body"]["error"]


def test_handler_timeout():
    gw = _mock_gateway(side_effect=PaymentTimeoutError())
    with patch(_GET_GATEWAY, return_value=gw):
        result = handler({"order_id": "order-001", "amount": 9000}, {})
    assert result["statusCode"] == 504
    assert "タイムアウト" in result["body"]["error"]


def test_handler_missing_order_id():
    result = handler({"amount": 9000}, {})
    assert result["statusCode"] == 400
    assert "必須パラメータが不足" in result["body"]["error"]


def test_handler_missing_amount():
    result = handler({"order_id": "order-001"}, {})
    assert result["statusCode"] == 400
    assert "必須パラメータが不足" in result["body"]["error"]


def test_handler_empty_event():
    result = handler({}, {})
    assert result["statusCode"] == 400
    assert "必須パラメータが不足" in result["body"]["error"]
