#利用递归方法求5!
#递归公式：fn=fn-1*4
def fib(n):
    if n==0:
        sum=1
    else:
        sum=n*fib(n-1)
    return sum
print(fib(9))