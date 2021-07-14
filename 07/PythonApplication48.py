#字符串 拆分与连接

a="for my dear pretty  previous russia"
print(a.partition("pre"))
#从左找 字符，将元字符分为 字符左、字符、字符右
#是元组

a="for my dear pretty  previous russia"
print(a.rpartition("pre"))
#从右找 字符，将元字符分为 字符左、字符、字符右
#是元组

a="for my dear pretty  previous russia"
print(a.split("pre"))
print(a.split())
#从找全部字符，将元字符中的 字符 删除，以删除后的空格分开
#不指定字符默认为空格
#是元组

word=a.split()
new="，，，，".join(word)  #用xx作为分割连接 元组
print (new)