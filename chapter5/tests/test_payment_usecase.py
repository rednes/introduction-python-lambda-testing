from unittest.mock import MagicMock

from app.usecases.payment_usecase import process_payment


def test_process_payment_success():
    """正常系: gateway の結果をそのまま返す"""
    gw = MagicMock()
    gw.process.return_value = {"transaction_id": "txn-001", "status": "completed"}
    result = process_payment("order-001", 9000, gw)
    assert result["transaction_id"] == "txn-001"
    gw.process.assert_called_once_with("order-001", 9000)
