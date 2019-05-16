#coding=utf-8
for i in range(101,200):
    for m in range(2,i):
        if i%m==0:
            break
    else:
        print(i,'是素数')
