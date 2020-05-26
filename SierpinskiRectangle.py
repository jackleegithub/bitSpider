#谢尔宾斯基地毯,Sierpinski Rectangle
import turtle
import math

#获取两个点的1/3点的坐标
def oneThird(a, b):
   ax, ay = a
   bx, by = b
   return ((ax + (bx - ax) / 3, ay + (by - ay) / 3))

#获取两个点的2/3点的坐标
def twoThird(a, b):
   ax, ay = a
   bx, by = b
   return ((ax + (bx - ax) / 3 * 2, ay + (by - ay) / 3 * 2))


#通过四个点，画矩形
def drawRectangle(a, b, c, d, color):
   ax, ay = a
   bx, by = b
   cx, cy = c
   dx, dy = d
   turtle.penup()
   turtle.goto(ax, ay)
   turtle.fillcolor(color)
   turtle.begin_fill()
   turtle.pendown()
   turtle.goto(bx, by)
   turtle.goto(cx, cy)
   turtle.goto(dx, dy)
   turtle.goto(ax, ay)
   turtle.end_fill()
   turtle.penup()


#递归函数实现谢尔宾斯基地毯
def sierpinskiRectangle(points, level):
   '''
   points:元组，元素是三角形三个顶点的坐标。
   level:谢尔宾斯基三角形的级数
   '''
   a, b, c, d = points  
   e = oneThird(a, b)
   f = twoThird(a, b)
   g = oneThird(b, c)
   h = twoThird(b, c)
   i = oneThird(c, d)
   j = twoThird(c, d)
   k = oneThird(d, a)
   l = twoThird(d, a)
   m = oneThird(l, g)
   n = twoThird(l, g)
   o = oneThird(h, k)
   p = twoThird(h, k)

   if level == 0:#基础例子
      drawRectangle(a, b, c, d, 'black') 
   elif level == 1:#基础例子
      drawRectangle(a, b, c, d, 'black') 
      drawRectangle(m, n, o, p, 'white')
   else:#递归链条
      sierpinskiRectangle((a, e, m, l), level - 1)
      sierpinskiRectangle((e, f, n, m), level - 1)
      sierpinskiRectangle((f, b, g, n), level - 1)
      sierpinskiRectangle((n, g, h, o), level - 1)
      sierpinskiRectangle((o, h, c, i), level - 1)
      sierpinskiRectangle((p, o, i, j), level - 1)
      sierpinskiRectangle((k, p, j, d), level - 1)
      sierpinskiRectangle((l, m, p, k), level - 1)

#https://www.bilibili.com/read/cv4404215/
def sierpinskiTriangleBase(points, level):
   a, b, c = points
   if level == 0:
      drawTriangle(a, b, c)
   else:
      d = getMid(a, b)
      e = getMid(b, c)
      f = getMid(c, a)
      sierpinskiTriangle((a, d, f), level - 1)
      sierpinskiTriangle((b, e, d), level - 1)
      sierpinskiTriangle((c, f, e), level - 1)

def main():
   turtle.setup(800, 800)

   level = 3 #谢尔宾斯基三角形的级数
   points = ((-350,350), (350,350),(350,-350),(-350,-350))
   sierpinskiRectangle(points, level)

   turtle.hideturtle()
   turtle.done()
if __name__ == '__main__':
   
   main()
   
