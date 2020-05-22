'''
科赫曲线
科赫曲线是de Rham曲线的特例。
   1.给定线段AB，科赫曲线可以由以下步骤生成：
   2.将线段分成三等份（AC,CD,DB）
   3.以CD为底，向外（内外随意）画一个等边三角形DMC
   4.将线段CD移去
分别对AC,CM,MD,DB重复1~3。
'''
import turtle

def koch(size, n):
   if(n == 0):
      turtle.fd(size)
   else:
      for angle in [0, 60, -120, 60]:
         turtle.left(angle)
         koch(size/3, n - 1)

def main():
   level = 5
   turtle.setup(1000, 1000)
   turtle.penup()
   turtle.pensize(1)
   turtle.goto(-400, 200)
   turtle.pendown()
   koch(800, level)
   turtle.right(120)
   koch(800, level)
   turtle.right(120)
   koch(800, level)
   
   turtle.hideturtle()
   turtle.done()

main()