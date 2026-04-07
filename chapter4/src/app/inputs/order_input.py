from app.exceptions import OrderItemValidationError
from app.models.order import OrderItem


def parse_order_items_from_event(data: object) -> list[OrderItem]:
    if not isinstance(data, list):
        raise OrderItemValidationError("items はリストである必要があります")
    return [parse_order_item(item) for item in data]


def parse_order_item(data: dict[str, object]) -> OrderItem:
    item = _parse(data)
    validate_order_item(item)
    return item


def _parse(data: dict[str, object]) -> OrderItem:
    try:
        return OrderItem(**data)
    except TypeError as e:
        raise OrderItemValidationError(f"不正なアイテムデータ: {e}") from e


def validate_order_item(item: OrderItem) -> None:
    if item.price <= 0 or item.quantity <= 0:
        raise OrderItemValidationError("price と quantity は1以上である必要があります")
