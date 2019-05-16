#计算阶乘相加
s1=1
s=[]
for i in range(1,21):
    s1=s1*i
    s.append(s1)
s4=sum(s)
print(s4)