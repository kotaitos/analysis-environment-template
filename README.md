# Jupyter+MySQL分析環境テンプレート
`Docker Compose`で`Python(Jupyter)`+`MySQL`分析環境構築

# 起動
- `ms-vscode-remote.remote-containers`をインストール
- `Dev Containers: Reopen in Container`を選択

# 構成
- Docker Compose version v2.23.0-desktop.1
- Docker version 24.0.6
- MySQL  Ver 8.0.33
- Python 3.11.9

> [!NOTE]
> その他のライブラリなどのバージョンはrequirements.txtを参照してください。

# ディレクトリの説明
- `core/`: 中心的な機能を提供するパッケージ
- `crud/`: CRUD機能を提供するパッケージ
- `migrations/`: マイグレーション関連ファイル格納先(`alembic`により自動生成)
- `models/`: DBのテーブル定義ファイルの格納先
- `notebooks/`: notebookの格納先

# マイグレーション
- マイグレーションを作成
```
alembic revision --autogenerate -m "some message"
```

> [!NOTE]
> `alembic`は`init`+`models/`を参照するように設定済みです。
