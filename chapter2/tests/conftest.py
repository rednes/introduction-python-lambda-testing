import os

import pytest

os.environ["AWS_ACCESS_KEY_ID"] = "testing"
os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
os.environ["AWS_SECURITY_TOKEN"] = "testing"
os.environ["AWS_SESSION_TOKEN"] = "testing"
os.environ["AWS_DEFAULT_REGION"] = "ap-northeast-1"
os.environ["TABLE_NAME"] = "orders"


@pytest.fixture(autouse=True)
def _clear_dependency_cache():
    from app.dependencies import get_order_repository
    get_order_repository.cache_clear()
    yield
    get_order_repository.cache_clear()
