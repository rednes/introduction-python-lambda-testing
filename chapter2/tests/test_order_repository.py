from unittest.mock import MagicMock

from app.models.order import Order, OrderItem
from app.repositories.order_repository import OrderRepository


def test_save():
    mock_dynamodb = MagicMock()
    mock_table = MagicMock()
    mock_dynamodb.Table.return_value = mock_table

    items = [OrderItem(price=3000, quantity=3)]
    order = Order(order_id="order-001", items=items, total=9000)
    repo = OrderRepository(mock_dynamodb, "orders")
    repo.save(order)

    mock_dynamodb.Table.assert_called_once_with("orders")
    mock_table.put_item.assert_called_once_with(Item={
        "order_id": "order-001",
        "items": [{"price": 3000, "quantity": 3}],
        "total": 9000,
    })
