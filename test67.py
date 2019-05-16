#输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组
l=[]
for n in range(6):
    while True:
        try:
            i = int(input('请输入一个数字：'))
        except:
            print('输入有误，请重新输入')
        if type(i) == int:
            break
    l.append(i)
if l[0]==max(l) and l[-1]==min(l):
    print(l)
else:
    c=l[0]
    d=max(l)
    a = l[-1]
    b = min(l)
    l[0]=d
    max(l)==c
    l[-1]=b
    min(l) == a
    print(l)