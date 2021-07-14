# 字符串 判断

a="     "
print(a)
print(a.isspace())
#是否全是空格

b="123asd123"
print(b)
print(b.isalnum())
#是否全是字母与数字

c="asdfnjij"
print(c)
print(c.isalpha())
#是否全是字母

d="1246123"
print(d)
print(d.isdecimal())
#是否全是数字，小数不可

e="123①\u00b2"
print(e)
print(e.isdigit())
#是否全是 数字 和 特殊不可通过键盘直接输入的字符（Unicode）

f="一万零一兆亿123①\u00b2"
print(f)
print(f.isnumeric())
#是否全是 中文数字 数字 和 特殊不可通过键盘直接输入的字符（Unicode）

g="Homeward Bound"
print(g)
print(e.istitle())
#是否全首字母大写

h="HOMEWARD BOUND 123"
print(h)
print(h.isupper())
#是否全字母大写,()可有其他字符

i="homeward bound 123"
print(i)
print(i.islower())
#是否全字母小写,()可有其他字符