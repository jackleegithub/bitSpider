#爬取 网站爱购网,利用正则表达式解析数据
# http://www.imaijp.jp/yahoo/query/query-iphone
# http://www.imaijp.jp/yahoo/query/query-iphone@offset-20
# http://www.imaijp.jp/yahoo/query/query-iphone@offset-40

import requests
import re
from bs4 import BeautifulSoup

def getHtmlText(url):
   try:
      ua = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
      r = requests.get(url, headers = ua, timeout =30)
      r.raise_for_status()
      r.encoding = r.apparent_encoding

      return r.text
   except:
      return ""

def parsePage(ls, html):
   '''ls: 保存结果的列表'''
   '''html: 搜素页面的 文本'''
   try:
      pattern = re.compile('(?<=searchkey=iphone.html">).+(?=</a></h1>)')#零宽度正向断言，不能有数量关键字
      lsname = pattern.findall(html)
      pattern = re.compile("(?<=<span class=\"prcis gred\">¥)[\\d,]+(?=</span>)")
      lsprice = pattern.findall(html)
      for i in range(len(lsname)):
         name = lsname[i]
         price = lsprice[i].replace(",","")
         ls.append((name,price))
   except:
      pass#忽略掉解析错误
def parseBySoup(ls, html):
   '''ls: 保存结果的列表'''
   '''html: 搜素页面的 文本'''
   '''
   <div class="goodbox">
		<ul>		 
		<li style="position:relative;">
			<h1><a href="/yahoo/item/v717653185&searchkey=iphone.html">【美品】iPhone11pro Max 512GB SoftBank スペースグレー　消費税無し送料無料　一円スタート</a></h1>
         <div style="width:100%;height:45px;" class="itemPrice">
				<span class="prcis gred">¥8,668</span> 
   '''
   try:
      soup = BeautifulSoup(html, 'html.parser')
      goodbox = soup.find('div',class_="goodbox")
      lsname = goodbox.find_all("h1")
      lsprice = goodbox.find_all("span",class_="prcis gred")
      
      for i in range(len(lsname)):
         name = lsname[i].string
         price = lsprice[i].string[1:].replace(",","")
         ls.append((name,price))
   except:
      pass#忽略掉解析错误

def printGoodsList(ls):
   '''ls: 保存结果的列表'''
   tempale = "{:4}\t{:8}\t{:16}"
   print(tempale.format("序号","价格","名称"))
   seq = 0
   for good in ls:
      seq = seq + 1
      print(tempale.format(seq, good[1],good[0]))


def main():
   #goods = 'iphone'
   depth = 2
   base = 'http://www.imaijp.jp/yahoo/query/query-iphone@offset-'
   lsInfo = []
   for i in range(depth):
      try:
         url = base + str(i * 20)
         html = getHtmlText(url)
         #parsePage(lsInfo, html)
         parseBySoup(lsInfo, html)
      except:
         print("Error")
         continue
   
   printGoodsList(lsInfo)


if __name__ == '__main__':
   main()