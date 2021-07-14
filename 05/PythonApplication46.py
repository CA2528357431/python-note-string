#文本对齐
poem=["xxx","yyyyy","zzzz"]


#居中对齐
for x in poem:
    print(x.center(10,","))
    
print("\n")
    #10使字符长为10     ,用“，”填充,  否则默认空格填充


#左对齐
for x in poem:
    print( x.ljust(10,","))
    
print("\n")
    #10使字符长为10     ,用“，”填充,  否则默认空格填充


#右对齐
for x in poem:
    print( x.rjust(10,","))

print("\n")
    #10使字符长为10     ,用“，”填充,  否则默认空格填充
