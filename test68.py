#有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
list=[]
num=int(input('你要输入几个整数：'))
for n in range(num):
    while True:
        try:
            i = int(input('请输入一个数字：'))
        except:
            print('输入有误，请重新输入')
        if type(i) == int:
            break
    list.append(i)
s=int(input('向后移多少个位置'))
list1=[]
list1=list[s:]
print(list1)
list2=[]
list2=list[0:s]
print('原始列表为：',list)
print('调整过后的列表为：',list1+list2)