#coding=utf-8
#输出九九乘法口诀
for i in range(1,10):
    for m in range(1,i+1):
        s=i*m
        print(i,' *',m ,'=', s,end=' , ')
    print()