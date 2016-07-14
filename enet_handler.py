# -*- encoding: utf-8 -*-
# 文字コードの設定
# インポートする
import re
import mechanize
from bs4 import BeautifulSoup

# urllib2
# beautifulsoup

# インスタンス作成
br = mechanize.Browser()

# 非ロボット化（これは何？）
br.set_handle_robots('false')

# 1)トップ画面から診察受付へ
# まずは、診察受付のURLを開く
response = br.open("http://euke.jp/enet/do/usr/entry/select/top?ID=72")
print "START" + response.read() + "END"  # 検証用
source = str(response.get_data())
#print "SourceStart" + source + "SourceEnd"
# セッションIDをGETする。
# logo_bg を探す
# そこに入っているリンク先URLをGETする。
# そこから正規表現で、jsessionid=から?ID=までをGETする。
# イメージ：<a href="/enet/do/usr/search/hospital;jsessionid=B6A7A0120B778A559732121CE9B4C33F?ID=72">
# beautifulsoupにHTMLソースを渡す
soup = BeautifulSoup(source, "html.parser")
# セッションIDのありかをゲットする
# assert isinstance(soup.find("img", name="entry").previous_sibling,object )
#print soup.find_all("td", attrs={"class": "logo_bg"})

#print soup.find("a",re.compile("jsessionid"))
print soup.find("a",{href:re.compile("\/enet\/do/usr\/search\/hospital\;jsessionid=[A-Z0-9]\?ID=72")})

#soup.a.get("href")
# assert isinstance(SessionIdLink, object)
#print "a"+soup.prettify()+"end"
#assert isinstance(contents.string, object)
soup.prettify()

# 正規表現あるいはBeautifulsoupの関数でセッションIDをGETして、変数に格納する。
# まずは、最初の



# 次に、リンクを開いてみる。
# br.page.link_with(:text => "ここをクリックしたい").click



# 2)フォームをサブミット
# 今回は不要：外部ファイルからIDとパスワードをGETする
# FORMをセレクト

# FORMに入力する

# SUBMITする

# SUBMITの結果をレスポンスで受け取る

# 次の画面
