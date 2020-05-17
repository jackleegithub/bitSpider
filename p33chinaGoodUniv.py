#中国好大学排名
import requests
from bs4 import BeautifulSoup
import time

#获取网页的内容 url = http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html
def getHtmlText(url):
   ua = {
      "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
   }
   try:
      r = requests.get(url, headers = ua, timeout=30)
      r.raise_for_status()
      r.encoding = r.apparent_encoding
      return r.text
   except:
      return ""

def fillUnivList1(ulist, html):
   soup = BeautifulSoup(html,"html.parser")
   trs = soup.find('tbody').find_all('tr')#返回列表，速度慢
   for tr in trs:
      info = []
      for td in tr.find_all('td')[:4]:
         info.append(td.string)
      ulist.append(info)

def fillUnivList(ulist, html):
   soup = BeautifulSoup(html, "html.parser")
   for tag in soup.find('tbody').children:
      if isinstance(tag, type(soup.html)):
         tds = tag.find_all('td')
         ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])

   


def printUnivList(ulist, num):
   #中英文混排，填充字符用中文空格填充，chr(12288)== "\u3000"
   template = "{0:^10}\t{1:{3}^12}\t{2:^6}"
   print(template.format("排名","学校","得分",chr(12288)))
   for i in range(num):
      u = ulist[i]
      print(template.format(u[0],u[1],u[2],"\u3000"))
   print("Suc" + str(num))

def main():
   uinfo = []
   url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
   html = getHtmlText(url)
   fillUnivList1(uinfo, html)
   printUnivList(uinfo, 20)   

if __name__ == '__main__':
   start = time.time()
   main()
   end = time.time()
   print(end -start)