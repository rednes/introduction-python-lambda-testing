from unittest.mock import MagicMock, patch

from controller import handler


def test_handler():
    mock_repo = MagicMock()
    with patch("controller.get_order_repository", return_value=mock_repo):
        event = {"order_id": "order-001", "items": [{"price": 5000, "quantity": 3}]}
        result = handler(event, {})
    assert result["statusCode"] == 200
    assert result["body"]["data"]["total"] == 13500
