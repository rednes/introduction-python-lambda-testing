from app.dependencies import get_order_repository
from app.exceptions import OrderItemValidationError, OrderSaveError
from app.inputs.order_input import parse_order_items_from_event
from app.usecases.order_usecase import create_order


def _ok(data: dict[str, object]) -> dict[str, object]:
    return {"statusCode": 200, "body": {"data": data}}


def _err(status_code: int, message: str) -> dict[str, object]:
    return {"statusCode": status_code, "body": {"error": message}}


def handler(event: dict[str, object], context: object) -> dict[str, object]:
    repo = get_order_repository()

    try:
        items = parse_order_items_from_event(event.get("items", []))
        order = create_order(items, event["order_id"], repo)
        return _ok({"total": order.total})

    except OrderSaveError as e:
        return _err(500, str(e))
    except OrderItemValidationError as e:
        return _err(400, str(e))
    except KeyError as e:
        return _err(400, f"必須パラメータが不足: {e}")
