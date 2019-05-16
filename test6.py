#coding=utf-8
import random
#根据用户制定个数输出斐波那契数列
n=None
def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return a
while True:
    try:
        n=int(input('请输入你要查询的第几个斐波那契数列:'))
    except:
        print('输入不是整数，请重新输入')
    if type(n)==int:
        break
print('你要查询的斐波那契数列为：',fib(n))