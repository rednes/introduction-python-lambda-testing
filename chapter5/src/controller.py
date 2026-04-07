from typing import Any

from app.dependencies import get_payment_gateway
from app.exceptions import PaymentAPIError, PaymentTimeoutError
from app.usecases.payment_usecase import process_payment


def handler(event: dict[str, Any], context: object) -> dict[str, Any]:
    try:
        order_id = event["order_id"]
        amount = event["amount"]
        result = process_payment(order_id, amount, get_payment_gateway())
        return {"statusCode": 200, "body": {"data": result}}
    except PaymentTimeoutError:
        return {"statusCode": 504, "body": {"error": "決済APIがタイムアウトしました"}}
    except PaymentAPIError as e:
        return {"statusCode": e.status_code, "body": {"error": "決済APIエラー"}}
    except KeyError as e:
        return {"statusCode": 400, "body": {"error": f"必須パラメータが不足: {e}"}}
