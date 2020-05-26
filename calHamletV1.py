#Hamlet英文词频统计实例,分析 res/hamlet.txt
#获取小说内容
def getText(path):
   txt = ''
   with open(path, 'rt') as f:
      txt = f.read()
      txt = txt.lower()
      for ch in '''!@#$%^&*()_+-=[]:",./<>?|\\;`'~''':
         txt = txt.replace(ch, ' ')

   return txt

txt = getText(r'd:\Learn\python\bitSpider\res\hamlet.txt')
counts = {}
for word in txt.split():
   counts[word] = counts.get(word, 0) + 1

items = list(counts.items())
items = sorted(items, key = lambda x: x[1],reverse=True)
for i in range(10):
   word, count = items[i]
   print("{:>10}:{:>5}".format(word, count))


