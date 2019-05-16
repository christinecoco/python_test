#数字比较
def compare(a,b):
    if a-b>0:
        print('%d大于%d'%(a,b))
    elif a-b<0:
        print('%d大于%d'%(b,a))
    else:
        print('%d等于%d'%(a,b))
    return
if __name__=='__main__':
    compare(23,12)