from typing import Any

from app.gateways.payment_gateway import PaymentGateway


def process_payment(order_id: str, amount: int, gateway: PaymentGateway) -> dict[str, Any]:
    return gateway.process(order_id, amount)
