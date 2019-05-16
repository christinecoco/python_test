#将列表中的值以相反的顺序输出
list=[1,2,3,4,5,'python','test']
list.reverse()
print(list)
print(','.join(str(n)for n in list))#按照xx分割列表，以都好来分隔列表join后的元素须是可迭代的