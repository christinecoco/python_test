#求猴子一共摘了多少桃子，每天都吃掉了总桃子数的一半加一个，第十天只剩下了一个桃子
day=10
x1=1
while day>1:
    x1=2*(x1+1)
    x2=x1
    day-=1

print(x2)