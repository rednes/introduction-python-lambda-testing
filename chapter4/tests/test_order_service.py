from app.models.order import OrderItem
from app.services.order_service import calculate_total


def test_calculate_total_no_discount():
    items = [OrderItem(price=3000, quantity=2)]
    assert calculate_total(items) == 6000


def test_calculate_total_with_discount():
    items = [OrderItem(price=5000, quantity=2)]
    assert calculate_total(items) == 9000


def test_calculate_total_truncates():
    """割引後の端数は切り捨て"""
    items = [OrderItem(price=10001, quantity=1)]
    assert calculate_total(items) == 9000  # 10001 * 0.9 = 9000.9 → 9000
