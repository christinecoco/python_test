#coding=utf-8
#判断这一天是一年中的第几天
y=None
m=None
d=None
l=None
while True:
    try:
        y=int(input('year:'))
    except:
        print('input error,try again ')
    if type(y)==int:
        break
while True:
    try:
        m=int(input('month:'))
    except:
        print('input error,try again ')
    if type(m)==int:
        break
while True:
    try:
        d=int(input('day:'))
    except:
        print('input error,try again ')
    if type(d)==int:
        break
if m==0 or m==1:
    s =d
else :
    s=m*30+d
if y%400==0 or y%4==0 and y%100!=0:
    l=1
if l==1 and m>2:
    s+=1
print('it is the %dth day'%s)
