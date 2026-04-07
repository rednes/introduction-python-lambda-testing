# introduction-python-lambda-testing

AWS Lambda の Python テストベストプラクティスを段階的に学ぶチュートリアルです。

## 前提条件

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## Chapter 一覧

| Chapter | テーマ |
|---------|--------|
| [Chapter 1](./chapter1/) | テスタブルな設計の基本 |
| [Chapter 2](./chapter2/) | 依存性注入とモックによるテスト |
| [Chapter 3](./chapter3/) | ウォームスタート対応の設計 |
| [Chapter 4](./chapter4/) | エラーハンドリングとバリデーション |
| [Chapter 5](./chapter5/) | 外部 API 呼び出しのモック |

## テストの実行

各 Chapter ディレクトリで以下を実行します。

```bash
cd chapterN
uv run pytest
```
