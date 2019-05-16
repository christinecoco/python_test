#输入3个数abc,按照大小顺序输出
l=[]
while True:
    try:
        i=int(input('请输入一个数:'))
    except:
        print('输入有误，请重新输入')
    if type(i)==int:
        break
while True:
    try:
        j=int(input('请输入一个数:'))
    except:
        print('输入有误，请重新输入')
    if type(j)==int:
        break
while True:
    try:
        k=int(input('请输入一个数:'))
    except:
        print('输入有误，请重新输入')
    if type(k)==int:
        break
l.append(i)
l.append(j)
l.append(k)
l.sort()
print(l)