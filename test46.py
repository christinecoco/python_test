#求输入数字的平方，如果平方运算后小于 50 则退出
print('如果输入数字的平方小于50，程序则会退出')
while True:
        i=int(input('请输入一个数：'))
        sum=i*i
        if sum<50:
            print('%d的平方是%d'%(i,sum))
            break
        else:
            print('%d的平方是%d'%(i,sum))

