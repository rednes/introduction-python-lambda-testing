# Chapter 5 — 外部 API 呼び出しのモック

`responses` ライブラリで HTTP 通信をモックし、リトライロジックをテストします。
Gateway 層でインフラ例外をドメイン例外に変換する Anticorruption Layer パターンを導入しています。

## テストの実行

```bash
cd chapter5
uv sync --dev
uv run pytest
```

## 構成

```
chapter5/
├── src/
│   ├── controller.py
│   └── app/
│       ├── dependencies.py
│       ├── exceptions.py
│       ├── gateways/payment_gateway.py
│       └── usecases/payment_usecase.py
└── tests/
    ├── conftest.py
    ├── test_controller.py
    ├── test_payment_gateway.py
    └── test_payment_usecase.py
```
