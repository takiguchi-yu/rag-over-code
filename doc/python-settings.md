## Getting Pyenv

pyenv で Python の複数バージョンを管理します。

### 前提環境

セットアップするときの前提環境です。

- OS: macOS Ventura 13
- Shell: Fish 3.6

### インストール方法

`pyenv` をインストールします。インストール済みの場合この手順は不要です。

```sh
brew update
brew install pyenv
pyenv --version
```

### シェルのセットアップ

```sh
set -Ux PYENV_ROOT $HOME/.pyenv
fish_add_path $PYENV_ROOT/bin

# 以下のコマンドで設定ファイルに設定を追加 ~/.config/fish/config.fish
pyenv init - | source
```

### pyenv 使い方

インストール可能な python を確認します。

```sh
pyenv install --list
```

インストールします。

```sh
pyenv install <Pythonバージョン>
```

インストールしたバージョンを確認します。

```sh
pyenv versions
```

バージョンを切り替えます。

```sh
# ユーザーアカウント全体に適用
pyenv global <Pythonバージョン>

# 現在のシェルセッションのみ
pyenv shell <Pythonバージョン>

# 現在のディレクトリ（またはそのサブディレクトリ）にいるときのみ
pyenv local <Pythonバージョン>
```

#### 参考資料

- https://github.com/pyenv/pyenv?tab=readme-ov-file#unixmacos

## Python

依存関係のパッケージをインストールします。

```sh
pip install --upgrade -r requirements.txt
```

インストール済みのパッケージのバージョンを確認します。

```sh
pip list

# アップデートが必要なパッケージのリスト
pip list -o

# パッケージの詳細を確認する場合
pip show <パッケージ名>
```

パッケージを更新します。

```sh
pip install -U <パッケージ名>
```

依存関係の更新をチェックします。

```sh
pip check
```

パッケージを一括更新します。pip-review というパッケージを使用します。

```sh
# すべてのパッケージを一括更新
pip-review --auto
```

現在の環境のパッケージを出力します。

```sh
pip freeze > requirements.txt
```

依存関係の競合をチェックします。

```sh
pip check
```
