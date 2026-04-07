# Chapter 3 — ウォームスタート対応の設計

環境変数をモジュールレベルで読み込み、Lambda のコールドスタートを最適化します。
未設定の環境変数を起動時に即座に検出するフェイルファスト設計も合わせて導入します。

## テストの実行

```bash
cd chapter3
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
