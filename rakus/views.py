from django.contrib.auth.decorators import login_required
# from searchs.models import Search
# from django.shortcuts import render, redirect, get_object_or_403
from django.shortcuts import render
# from searchs.forms import SearchForm




# 楽天APIを使わない方法
# 使用するライブラリの宣言
# Requests（Webページの情報を取得できる）を使う
import requests
# bs4（取得したURL内のHTML要素を操作できる）に含まれる「BeautifulSoup」という部品のみ使う
from bs4 import BeautifulSoup
import sys
import random



def top(request):
    return render (request, "rakus/top.html")

@login_required
def raku_new(request):
    return render(request,'rakus/raku_new.html') 
    

@login_required
def raku_set(request):
    return render(request,'rakus/raku_set.html') 
    
@login_required
def raku_get(request):
    return render(request,'rakus/raku_get.html') 
    

random = random.randint(1, 45)
@login_required
def raku_search(request):
    # search_key = {
    #     'keyword1': request.GET.get('keyword1'),
    #     'keyword2': request.GET.get('keyword2'),
    #     'keyword3': request.GET.get('keyword3'),
    # }
    
    # お菓子/?max=5000&min=4000
    
    keyword1 = request.GET.get('keyword1')
    keyword2 = request.GET.get('keyword2')
    keyword3 = request.GET.get('keyword3')
    max = request.GET.get('max')
    max_yen = "?max=" + max
    min_yen = "&min=" + str(int(max)-1000)

    url_basic_1 = "https://search.rakuten.co.jp/search/mall/"
    url_basic_in = "%E3%80%80"
    url_basic_2 = "%E3%80%80ギフト%E3%80%80テレビ/" + max_yen + min_yen + "&s=5"
    
    # https://search.rakuten.co.jp/search/mall/お中元%E3%80%80%E3%80%80ギフト%E3%80%80テレビ/&s=5?max=5000&min=4000
    
    url = ""
    if keyword2 == "" and keyword3 == "":
        url = url_basic_1 + keyword1 + url_basic_2
    elif keyword3 == "":
        url = url_basic_1 + keyword1 + url_basic_in + keyword2 + url_basic_2
    else:
        url = url_basic_1 + keyword1 + url_basic_in + keyword2 + url_basic_in + keyword3 + url_basic_2

    # url = "https://search.rakuten.co.jp/search/mall/{{ keyword1 }}%E3%80%80{{ keyword2 }}%E3%80%80テレビ/"
    # url = "https://search.rakuten.co.jp/search/mall/お中元%E3%80%80お菓子%E3%80%80映え%E3%80%80テレビ/"
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
    print(links)
    # print(len(links))
    
    
    # htmlに表示するように一つ選ぶ
    # random = random.randint(1, 45)
    # print(images[random])  
    # print(titles[random])  
    # print(prices[random])
    # print(links[random])
    
    # context = {
    #     keyword1, keyword2, keyword3, images[random], titles[random],
    #     "price": prices[random],
    #     "link": links[random],
    # }    
    context = {
        "keyword1": keyword1,
        "keyword2": keyword2,
        "keyword3": keyword3,
        # "image": images[random],
        # "title": titles[random],
        # "price": prices[random],
        # "link": links[random],
        # "image": images[4],
        # "title": titles[4],
        # "price": prices[4],
        # "link": links[4],
        "image1": images[1],
        "title1": titles[1],
        "price1": prices[1],
        "link1": links[1],
        
        "image2": images[2],
        "title2": titles[2],
        "price2": prices[2],
        "link2": links[2],
        
        "image3": images[3],
        "title3": titles[3],
        "price3": prices[3],
        "link3": links[3],
    }
    return render(request, 'rakus/raku_search.html', context)

