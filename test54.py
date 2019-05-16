#取一个整数a从右端开始的4〜7位
a=1234567890435346456
if __name__=='__main__':
    a=int(input('input a number:\n'))
    b=a>>4
    c=~(~0<<4)
    d=b&c
    print('%o\t%o'%(a,d))