from order_handler import calculate_total, save_order, handler


def test_empty_items():
    assert calculate_total([]) == 0


def test_exact_threshold():
    items = [{"price": 10000, "quantity": 1}]
    assert calculate_total(items) == 9000


def test_no_discount_below_threshold():
    items = [{"price": 3000, "quantity": 2}]
    assert calculate_total(items) == 6000


def test_discount_applied_at_threshold():
    items = [{"price": 6000, "quantity": 2}]
    assert calculate_total(items) == 10800


def test_calculate_total_truncation():
    """割引後の端数は切り捨てられる"""
    items = [{"price": 10001, "quantity": 1}]
    assert calculate_total(items) == 9000


def test_multiple_items():
    items = [
        {"price": 2000, "quantity": 3},
        {"price": 1000, "quantity": 5},
    ]
    assert calculate_total(items) == 9900


def test_save_order(dynamodb_table):
    items = [{"price": 3000, "quantity": 3}]
    save_order("order-001", items, 9000)
    table = dynamodb_table.Table("orders")
    response = table.get_item(Key={"order_id": "order-001"})
    assert response["Item"]["items"] == items
    assert response["Item"]["total"] == 9000


def test_handler(dynamodb_table):
    event = {
        "order_id": "order-001",
        "items": [{"price": 5000, "quantity": 3}],
    }
    result = handler(event, {})
    assert result["statusCode"] == 200
    assert result["body"]["data"]["total"] == 13500
