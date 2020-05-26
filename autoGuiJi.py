#自动轨迹绘制
import turtle as t

t.title("自动轨迹绘制")
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)

#读取数据
data = []
f = open("res/data.txt", "rt")
for line in f:
   line = line.strip()
   data.append(list(map(eval, line.split(","))))
f.close()

#自动绘制
for it in data:
   t.pencolor(it[3], it[4], it[5])
   t.fd(it[0])
   if it[1]:
      t.right(it[2])
   else:
      t.left(it[2])

t.done()