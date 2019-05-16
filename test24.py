#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
#coding=utf-8
a=1
b=2
s=[]
for i in range(1,21):
    s1=a+b
    sum1=s1/b
    s.append(sum1)
c=sum(s)
print(float(s1+c))
#第二种解决方案
a=1
b=2
s=[]
for j in range(1,21):
    a,b=b,a+b
    s1=b/a
    s.append(s1)

d=sum(s)
print(d)