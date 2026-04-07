import os
from functools import cache

from app.gateways.payment_gateway import PaymentGateway

_PAYMENT_API_URL = os.environ["PAYMENT_API_URL"]
_PAYMENT_API_TIMEOUT = int(os.environ.get("PAYMENT_API_TIMEOUT", "5"))


@cache
def get_payment_gateway() -> PaymentGateway:
    return PaymentGateway(_PAYMENT_API_URL, timeout=_PAYMENT_API_TIMEOUT)
