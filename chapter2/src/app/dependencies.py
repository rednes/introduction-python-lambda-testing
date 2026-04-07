import os
from functools import cache

import boto3
from app.repositories.order_repository import OrderRepository

_TABLE_NAME = os.environ["TABLE_NAME"]


@cache
def get_order_repository() -> OrderRepository:
    return OrderRepository(boto3.resource("dynamodb"), _TABLE_NAME)