# リポジトリの設定
REPOSITORY_CONFIG = {
    # ソースコードのリポジトリURL
    "url": "https://github.com/takiguchi-yu/cognito-google-federation-example",
    "local_path": "./local_repo"  # ローカルにクローンされるリポジトリのパス
}

# ドキュメントローダーの設定
DOCUMENT_LOADER_CONFIG = {
    "path": "./local_repo",  # ドキュメントが保存されているディレクトリのパス
    "glob_pattern": "**/*",  # ファイル検索に使用されるglobパターン
    # 取り込むファイルの拡張子
    "suffixes": [".py", ".js", ".ts", ".tsx", ".css", ".php", ".md", ".json", ".html"],
    "exclude_patterns": ["**/.git/**"]  # 除外するパターン
}

# テキストスプリッターの設定
TEXT_SPLITTER_CONFIG = {
    "chunk_size": 2048,  # 分割するチャンクのサイズ
    "chunk_overlap": 200  # チャンク間のオーバーラップサイズ
}

# ベクトルストアの設定
VECTOR_STORE_CONFIG = {
    "store_type": "chroma",  # 使用するベクトルストアのタイプ ('chroma', 'faiss', etc.)
    "embedding_model": "text-embedding-3-large",  # 使用する Embedding モデル
}
