#谢尔宾斯基三角形,Sierpinski triangle
import turtle
import math

#填充色
fillColor = ('aqua',  'blue', 'fuchsia', 'gray', 'green', 'lime', 'maroon', 'navy', 'olive', 'purple', 'red', 'silver', 'teal', 'yellow')

#获取两个点的中点坐标
def getMid(a, b):
   ax, ay = a
   bx, by = b
   return ((ax + bx) / 2, (ay + by) / 2)

#通过三个点，画三角形
def drawTriangle(a, b, c):
   ax, ay = a
   bx, by = b
   cx, cy = c
   turtle.penup()
   turtle.goto(ax, ay)
   turtle.pendown()
   turtle.goto(bx, by)
   turtle.goto(cx, cy)
   turtle.goto(ax, ay)
   turtle.penup()


#递归函数实现谢尔宾斯基三角形
def sierpinskiTriangle(points, level):
   '''
   points:元组，元素是三角形三个顶点的坐标。
   level:谢尔宾斯基三角形的级数
   '''
   a, b, c = points  
   d = getMid(a, b)
   e = getMid(b, c)
   f = getMid(c, a) 
   if level == 0:#基础例子
      drawTriangle(a, b, c) 
   elif level == 1:#基础例子
      drawTriangle(a, b, c) 
      drawTriangle(d, e, f)
   else:#递归链条
      sierpinskiTriangle((a, d, f), level - 1)#正上角的三角形
      sierpinskiTriangle((b, e, d), level - 1)#右下角的三角形
      sierpinskiTriangle((c, f, e), level - 1)#左下角的三角形

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
   level = 2 #谢尔宾斯基三角形的级数
   points = ((0, 150 * math.sqrt(3)),(300, -150*math.sqrt(3)), (-300,-150*math.sqrt(3)))
   sierpinskiTriangle(points, level)

if __name__ == '__main__':
   main()
   turtle.done()
