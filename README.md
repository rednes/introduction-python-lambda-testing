# introduction-python-lambda-testing

[pytest](https://docs.pytest.org/) と [moto](https://github.com/getmoto/moto) を使って、AWS Lambda（Python）の単体テストを段階的に学ぶチュートリアルです。

詳しくはこちらのブログをご覧ください。

- [pytestとmotoで始めるLambda単体テスト入門 \| DevelopersIO](https://dev.classmethod.jp/articles/introduction-python-lambda-testing/)

## 前提条件

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## 主な使用ライブラリ

| ライブラリ | 用途 |
|-----------|------|
| [pytest](https://docs.pytest.org/) | テストフレームワーク |
| [pytest-cov](https://pytest-cov.readthedocs.io/) | カバレッジレポート |
| [moto](https://github.com/getmoto/moto) | AWS サービスのモック |
| [responses](https://github.com/getsentry/responses) | HTTP リクエストのモック（Chapter 5） |

## Chapter 一覧

| Chapter | テーマ |
|---------|--------|
| [Chapter 1](./chapter1/) | テスタブルな設計の基本 |
| [Chapter 2](./chapter2/) | 依存性注入とモックによるテスト |
| [Chapter 3](./chapter3/) | リポジトリ層を moto でテストする |
| [Chapter 4](./chapter4/) | エラーハンドリングとバリデーション |
| [Chapter 5](./chapter5/) | 外部 API 呼び出しのモック |

## ディレクトリ構成

各 Chapter は独立したプロジェクト（`pyproject.toml`）として構成されています。

```
introduction-python-lambda-testing/
├── chapter1/          # テスタブルな設計の基本（カバレッジを含む）
│   ├── pyproject.toml
│   ├── src/
│   └── tests/
├── chapter2/          # 現実的なファイル分割（全層DI・モック）
├── chapter3/          # リポジトリ層をmotoでテストする
├── chapter4/          # エラーハンドリングとバリデーションのテスト
└── chapter5/          # 外部API呼び出しのモック
```

## テストの実行

各 Chapter ディレクトリで以下を実行します。

```bash
cd chapterN
uv sync --dev
uv run pytest
```
