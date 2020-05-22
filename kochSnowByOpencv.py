#opencv 下实现 科赫曲线
import cv2 as cv
import numpy as np
import time 
import math

def koch(img,start, end, level,color=(0,0,255),thick=1):
   if(level == 0):
      cv.line(img,start, end, color=color,thickness=thick)
   else:
      p0 = start
      p4 = end
      x0, y0 = start
      x4, y4 = end
      side = math.sqrt((x4-x0)**2+(y4-y0)**2) / 3
      angle = math.atan((y0 - y4)/(x4 - x0)) + math.pi/3 #折边相对原坐标系的角度（弧度）
      
      #计算第一个转折点的坐标
      x1 = (2 * x0 + x4)/3
      y1 = (2 * y0 + y4)/3
      p1 = (round(x1), round(y1))

      #计算第二个转折点的坐标
      x2 = x1 + side * math.cos(angle)
      y2 = y1 - side * math.sin(angle)
      p2 = (round(x2), round(y2))

      #计算第三个转折点，
      x3 = (x0 + 2 * x4) / 3
      y3 = (y0 + 2 * y4) / 3
      p3 = (round(x3), round(y3))
      print(p0,p1,p2,p3,p4,angle,side*3)
      cv.line(img, p0, p1, color=color, thickness=thick)
      cv.line(img, p1, p2, color=color, thickness=thick)
      cv.line(img, p2, p3, color=color, thickness=thick)
      cv.line(img, p3, p4, color=color, thickness=thick)

      koch(img,p0, p1, level - 1)
      koch(img,p1, p2, level - 1)
      koch(img,p2, p3, level - 1)
      koch(img,p3, p4, level - 1)

img = np.zeros((512, 512,3), np.uint8)
koch(img, (10,500),(500,500),3)
cv.imshow("koch", img)
cv.waitKey(0)
cv.destroyAllWindows()
