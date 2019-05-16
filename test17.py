#判断用户输入的字符串中英文字符、标点符号、数字等个数
import string
number=0
alphabet=0
space=0
others=0
str=None
# while True:
#     try:
str=input('请输入一个字符串：')
    # except:
    #     print('输入有误，请重新输入')
    # if type(str)==string:
    #     break
for i in str:
    if i.isdigit():
        number+=1
    elif i.isalpha():
        alphabet+=1
    elif i.isspace():
        space+=1
    else:
        others+=1
print('字符串中英文字母共%d个，数字共%d个，空格共%d个，其他字符共%d个'%(alphabet ,number ,space ,others))