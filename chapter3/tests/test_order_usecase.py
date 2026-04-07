from unittest.mock import MagicMock

from app.models.order import OrderItem
from app.usecases.order_usecase import create_order


def test_create_order():
    mock_repo = MagicMock()
    order = create_order([OrderItem(price=5000, quantity=3)], "order-001", mock_repo)
    assert order.total == 13500
    assert order.order_id == "order-001"
    mock_repo.save.assert_called_once_with(order)
