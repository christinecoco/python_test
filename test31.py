#请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母
#周一monday,周二 Tuesday，周三wednesday，周四Thursday，周五friday，周六saturday，周日sunday
while True:
    date=input('请输入首字母：')
    if date=='m':
        print('Monday')
    elif date=='t':
        date1=input('请输入第二个字母：')
        if date1=='u':
            print('Tuesday')
        elif date1=='h':
            print('Thursday')
        else:
            print('输入有误，无相应日期')
    elif date=='w':
        print('Wednesday')
    elif date=='f':
        print('Friday')
    elif date=='s':
        date2=input('请输入第二个字母：')
        if date2=='a':
            print('Saturday')
        elif date2=='u':
            print('Sunday')
        else:
            print('输入有误，无相应日期')
    else:
        print('输入有误，无响应日期')