from unittest.mock import MagicMock, patch

from app.exceptions import OrderSaveError
from controller import handler


def test_create_order():
    mock_repo = MagicMock()
    with patch("controller.get_order_repository", return_value=mock_repo):
        event = {"order_id": "order-001", "items": [{"price": 5000, "quantity": 3}]}
        result = handler(event, {})
    assert result["statusCode"] == 200
    assert result["body"]["data"]["total"] == 13500


def test_dynamodb_save_error_returns_500():
    mock_repo = MagicMock()
    mock_repo.save.side_effect = OrderSaveError("保存失敗")
    with patch("controller.get_order_repository", return_value=mock_repo):
        event = {"order_id": "order-001", "items": [{"price": 1000, "quantity": 1}]}
        result = handler(event, {})
    assert result["statusCode"] == 500
    assert "保存失敗" in result["body"]["error"]


def test_invalid_item_returns_400():
    mock_repo = MagicMock()
    with patch("controller.get_order_repository", return_value=mock_repo):
        result = handler({"order_id": "order-001", "items": [{"price": 1000}]}, {})
    assert result["statusCode"] == 400
    assert "不正なアイテムデータ" in result["body"]["error"]


def test_missing_order_id_returns_400():
    mock_repo = MagicMock()
    with patch("controller.get_order_repository", return_value=mock_repo):
        result = handler({"items": [{"price": 1000, "quantity": 1}]}, {})
    assert result["statusCode"] == 400
    assert "必須パラメータが不足" in result["body"]["error"]
