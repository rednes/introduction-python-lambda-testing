from app.models.order import OrderItem


def calculate_total(items: list[OrderItem]) -> int:
    """10,000円以上は10%割引"""
    subtotal = sum(item.price * item.quantity for item in items)
    if subtotal >= 10000:
        return int(subtotal * 0.9)
    return subtotal
