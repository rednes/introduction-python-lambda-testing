# Chapter 2 — 依存性注入とモックによるテスト

DI パターンでレイヤーを分離し、MagicMock でリポジトリをモックします。
moto を使わず pytest だけで動かせる構成です。

## テストの実行

```bash
cd chapter2
uv sync --dev
uv run pytest
```

## 構成

```
chapter2/
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
