#计算数字n项相加的和
from functools import reduce

a=None
n=None
while True:
    try:
        a=int(input('请输入你要求和的数字：'))
    except:
        print('输入有误，请重新输入')
    if type(a)==int:
        break
while True:
    try:
        n=int(input('请输入你要求和的项：'))
    except:
        print('输入有误，请重新输入')
    if type(n)==int:
        break
s=0
list=[]
for count in range (1,n+1):
    #a1=a*count
    s=s+a
    a=a*10
    list.append(s)
    print(s)
list=reduce(lambda x,y:x+y,list)
print('总和为：',list)