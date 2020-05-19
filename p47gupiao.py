# -*- coding:utf-8 -*-
'''
股票信息爬取
目录网页：stockListUrl = 'http://quote.eastmoney.com/stock_list.html',获取所有上证和深交所的股票代码。
详细页面：stockInfoUrl = 'http://so.cfi.cn/so.aspx?txquery=xxxxxxxx',获取股票的详细信息。
都是用正则表达式。利用正向断言和分组获取数据。注意python断言不能使用数量修饰符（定宽）和括号的转义。
作者：李志新
版本：1.1
语言：python
日期：2020-5-19
'''
import requests
from bs4 import BeautifulSoup
import re
import os

#获取网页HTML代码
def getHtmlText(url,code='utf-8'):
   '''
   url:网页的网址
   code:网页编码方式，默认是 utf-8
   '''
   try:
      r = requests.get(url,timeout = 30)
      r.raise_for_status()
      r.encoding = code
      return r.text
   except:
      return ""

#获取目录页的股票代码，存储在列表中。
def getStockList(lsStock, url):
   '''
   lsStock: 存储股票代码的列表
   url: 目录页的网址
   '''
   html = getHtmlText(url)
   try:
      partten = re.compile('(?<=<li><a target="_blank" href="http://quote.eastmoney.com/).+(?=.html">)')
      for it in partten.finditer(html):
         lsStock.append(it.group(0))   
   except:
      pass

#获取股票的详细信息   
def getStockInfo(lsStock, url, savePath):#by re
   '''
   lsStock:存储股票代码的列表，输入
   url: 股票详细信息的网址，'http://so.cfi.cn/so.aspx?txquery='+stock_code，拼接成合法的url
   savePath: 股票详细信息保存的文件。
   '''
   count = 0
   length = len(lsStock)
   #定义模式
   pattern = None
   try:
      pattern = re.compile('''<td id="tdquote" style="width:240px;vertical-align:top "><table style=width:100% class='quote'><tr><td>(.+?)&nbsp;<a href='http://quote.cfi.cn/quote_.{6,}.html' target='_blank'>行情</a></td><td>\[(.+?)\]</td></tr><tr><td>最　新:<span style=color:rgb\(0,102,0\)>(.+?)</span></td><td>开　盘:(.+?)</td></tr><tr><td>涨跌幅:<span style=color:rgb\(0,102,0\)>(.+?)</span></td><td>涨　跌:<span style=color:rgb\(0,102,0\)>(.+?)</td></tr><tr><td>最　高:(.+?)</td><td>最　低:(.+?)</td></tr><tr><td>成交量:(.+?)</td><td>换　手:(.+?)</td></tr></table>''')
   except Exception as e:
      print("正则模式字符串错误:",e) 

   for code in lsStock:
      html = getHtmlText(url + code)
      if html== "":
         continue
      elif pattern:
         match = pattern.search(html)
         if match:
            #写入文件
            with open(savePath,'at', encoding='utf-8') as f:
               f.write(",".join(match.groups()) +"\n")
            
      count = count + 1
      print('\r当前进度:{:.2f}%'.format(count*100/length), end="")

def getStockInfoBS(lsStock, url, savePath):
   count = 0
   length = len(lsStock)
   for code in lsStock:
      html = getHtmlText(url + code)
      try:
         if html== "":
            continue
         else:
            soup = BeautifulSoup(html, "html.parser")
            trs = soup.find('table',class_="quote").findAll("tr")
            info=[]
            info.append(trs[0].findAll("td")[0].contents[0].string.strip())
            info.append(trs[0].findAll("td")[1].string[1:-1])
            #最　新:5.16	开　盘
            info.append(trs[1].findAll("td")[0].find("span").string)
            info.append(trs[1].findAll("td")[1].string.split(":")[1])
            #涨跌幅: 	涨　跌
            info.append(trs[2].findAll("td")[0].find("span").string)
            info.append(trs[2].findAll("td")[1].find("span").string)
            #最　高:5.29	最　低:5.13
            info.append(trs[3].findAll("td")[0].string.split(":")[1])
            info.append(trs[3].findAll("td")[1].string.split(":")[1])
            #成交量:658万股	换　手:0.80%
            info.append(trs[4].findAll("td")[0].string.split(":")[1])
            info.append(trs[4].findAll("td")[1].string.split(":")[1])
            
            #写入文件
            with open(savePath,'at', encoding='utf-8') as f:
               f.write(",".join(info) +"\n")
               count = count + 1
               print('\r当前进度:{:.2f}%'.format(count*100/length), end="")
      except:
         count = count + 1
         print('\r当前进度:{:.2f}%'.format(count*100/length), end="")
         continue

def main():
   stockListUrl = 'http://quote.eastmoney.com/stock_list.html'
   stockInfoUrl = 'http://so.cfi.cn/so.aspx?txquery='

   path,filename = os.path.split(os.path.abspath(__name__))
   savePath = os.path.join(path,'stockinfo.csv')
   
   lsStock = []
   getStockList(lsStock, stockListUrl)
   getStockInfo(lsStock, stockInfoUrl, savePath)

if __name__ == '__main__':
   main()