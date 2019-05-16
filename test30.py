#一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
i=None
while True:
    try:
        i=int(input('请输入一个数字：'))
    except:
        print('输入有误，请重新输入')
    if type(i)==int:
        break
x=str(i)
flag=True

for m in range(len(x)//2):
    if x[m]!=x[-m-1]:
        flag=False
        break
if flag:
    print('%d是一个回文数！'%i)
else:
    print('%d不是一个回文数！'%i)

# 第二种方法
i=None
while True:
    try:
        i=int(input('请输入一个5位的数字：'))
    except:
        print('输入有误，请重新输入')
    if type(i)==int:
        break
a=str(i)
if a[0]==a[-1] and a[1]==a[-2]:
    print('%d是回文数'%i)
else:
    print('%d不是回文数'%i)