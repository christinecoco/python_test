#给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
i=input('input a number:')
l=[]
l.extend(i)
print(len(l))
l.reverse()
print(''.join(l))