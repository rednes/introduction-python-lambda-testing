from app.models.order import Order, OrderItem
from app.repositories.order_repository import OrderRepository
from app.services.order_service import calculate_total


def create_order(items: list[OrderItem], order_id: str, repository: OrderRepository) -> Order:
    total = calculate_total(items)
    order = Order(order_id=order_id, items=items, total=total)
    repository.save(order)
    return order
