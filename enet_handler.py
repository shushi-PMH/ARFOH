# -*- encoding: utf-8 -*-
#文字コードの設定
#インポートする
import mechanize
from bs4 import BeautifulSoup
#urllib2
#beautifulsoup

#インスタンス作成
br = mechanize.Browser()

#非ロボット化（これは何？）
br.set_handle_robots('false')

#1)トップ画面から診察受付へ
#まずは、診察受付のURLを開く
response = br.open("http://euke.jp/enet/do/usr/entry/select/top?ID=72")
print response.read()  #検証用
#セッションIDをGETする。
#logo_bg を探す
#そこに入っているリンク先URLをGETする。
#そこから正規表現で、jsessionid=から?ID=までをGETする。
#イメージ：<a href="/enet/do/usr/search/hospital;jsessionid=B6A7A0120B778A559732121CE9B4C33F?ID=72">
#beautifulsoupにHTMLソースを渡す
soup = BeautifulSoup(response, "html")
#セッションIDのありかをゲットする
#正規表現あるいはBeautifulsoupの関数でセッションIDをGETして、変数に格納する。



#次に、リンクを開いてみる。
#br.page.link_with(:text => "ここをクリックしたい").click



#2)フォームをサブミット
#今回は不要：外部ファイルからIDとパスワードをGETする
#FORMをセレクト

#FORMに入力する

#SUBMITする

#SUBMITの結果をレスポンスで受け取る

#次の画面

