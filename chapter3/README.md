# Chapter 3 — リポジトリ層を moto でテストする

Chapter 2 の MagicMock だけでは確認できない DynamoDB 操作の正しさを、moto で検証します。
ユースケース・コントローラー層は MagicMock のまま、リポジトリ層だけ moto に切り替える構成です。

## テストの実行

```bash
cd chapter3
uv sync --dev
uv run pytest
```

## 構成

```
chapter3/
├── src/
│   ├── controller.py
│   └── app/
│       ├── dependencies.py
│       ├── models/order.py
│       ├── repositories/order_repository.py
│       ├── services/order_service.py
│       └── usecases/order_usecase.py
└── tests/
    ├── conftest.py
    ├── test_controller.py
    ├── test_dependencies.py
    ├── test_order_repository.py
    ├── test_order_service.py
    └── test_order_usecase.py
```
