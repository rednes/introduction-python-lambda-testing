import pytest
from unittest.mock import MagicMock

from app.exceptions import OrderSaveError
from app.models.order import OrderItem
from app.usecases.order_usecase import create_order


def test_create_order():
    from app.models.order import Order
    mock_repo = MagicMock()
    order = create_order([OrderItem(price=5000, quantity=3)], "order-001", mock_repo)
    assert order.total == 13500
    mock_repo.save.assert_called_once_with(order)


def test_create_order_propagates_save_error():
    mock_repo = MagicMock()
    mock_repo.save.side_effect = OrderSaveError("保存失敗")
    with pytest.raises(OrderSaveError):
        create_order([OrderItem(price=1000, quantity=1)], "order-001", mock_repo)
