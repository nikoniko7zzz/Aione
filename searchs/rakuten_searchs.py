# 楽天APIを使わない方法

# 使用するライブラリの宣言
# Requests（Webページの情報を取得できる）を使う
import requests
# bs4（取得したURL内のHTML要素を操作できる）に含まれる「BeautifulSoup」という部品のみ使う
from bs4 import BeautifulSoup
import sys
import random


# 楽天から45件抽出
# def get_rakuten():

url = "https://search.rakuten.co.jp/search/mall/お中元%E3%80%80パン%E3%80%80テレビ/"
# Requestsを使ってWebページ情報を取得
html=requests.get(url)
# BeautifulSoupを使って解析
soup = BeautifulSoup(html.text,'html.parser')
# print(soup)

items=soup.select('.searchresultitem')
# get_rakuten()

image_elem = soup.select("img")# imgタグを全部取得

a_elem = soup.select('a')

href_elem = soup.select('a[href*="item.rakuten"]')

# トップの写真をリストにする
image_list = []
for i in image_elem:
    # attrsでsrcをひとつづつリスト化
    src_fact = i.attrs["src"] 
    image_list.append(src_fact) 
    img_key = '275:275'
    images = [ s for s in image_list if img_key in s ]
# print(images)  
# print(len(images))  

# 商品名をリストにする
titles = []
for i in items:
    title = i.select_one('.title').text.replace('\n','')
    titles.append(title) 
# print(titles)  
# print(len(titles)) 

# 価格をリストにする
prices = []
for i in items:
    price = i.select_one('.price').text.replace('\n','')
    prices.append(price) 
# print(prices)
# print(len(prices))

# リンクをリストにする
link_list = []
for i in href_elem:
    link = i.get('href')
    link_list.append(link) 
    # 偶数だけ取り出す
    links = link_list[::2]
# print(links)
# print(len(links))


htmlに表示するように一つ選ぶ
random = random.randint(1, 45)
print(images[random])  
print(titles[random])  
print(prices[random])
print(links[random])


# url_one = links[random]
# html_one=requests.get(url_one)
# # BeautifulSoupを使って解析
# soup_one = BeautifulSoup(html_one.text,'html.parser')
# # print(soup)

# items=soup_one.select('.searchresultitem')
# # get_rakuten()

# image_elem = soup.select("img")# imgタグを全部取得

# a_elem = soup.select('a')

# ppp = soup.select('a[href*="item.rakuten"]')

# image_list = []
# for i in image_elem:
#     # attrsでsrcをひとつづつリスト化
#     src_fact = i.attrs["src"] 
#     image_list.append(src_fact) 
#     img_key = '275:275'
#     images = [ s for s in image_list if img_key in s ]
# print(images)  
# print(len(images))  

# htm = HTML('''
# <!-- <style>
#   .color1{ color: green; }
#   .color2{ color: #fff; background-color: #f00; }
# </style> -->
# <div>
#   <p>{% images[random] %}</p>
#   <p>{% titles[random] %}</p>
#   <p>{% prices[random] %}</p>
#   <p>{% links[random] %}</p>

#   <div class='color1'>Hello World!</div>
#   <b class='color2'>こんちは！</b>
# </div>
# ''')
 
# display(htm)

