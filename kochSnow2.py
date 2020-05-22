# 科赫曲线
# 四分线段模式
import turtle

def koch(length, n):#递归函数，画科赫曲线，四分段
   if(n == 0):
      turtle.fd(length)
   else:
      for angle in [0, 90,270, 270, 90]:
         turtle.left(angle)
         koch(length / 4, n - 1)



def main():
   level = 2
   turtle.setup(1000, 1000)
   turtle.pensize(1)
   turtle.penup()
   turtle.goto(-400, 300)
   turtle.pendown()
   koch(800, level)
   turtle.right(90)
   koch(800, level)
   turtle.right(90)
   koch(800, level)
   turtle.right(90)
   koch(800, level)



   turtle.hideturtle()
   turtle.done()

if __name__ == '__main__':
   main()