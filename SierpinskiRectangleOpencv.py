#谢尔宾斯基地毯,Sierpinski Rectangle, opencv 实现
import cv2 as cv
import math
import numpy as np

#获取两个点的1/3点的坐标
def oneThird(a, b):
   ax, ay = a
   bx, by = b
   return (round(ax + (bx - ax) / 3), round(ay + (by - ay) / 3))

#获取两个点的2/3点的坐标
def twoThird(a, b):
   ax, ay = a
   bx, by = b
   return (round(ax + (bx - ax) / 3 * 2), round(ay + (by - ay) / 3 * 2))


#通过四个点，画矩形
def drawRectangle(img,a, b, c, d, color=(0,0,255)):
   pts = np.array([a,b,c,d], np.int32)
   pts = pts.reshape((-1,1,2))
   cv.fillPoly(img, [pts], color)


#递归函数实现谢尔宾斯基地毯
def sierpinskiRectangle(img, points, level):
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
      drawRectangle(img, a, b, c, d, (0,0,0)) 
   elif level == 1:#基础例子
      drawRectangle(img, a, b, c, d, (0,0,0)) 
      drawRectangle(img, m, n, o, p, (255,255,255))
   else:#递归链条
      sierpinskiRectangle(img, (a, e, m, l), level - 1)
      sierpinskiRectangle(img, (e, f, n, m), level - 1)
      sierpinskiRectangle(img, (f, b, g, n), level - 1)
      sierpinskiRectangle(img, (n, g, h, o), level - 1)
      sierpinskiRectangle(img, (o, h, c, i), level - 1)
      sierpinskiRectangle(img, (p, o, i, j), level - 1)
      sierpinskiRectangle(img, (k, p, j, d), level - 1)
      sierpinskiRectangle(img, (l, m, p, k), level - 1)


def main():
   row = 1000
   col = 1000
   img = np.ones((row, col, 3),np.uint8) * 255

   level = 5 #谢尔宾斯基三角形的级数
   assert level < 7,"级数太高，无法显示"
   points = ((50,50), (col - 50,50),(col - 50, row - 50),(50, row - 50))
   sierpinskiRectangle(img, points, level)

   cv.imshow('Sierpinski rectangle', img)
   cv.waitKey(0)
   cv.destroyAllWindows()
if __name__ == '__main__':
   
   main()
   
