#coding=utf-8
for i in range(100,1000):
    b=i//100
    s=i//10%10
    g=i%10
    if i==b**3+s**3+g**3:
        print (i)