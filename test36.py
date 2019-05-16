#求100之内的素数
for i in range(2,100):
    for n in range(2,i):
        if i%n==0:
            break
    else:
        print('%d是素数'%i)