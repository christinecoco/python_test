#根据学生的分数来判断属于哪个等级
a=None
while True:
    try:
        a=int(input('请输入分数：'))
    except:
        print('输入有误请重新输入')
    if type(a)==int:
        break
if a>=90:
    print('A')
elif a>=60 and a<=89:
    print('B')
else:
    print('C')