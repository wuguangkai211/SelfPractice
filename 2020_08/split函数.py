# 这个函数可以实现简单的格式化输入

str = "this is string example....wow!!!"
print (str.split())        # 以空格为分隔符
print (str.split('i',1))   # 以 i 为分隔符
print (str.split('w'))     # 以 w 为分隔符

print("-------------------------------------------------")

txt = "Google#Runoob#Taobao#Facebook"
# 第二个参数为 1，返回两个参数列表
x = txt.split("#", 1)
print(x)


""" 描述
split() 通过指定分隔符对字符串进行切片，如果第二个参数 num 有指定值，则分割为 num+1 个子字符串。(即有 num 个分割点)

语法
split() 方法语法：

str.split(str="", num=string.count(str))
参数
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num -- 分割次数。默认为 -1, 即分隔所有。
返回值
返回分割后的字符串列表(List)。"""
