from app.models.order import OrderItem
from app.services.order_service import calculate_total


def test_calculate_total_no_discount():
    items = [OrderItem(price=3000, quantity=2)]
    assert calculate_total(items) == 6000


def test_calculate_total_exact_threshold():
    items = [OrderItem(price=10000, quantity=1)]
    assert calculate_total(items) == 9000


def test_calculate_total_with_discount():
    items = [OrderItem(price=6000, quantity=2)]
    assert calculate_total(items) == 10800


def test_calculate_total_truncation():
    """割引後の端数は切り捨てられる"""
    items = [OrderItem(price=10001, quantity=1)]
    assert calculate_total(items) == 9000
