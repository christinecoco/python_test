#画图，学用rectangle画方形
import turtle
import time
rectangle=turtle.Pen()
rectangle.begin_fill()
for i in range(4):
    rectangle.forward(100)
    rectangle.left(360/4)
rectangle.end_fill()
time.sleep(5)