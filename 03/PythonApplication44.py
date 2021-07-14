# 字符串 查找替换

a="whvoiwrlobkywhvoi"
print(a.startswith("whvoi"))
#以xxx开始

print(a.endswith("whvoi"))
#以xxx结束

print(a.find("o"))
print(a.find("p"))
#存在输出位置，否则输出-1

print(a.rfind("o"))
#从右侧找

print(a.replace("whv","123"))
print(a)
#替换    只在当句有效  应用新字母接受



