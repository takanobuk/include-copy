
# include-copy

include-copyはwebページを作成時にメニューやヘッダーなどを外部からincludeするシンプルなツールです。
python3で開発しました。
簡易的なWebページ作成に活用できると思います。
GitHub Copilotに手伝ってもらいました。

**このリポジトリはGit練習用ですが、実際に使用可能です。**

## Features

.htmlファイルのインクルードしたい箇所に以下の様に記述し、include-copy.pyを実行することで<br>
指定した外部ファイルをインクルードして、指定フォルダーに出力します。<br>
`<!-- @include-file="../include/menu.html"-->`

その他、インクルード指定が無いファイルや、画像ファイル、cssファイル、jsファイルはそのままコピーします。<br>

## How do I run this?

python3をインストールしている環境で、以下のように実行してください。<br>
例: 以下のフォルダ構成で実行する場合<br>

- your-project/
  - include_copy.py
  - source/
    - index.html
    - *.html
  - include/
    - menu.html
  - www/
  
<br>
    python include_copy.py ./source ./www<br>

## Note

今のところ、Windowsのpython3でのみ動作確認しています。

## License

This software is released under the MIT License, see LICENSE.
