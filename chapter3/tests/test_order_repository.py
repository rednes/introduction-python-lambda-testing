from app.models.order import Order, OrderItem
from app.repositories.order_repository import OrderRepository


def test_save(dynamodb_table):
    repo = OrderRepository(dynamodb_table, "orders")
    order = Order(order_id="order-001", items=[OrderItem(price=3000, quantity=3)], total=9000)
    repo.save(order)
    table = dynamodb_table.Table("orders")
    response = table.get_item(Key={"order_id": "order-001"})
    assert response["Item"]["items"] == [{"price": 3000, "quantity": 3}]
    assert response["Item"]["total"] == 9000
