import boto3
import os

# モジュールレベルで初期化（コールドスタート最適化）
_dynamodb = boto3.resource("dynamodb")
_TABLE_NAME = os.environ["TABLE_NAME"]


def calculate_total(items: list[dict]) -> int:
    """注文明細から合計金額を計算する（10,000円以上は10%割引）"""
    subtotal = sum(item["price"] * item["quantity"] for item in items)
    if subtotal >= 10000:
        return int(subtotal * 0.9)
    return subtotal


def save_order(order_id: str, items: list[dict], total: int) -> None:
    table = _dynamodb.Table(_TABLE_NAME)
    table.put_item(Item={"order_id": order_id, "items": items, "total": total})


def handler(event, context):
    items = event.get("items", [])
    total = calculate_total(items)
    save_order(event["order_id"], items, total)
    return {"statusCode": 200, "body": {"data": {"total": total}}}
