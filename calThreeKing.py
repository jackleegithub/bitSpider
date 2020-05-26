#《三国演义》人物出场统计实例
import jieba
path = r'd:\Learn\python\bitSpider\res\threekingdoms.txt'
txt = ''
with open(path,'rt', encoding='utf-8') as f:
   txt = f.read()

counts = {}
exclude = ["将军","却说", "二人", "不可", "荆州", "不能", "如此", "商议", "如何", "军士","左右","军民","引兵","次日","天下","东吴","于是","今日","大喜"]
words = jieba.lcut(txt)
for word in words:
   if len(word) <= 1:
      continue
   elif word == '玄德曰' or word == '玄德':
      rword = '刘备'
   elif word == '关公' or word == '云长':
      rword = '关羽'
   elif word == '诸葛亮' or word == '孔明曰':
      rword = '孔明'
   elif word == '丞相' or word == '孟德':
      rword = '曹操'
   else:
      rword = word

   counts[rword] = counts.get(rword, 0) + 1

for key in exclude:
   del counts[key]
items = list(counts.items())
items.sort(key = lambda x: x[1], reverse = True)

for i in range(10):
   word, count = items[i]
   print("{0:{2}>5}:{1:>5}".format(word, count, "\u3000"))#中英文混排，填充字符用中文空格填充，chr(12288)== "\u3000"
