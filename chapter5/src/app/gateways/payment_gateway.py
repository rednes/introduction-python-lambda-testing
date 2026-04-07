from typing import Any

import requests

from app.exceptions import PaymentAPIError, PaymentTimeoutError


# requests モジュールはステートレスで初期化コストがないため、boto3 クライアントのように
# DI（依存性注入）でシングルトンを使い回す設計はしない。
# テスト時は responses ライブラリが HTTP 通信をインターセプトするため、
# ここでは DI を用いない構造とする。
class PaymentGateway:
    def __init__(self, url: str, timeout: int = 5, max_retries: int = 3):
        self._url = url
        self._timeout = timeout
        self._max_retries = max_retries

    def process(self, order_id: str, amount: int) -> dict[str, Any]:
        """外部決済APIを呼び出して決済処理を行う（タイムアウト・5xxエラー時にリトライ）"""
        try:
            return self._request(order_id, amount)
        except requests.Timeout as e:
            raise PaymentTimeoutError() from e
        except requests.HTTPError as e:
            raise PaymentAPIError(e.response.status_code) from e

    def _request(self, order_id: str, amount: int) -> dict[str, Any]:
        """リトライ込みで HTTP リクエストを送る。requests 例外はそのまま raise する。"""
        last_exc: Exception | None = None
        for _ in range(self._max_retries):
            try:
                response = requests.post(
                    self._url,
                    json={"order_id": order_id, "amount": amount},
                    timeout=self._timeout,
                )
                response.raise_for_status()
                return response.json()
            except requests.Timeout as e:
                last_exc = e
            except requests.HTTPError as e:
                if e.response.status_code < 500:
                    raise
                last_exc = e
        raise last_exc  # type: ignore[misc]
