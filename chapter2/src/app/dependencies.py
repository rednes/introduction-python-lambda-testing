import os
from functools import cache

import boto3
from app.repositories.order_repository import OrderRepository


@cache
def get_order_repository() -> OrderRepository:
    return OrderRepository(boto3.resource("dynamodb"), os.environ["TABLE_NAME"])