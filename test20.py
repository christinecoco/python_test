#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
#coding=utf-8
times=10
l=[]
height=100
while times>0:
    height/=2
    l.append(height)
    times -= 1
print(l)
print('第10次反弹的高度：',l[9])
print('一共经过',100+(sum(l)*2),'米')