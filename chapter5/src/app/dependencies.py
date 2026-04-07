import os

from app.gateways.payment_gateway import PaymentGateway

_payment_api_url = os.environ["PAYMENT_API_URL"]
_payment_api_timeout = os.environ.get("PAYMENT_API_TIMEOUT", "5")

def get_payment_gateway() -> PaymentGateway:
    return PaymentGateway(
        _payment_api_url,
        timeout=int(_payment_api_timeout),
    )
