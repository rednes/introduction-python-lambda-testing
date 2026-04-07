from app.dependencies import get_order_repository
from app.models.order import OrderItem
from app.usecases.order_usecase import create_order


def handler(event, context):
    order_id = event["order_id"]
    items = [OrderItem(**item) for item in event.get("items", [])]
    order = create_order(items, order_id, get_order_repository())
    return {"statusCode": 200, "body": {"data": {"total": order.total}}}
