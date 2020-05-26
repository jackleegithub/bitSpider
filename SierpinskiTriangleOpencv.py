#谢尔宾斯基三角形,Sierpinski triangle, Opencv 实现
import cv2 as cv
import math
import numpy as np

#获取两个点的中点坐标
def getMid(a, b):
   ax, ay = a
   bx, by = b
   return (round((ax + bx) / 2), round((ay + by) / 2))

#通过三个点，画三角形
def drawTriangle(img,a, b, c,fillcolor=(0,0,255), strokecolor = (0,0,0)):
   # ax, ay = a
   # bx, by = b
   # cx, cy = c
   # cv.line(img,a, b,(0,0,255),1)
   # cv.line(img,b, c,(0,0,255),1)
   # cv.line(img,c, a,(0,0,255),1)
   pts = np.array([a,b,c], np.int32)
   pts = pts.reshape((-1,1,2))
   cv.fillPoly(img,[pts], fillcolor)

#递归函数实现谢尔宾斯基三角形
def sierpinskiTriangle(img, points, level):
   '''
   points:元组，元素是三角形三个顶点的坐标。
   level:谢尔宾斯基三角形的级数
   '''
   a, b, c = points  
   d = getMid(a, b)
   e = getMid(b, c)
   f = getMid(c, a) 
   if level == 0:#基础例子
      drawTriangle(img, a, b, c) 
   elif level == 1:#基础例子
      drawTriangle(img, a, b, c) 
      drawTriangle(img, d, e, f,fillcolor=(255,255,255))
   else:#递归链条
      sierpinskiTriangle(img, (a, d, f), level - 1)#正上角的三角形
      sierpinskiTriangle(img, (b, e, d), level - 1)#右下角的三角形
      sierpinskiTriangle(img, (c, f, e), level - 1)#左下角的三角形

def main():
   img = np.ones((800, 800, 3),np.uint8) * 255

   level = 8 #谢尔宾斯基三角形的级数
   points = ((400, 50),(750, round(350*math.sqrt(3))+50), (50, round(350*math.sqrt(3)) + 50))
   sierpinskiTriangle(img, points, level)

   cv.imshow('Sierpinski triangle', img)
   cv.waitKey(0)
   cv.destroyAllWindows()

if __name__ == '__main__':
   main()
   
