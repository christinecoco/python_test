#练习函数调用
#比较三个数的大小
def compare(a,b,c):
    if a>b>c:
        print("%d>%d>%d"%(a,b,c))
    elif a>b and b<c and a>c:
        print("%d>%d>%d"%(a,c,b))
    elif a>b and b<c and a<c:
        print("%d>%d>%d"%(c,a,b))
    elif a>b and b==c:
        print("%d>%d=%d"%(a,b,c))
    elif a<b<c:
        print("%d>%d>%d"%(c,b,a))
    elif a==b and b<c:
        print("%d>%d=%d"%(c,a,b))
    elif a<b and b>c and a<c:
        print("%d>%d>%d"%(b,c,a))
    elif a<b and b>c and a>c:
        print("%d>%d>%d"%(b,a,c))
    elif a<b and a==c:
        print("%d>%d=%d"%(b,a,c))
    elif a<b and b==c:
        print("%d=%d>%d"%(b,c,a))
    else:
        print("%d=%d=%d"%(a,b,c))
    return a,b,c
compare(2,8,1)
def hello():
    print('hello world')
def three_hello():
     for i in range(3):
         hello()
if __name__=='__main__':
    three_hello()
