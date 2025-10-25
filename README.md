# include-copy
include-copyはwebページを作成時にメニューやヘッダーなどを外部からincludeするシンプルなツールです。
python3で開発しました。
簡易的なWebページ作成に活用できると思います。
GitHub Copilotに手伝ってもらいました。

** このリポジトリはGit練習用ですが、実際に使用可能です。 **

## Features
.htmlファイルのインクルードしたい箇所に以下の様に記述し、include-copy.pyを実行することで
指定した外部ファイルをインクルードして、指定フォルダーに出力します。
<code><!-- @include-file="../include/menu.html"--></code>

その他、インクルード指定が無いファイルや、画像ファイル、cssファイル、jsファイルはそのままコピーします。

## How do I run this?
python3をインストールしている環境で、以下のように実行してください。
例: 以下のフォルダ構成で実行する場合
　your-project/
    include_copy.py
    source/
        index.html
        *.html
    include/
        menu.html
    www/
　
  python include_copy.py ./source ./www

## Note
今のところ、Windowsのpython3でのみ動作確認しています。
