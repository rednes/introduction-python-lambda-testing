class OrderError(Exception):
    """注文ドメインの基底例外"""


class OrderSaveError(OrderError):
    """注文の保存に失敗"""


class OrderItemValidationError(OrderError):
    """注文アイテムの入力値が不正"""
