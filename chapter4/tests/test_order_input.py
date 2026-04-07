import pytest

from app.exceptions import OrderItemValidationError
from app.inputs.order_input import parse_order_item, parse_order_items_from_event, validate_order_item
from app.models.order import OrderItem


def test_parse_order_items_from_event_valid():
    items = parse_order_items_from_event([{"price": 5000, "quantity": 3}, {"price": 1000, "quantity": 1}])
    assert items == [OrderItem(price=5000, quantity=3), OrderItem(price=1000, quantity=1)]


def test_parse_order_items_from_event_not_a_list_raises_validation_error():
    with pytest.raises(OrderItemValidationError, match="items はリスト"):
        parse_order_items_from_event("invalid")


def test_parse_order_items_from_event_none_raises_validation_error():
    with pytest.raises(OrderItemValidationError, match="items はリスト"):
        parse_order_items_from_event(None)


def test_parse_order_items_from_event_propagates_item_validation_error():
    with pytest.raises(OrderItemValidationError, match="不正なアイテムデータ"):
        parse_order_items_from_event([{"price": 1000}])


def test_parse_order_item_valid():
    item = parse_order_item({"price": 5000, "quantity": 3})
    assert item == OrderItem(price=5000, quantity=3)


def test_parse_order_item_missing_field_raises_validation_error():
    with pytest.raises(OrderItemValidationError, match="不正なアイテムデータ"):
        parse_order_item({"price": 1000})


def test_parse_order_item_unexpected_field_raises_validation_error():
    with pytest.raises(OrderItemValidationError, match="不正なアイテムデータ"):
        parse_order_item({"price": 1000, "quantity": 1, "discount": 0.1})


def test_parse_order_item_zero_price_raises_validation_error():
    with pytest.raises(OrderItemValidationError, match="price と quantity は1以上"):
        parse_order_item({"price": 0, "quantity": 1})


def test_parse_order_item_negative_quantity_raises_validation_error():
    with pytest.raises(OrderItemValidationError, match="price と quantity は1以上"):
        parse_order_item({"price": 1000, "quantity": -1})


def test_validate_order_item_zero_price_raises_validation_error():
    with pytest.raises(OrderItemValidationError, match="price と quantity は1以上"):
        validate_order_item(OrderItem(price=0, quantity=1))


def test_validate_order_item_negative_quantity_raises_validation_error():
    with pytest.raises(OrderItemValidationError, match="price と quantity は1以上"):
        validate_order_item(OrderItem(price=1000, quantity=-1))
