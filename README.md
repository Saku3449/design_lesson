# Djangoで掲示板アプリをデザインしてみよう！

## 最初だけすること
<u></u>
プロジェクトを置いてもいいディレクトリに移動して
```terminal
git clone https://github.com/YusakuNokubi/design_lesson/
```

## 開発を始めるときにすること
<u></u>
コードを書くときに毎回行いましょう。
```terminal
source myvenv/bin/activate
```
カレントディレクトリの頭に`(myvenv)`が付いていればOK!

## 各ページの説明
<u></u>
### admin
`http://127.0.0.1:8000/admin`にアクセスするとパスワードが要求されます。
ユーザ名は`ower`、パスワードは`1`です。
ログインすると管理者画面に入ります。

BBの`PostModel`をクリックしてみましょう。追加のボタンからデータを追加できます。

試しに3つほど投稿してみましょう！

### top_page
`http://127.0.0.1:8000/list`にアクセスすると記事の一覧を見ることができます。先ほど追加したデータが一覧になっているはずです。

### detail/
`http://127.0.0.1:8000/detail/1`にアクセスすると1つ目の記事の詳細ページを見ることができます。末尾の数字を変更することで他の記事にも移動できますが、存在しない記事を指定するとエラーになるので気をつけましょう。


## 今回のタスク
今回はtop_pageとdetailを`Bootstrap`で装飾することでDjangoでのデザインを勉強してもらいます。下に示す`templates`内のhtmlファイルにBootstrapを適用するだけでもいいですが、余力があればCSSを試してみてください。完成形は2人に委ねます！

design_lesson

  ┠ BB
  
  ┠ designProject
  
  ┠ myvenv
  
  ┠ static
  
  ┠ templates
  
  ┃ ┠ base.html
  
  ┃ ┠ detail_page.html
  
  ┃ ┗ top_page.html
  
  ┠ manage.py
  
  ┗ requirements.txt

