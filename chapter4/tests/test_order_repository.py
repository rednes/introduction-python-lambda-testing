import pytest
from unittest.mock import MagicMock
from botocore.exceptions import ClientError

from app.exceptions import OrderSaveError
from app.models.order import Order, OrderItem
from app.repositories.order_repository import OrderRepository


def test_save(dynamodb_table):
    repo = OrderRepository(dynamodb_table, "orders")
    order = Order(order_id="order-001", items=[OrderItem(price=3000, quantity=3)], total=9000)
    repo.save(order)
    table = dynamodb_table.Table("orders")
    response = table.get_item(Key={"order_id": "order-001"})
    assert response["Item"]["total"] == 9000
    assert response["Item"]["items"] == [{"price": 3000, "quantity": 3}]


def test_save_raises_order_save_error_on_dynamodb_failure():
    mock_dynamodb = MagicMock()
    mock_table = MagicMock()
    mock_dynamodb.Table.return_value = mock_table
    mock_table.put_item.side_effect = ClientError(
        {"Error": {"Code": "ProvisionedThroughputExceededException", "Message": "スループット超過"}},
        "PutItem",
    )
    repo = OrderRepository(mock_dynamodb, "orders")
    order = Order(order_id="order-001", items=[OrderItem(price=3000, quantity=3)], total=9000)
    with pytest.raises(OrderSaveError, match="注文の保存に失敗しました"):
        repo.save(order)
