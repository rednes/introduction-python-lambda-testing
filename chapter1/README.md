# Chapter 1 — テスタブルな設計の基本

ビジネスロジックを副作用のない純粋関数として切り出し、テストしやすい構造を作ります。
DynamoDB のモックには moto を使います。

## テストの実行

```bash
cd chapter1
uv run pytest
```

## 構成

```
chapter1/
├── src/
│   └── order_handler.py
└── tests/
    ├── conftest.py
    └── test_order_handler.py
```
