# coding=utf-8
# 分解质因数，输出用户要求解的质因数的结果
# x = int(input("是否进入循环？是：1， 否：0\n"))
# while(x):
#     n = int(input("请输入一个正整数："))
#     print ("%d = " %n , end = '')
#     while n not in [1]:
#         for i in range(2, n+1):
#             if n % i == 0:
#                 n = int(n/i)
#                 if n == 1:
#                     print("%d " %i , end = '')
#                 else:
#                     print("%d * " %i , end = '')
#                 break
#     print()
#     x = int(input("是否进入循环？是：1， 否：0\n"))


i=None
m=None
num=None
while True:
    try:
        num=int(input('请输入一个正整数:'))
    except:
        print('输入的不是整数，请重新输入')
    if type(num)==int and num>1:
        break
    else:
        print('输入有误，请重新输入')
    for i in range(2,num+1):
        for n in range(2,i+1):
            if n%i==0:
                break
