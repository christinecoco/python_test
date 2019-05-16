#将两个变量值互换
a=10
b=20
c=a
d=b
print('a=',d)
print('b=',c)
#第二种方法使用函数
def exchange(a,b):
    print('交换前：a=%d,b=%d' % (a, b))
    a,b=b,a
    print('交换后：a=%d,b=%d'%(a,b))
    return a,b
exchange(10,20)