#字符串去除空格

poem=["        noble  faithful      ","    goog day   "]
for x in poem:
    print("%s" % x.strip().center(30,","))
for x in poem:
    print("%s" % x.lstrip().center(30,","))
for x in poem:
    print("%s" % x.rstrip().center(30,","))



'''
print(a.lstrip())  #  删除左边空格
print(a.rstrip())  #  删除右边空格
print(a.strip())   #  删除左右边空格
'''