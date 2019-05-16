#有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
list=[1,23,34,45,67,89,98]
while True:
    try:
        i=int(input('enter a number:'))
    except:
        print('input error,try again')
    if type(i)==int:
        break
list.append(i)
list.sort()
print('插入数字后的列表为：',list)