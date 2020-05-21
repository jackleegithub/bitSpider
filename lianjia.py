#链家房价爬取
#二级目录
#1.区县信息：https://bj.lianjia.com/xiaoqu
#2.各区县的小区信息
#小区地址：https://bj.lianjia.com/xiaoqu/fengtai/pg30/    /丰台区/pg页码数字

import requests,re
import urllib.request, html.parser 
import math, random
import time #计时


def isTagA(url):
   ls = url.split('/')
   if len(ls)!= 4:
      return False
   elif ls[0] !='':
      return False
   elif ls[1] !='xiaoqu':
      return False
   elif ls[2]=='':
      return False
   elif ls[3]!='':
      return False
   elif ls[2].isalpha() == False:
      return False
   else:
      return True

class LJDistrict(html.parser.HTMLParser):
   isTagLink = False
   def handle_starttag(self, tag, attrs):
      attrs = dict(attrs)
      href= attrs.get('href','')
      if tag=='a' and isTagA(href):
         self.isTagLink = True
         self.href = urllib.request.urljoin('https://bj.lianjia.com/xiaoqu/',href)

   def handle_data(self, data):
      if self.isTagLink and len(data.strip()):
         self.txt = data
         lsDistrict.append((self.href,data))

   def handle_endtag(self, tag):
      if self.isTagLink:
         self.isTagLink = False
      

#获取北京市各区县的url 字段
url = 'https://bj.lianjia.com/xiaoqu/'
lsDistrict = []
try:
   r = urllib.request.urlopen(url)
   pageText = r.read().decode()
   parser = LJDistrict()
   parser.feed(pageText)
   parser.close()
   
except Exception as e:
   print(e)
   

for qx in lsDistrict:

   count = 0#区县小区的数量
   pagesize = 30#分页页面上小区的数量
   url = qx[0]
   try:
      r = requests.get(url)
      r.encoding = r.apparent_encoding
      pageText = r.text
      pattern = re.compile('<h2 class="total fl">共找到<span> (\\d{1,5}) </span>个')
      m = pattern.search(pageText)
      if m:
         count = math.ceil(float(m.group(1)))
      
   except Exception as e:
      print(e)

   startTime = time.perf_counter()
   pagecount = math.ceil(count / pagesize)#总页数

   for index in range(1,pagecount + 1):
      url = 'https://bj.lianjia.com/xiaoqu/fengtai/pg' + str(index)
      
      r = requests.get(url)
      r.encoding = r.apparent_encoding
      pageText = r.text
      pattern = re.compile('<a href="(https://bj.lianjia.com/xiaoqu/\\d+?/)" target="_blank">(.+)</a>')  #小区名称
      iter = pattern.finditer(pageText)
      txtResult = ""
      for it in iter:
         url = it.group(1)#小区的地址
         name = it.group(2)#小区的名称
         pattern = re.compile('<div class="totalPrice"><span>(\\d+)</span>元/m<sup>2</sup></div>') #均价
         m = pattern.search(pageText, it.end())
         if m:
            price = m.group(1)
         else:
            price = "0"

         pattern = re.compile('class="totalSellCount"><span>(\\d+)</span>套</a>')#在售套数
         m = pattern.search(pageText,it.end())
         if m:
            sellCount = m.group(1)
         else:
            sellCount = "0"

         pattern = re.compile('class="district" title=".+">(.+)</a>')#区县
         m = pattern.search(pageText,it.end())
         if m:
            district = m.group(1)
         else:
            district = ""

         pattern = re.compile('class="bizcircle" title=".+">(.+)</a>')#区域
         m = pattern.search(pageText,it.end())
         if m:
            bizcircle = m.group(1)
         else:
            bizcircle = ""
            
         r ="{},{},{},{},{},{}\n".format(name, price,sellCount, district, bizcircle,url)
         txtResult = txtResult + r
      with open('lianjia.txt','at') as f:
         f.write(txtResult)

      prec = index / pagecount * 100
      print("\r{}完成{:.2f}%，{}".format(qx[1],prec, ('>'* math.ceil(prec*0.5)).ljust(50,"|")), end="")#进度条
      time.sleep(random.randint(1,10)/10)#延时，模拟人工0.1--0.9s

   print("\n{}总共耗时{:.5f}s。".format(qx[1], time.perf_counter() - startTime))