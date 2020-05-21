#进度条
import time

scale = 50
for i in range(1,scale + 1):
   pre = '*' * i
   nex = '.' * (scale - i)
   
   prec = i / scale * 100
   print("\r{:^4.2f}%[{}{}]".format(prec,pre,nex), end="")

   time.sleep(0.1)