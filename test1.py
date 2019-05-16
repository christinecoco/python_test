#coding=utf-8
#b代表百位，s代表十位，g代表个位
for b in range(1,5):
    for s in range(1,5):
        for g in range(1,5):
            if b==s:
                continue
            elif b==g:
                continue
            elif s==g:
                continue
            print(b,s,g)


