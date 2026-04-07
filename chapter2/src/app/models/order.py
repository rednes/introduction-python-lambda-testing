from dataclasses import dataclass


@dataclass
class OrderItem:
    price: int
    quantity: int


@dataclass
class Order:
    order_id: str
    items: list[OrderItem]
    total: int = 0
