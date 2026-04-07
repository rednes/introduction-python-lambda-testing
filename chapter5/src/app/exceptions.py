class PaymentError(Exception):
    pass


class PaymentTimeoutError(PaymentError):
    pass


class PaymentAPIError(PaymentError):
    def __init__(self, status_code: int) -> None:
        self.status_code = status_code
        super().__init__(f"Payment API error: {status_code}")
