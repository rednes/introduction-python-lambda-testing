from app.models.order import Order


class OrderRepository:
    def __init__(self, dynamodb, table_name: str):
        self._table = dynamodb.Table(table_name)

    def save(self, order: Order) -> None:
        self._table.put_item(Item={
            "order_id": order.order_id,
            "items": [{"price": item.price, "quantity": item.quantity} for item in order.items],
            "total": order.total,
        })
