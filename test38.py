#求矩阵中主对角线元素之和
list1=[]
list2=[]
list3=[]
for i in range(1,4):
    i=int(input('请输入第一行矩阵的3个元素：'))
    list1.append(i)
#print(list1)
for m in range(1,4):
    m=int(input('请输入第二行矩阵的3个元素：'))
    list2.append(m)
#print(list2)
for n in range(1,4):
    n=int(input('请输入第三行矩阵的3个元素：'))
    list3.append(n)
#print(list3)
sum1=list1[0]+list2[1]+list3[2]
sum2=list1[2]+list2[1]+list3[0]
print(sum1,sum2)
