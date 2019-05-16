#coding=utf-8
#判断输入的三个整数的大小，并从小到大排列
i=None
m=None
n=None
while True:
    try:
        i=int(input('请输入一个整数i:'))
    except:
        print('输入的不是整数，请重新输入')
    if type(i)==int:
        break
while True:
    try:
        m=int(input('请输入一个整数m:'))
    except:
        print('输入的不是整数，请重新输入')
    if type(m)==int:
        break
while True:
    try:
        n=int(input('请输入一个整数n:'))
    except:
        print('输入的不是整数，请重新输入')
    if type(n)==int:
        break
l=[i,m,n]
l.sort()
print('由小到大排序后的结果为',l)