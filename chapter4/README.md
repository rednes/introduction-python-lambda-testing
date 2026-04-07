# Chapter 4 — エラーハンドリングとバリデーション

入力値の検証とカスタム例外を導入し、エラーを適切な HTTP ステータスコードに変換します。
DynamoDB の `ClientError` はドメイン例外に変換して上位層に漏らさない設計にしています。

## テストの実行

```bash
cd chapter4
uv sync --dev
uv run pytest
```

## 構成

```
chapter4/
├── src/
│   ├── controller.py
│   └── app/
│       ├── dependencies.py
│       ├── exceptions.py
│       ├── inputs/order_input.py
│       ├── models/order.py
│       ├── repositories/order_repository.py
│       ├── services/order_service.py
│       └── usecases/order_usecase.py
└── tests/
    ├── conftest.py
    ├── test_controller.py
    ├── test_dependencies.py
    ├── test_order_input.py
    ├── test_order_repository.py
    ├── test_order_service.py
    └── test_order_usecase.py
```
