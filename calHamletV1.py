#Hamlet英文词频统计实例,分析res/hamlet.txt
import re

#字符串操作
def hamlet1(path):
   txt = ''
   with open(path, 'rt') as f:
      txt = f.read()
      txt = txt.lower()
      for ch in '''!@#$%^&*()_+-=[]:",./<>?|\\;`'~''':
         txt = txt.replace(ch, ' ')
   counts = {}
   for word in txt.split():
      counts[word] = counts.get(word, 0) + 1

   items = list(counts.items())
   items = sorted(items, key = lambda x: x[1],reverse=True)
   for i in range(10):
      word, count = items[i]
      print("{:>10}:{:>5}".format(word, count))

#正则直接分割
def hamlet2(path):
   txt = ''
   with open(path, 'rt') as f:
      txt = f.read()
      txt = txt.lower()

   pattern = re.compile(r'[^\w]')
   words = pattern.split(txt)
   counts = {}
   for word in words:
      if word != "":#空的字符串
         counts[word] = counts.get(word, 0) + 1

   items = list(counts.items())
   items = sorted(items, key = lambda x: x[1],reverse=True)
   for i in range(10):
      word, count = items[i]
      print("{:>10}:{:>5}".format(word, count))

path = r'd:\Learn\python\bitSpider\res\hamlet.txt'
hamlet2(path)
