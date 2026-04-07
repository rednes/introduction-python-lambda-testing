import os

import pytest

PAYMENT_API_URL = "https://api.example.com/payments"

os.environ["PAYMENT_API_URL"] = PAYMENT_API_URL
os.environ["PAYMENT_API_TIMEOUT"] = "5"


@pytest.fixture(autouse=True)
def _clear_dependency_cache():
    from app.dependencies import get_payment_gateway
    get_payment_gateway.cache_clear()
    yield
    get_payment_gateway.cache_clear()
