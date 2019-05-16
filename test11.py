#计算每个月兔子数量
#coding=utf-8
month=None
while True:
    try:
        month=int(input('请输入你要查询的第几个月的兔子数量：'))
    except:
        print('输入有误，请重新输入')
    if type(month)==int:
        break
a,b=1,1
if month==1 or month==2:
    print('共有1只兔子')
else:
    for i in range(month-1):
        a,b=b,a+b
    print('第%d个月共有%d只兔子'%(month, a))