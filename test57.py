#画图，学用line画直线
import turtle
import time
draw=turtle.Pen()
draw.color(0.3,0.8,0.6)
draw.begin_fill()
for i in range(5):#range内的数字是几就是几边形，为1是直线
    draw.forward(100)
    draw.left(360/5)
draw.end_fill()
time.sleep(5)