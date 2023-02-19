# 朝ごはんアプリ

## 導入

1. 導入先のディレクトリを作る

2. 導入先のディレクトリに移動する

3. 以下のコマンドを実行する

   ```git clone https://github.com/alice37308108/django_breakfast.git .```

***

## 起動まで

1. 仮想環境を作る

``` shell
python -m venv venv
```

2. 仮想環境に入る

``` shell
venv\Scripts\activate
```

3. 必要なパッケージをインストール

```shell
pip install -r requirements.txt
```

4. マイグレーション(データベースの設定)

```shell
python manage.py migrate
```

5. ローカルサーバーを起動

```shell
python manage.py runserver
```

(サーバの終了は、 [Ctrl] + [C] で)

6. ブラウザで管理画面にログイン

`http://127.0.0.1:8000/admin/` からログインできることを確かめる

動作確認できたら、 [Ctrl] + [C] でいったんサーバを止める。

***

## サンプルデータの投入

1. 管理画面ログイン用のスーパーユーザーを作成

```shell
python manage.py createsuperuser
```

2. fixture からデータをロード

```shell
python python manage.py loaddata fixtures/breakfast.json
```

サンプルデータ投入が済んだら、以下のページ等で表示を確かめてください。  
`http://127.0.0.1:8000/list/`

