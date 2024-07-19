# Mail Delivery Demo Backend

## Environments

- [node](https://nodejs.org/ja/download): 20.15.1
- [npm](https://nodejs.org/ja/download): 10.8.2

  ```bash
  volta install node
  ```

- [python](https://www.python.org/downloads/): 3.11.9

  ```bash
  pyenv install 3.11.9
  ```

## Installation

1. パッケージのインストール

```bash
npm install
```

```bash
pip install poetry
poetry config virtualenvs.in-project true
poetry install
```

## Task

test

```bash
task test
```

lint

```bash
task lint
```

format

```bash
task format
```

### Branch rule

| ブランチ名      | 役割                 | 派生元              | 詳細                                                                                                                                                                     |
| --------------- | -------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `main`          | 安定版リリース       | (default ブランチ)  | 基本的に最新版のリリースとなる予定です。                                                                                                                                 |
| `dev`           | 開発用ブランチ       | `main`              | 開発中の最新状態が反映されたブランチです。                                                                                                                               |
| `release/x.y.z` | リリース準備ブランチ | `dev`               | `hotfix`以外のリリースはこちらから行います。`main`ブランチに merge する際にタグを作成し、当該バージョンをリリースします。major, minor のアップデート管理を行う予定です。 |
| `feature/*`     | 機能開発             | `dev`               | 新機能開発用のブランチです。完了したら`dev`に merge します。                                                                                                             |
| `fix/*`         | 修正                 | `dev` , `feature/*` | 　次回リリースまでに反映したい仕様変更、バグなどの修正を行います。                                                                                                       |
| `hotfix/*`      | 緊急の修正           | `main`              | 重大なバグや緊急の修正に用います。修正が完了したら、`main`と`dev`ブランチに反映します。                                                                                  |
| `patch/*`       | 軽微な修正           | `main`              | 軽微なバグ、パッチ対応のブランチ。`hotfix`と機能としては変わりません。                                                                                                   |

demo 用 パッケージなので基本的には main ブランチの最新安定版しか使わないと思うので、各バージョンに対する個別のパッチは考えていません。

管理の煩雑さを回避するためです。
