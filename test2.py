#coding=utf-8
#当用户输入当月利润时给出应发放的奖金总数
i=None
while True:
    try:
        i = float(input('请输入当月利润(元)：'))
    except Exception as e:
        print('输入的不是数字，请重新输入')
    if type(i)==float:
         break
if i <=100000:
    bonus=i*0.01
elif i>100000 and i<200000:
    bonus=100000*0.1+(i-100000)*0.075
elif i > 200000 and i < 400000:
    bonus = 100000 * 0.1 +100000*0.075+ (i - 200000) * 0.05
elif i>400000 and i<600000:
    bonus=100000*0.1+100000*0.075+200000*0.05+(i-400000)*0.03
elif i>600000 and i<1000000:
    bonus=100000*0.1+100000*0.075+200000*0.05+200000*0.03+(i-600000)*0.015
elif i>1000000:
    bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000* 0.015+(i-1000000)*0.01
print('应发放的奖金总数为：',bonus)