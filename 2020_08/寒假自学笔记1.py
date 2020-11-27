# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 18:31:09 2020

@author: wuguangkai211
"""
print()  # ...................................................................

counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter)  # print自带换行功能
print(miles)
print(name)

# int、float、bool、complex（复数）

print()  # ...................................................................

str1 = 'Runoob'

print(str1)               # 输出字符串
print(str1[0:-1])         # 输出第一个到倒数第二个的所有字符,左闭右开
print(str1[0])            # 输出字符串第一个字符
print(str1[2:5])          # 输出第三个到第四个字符
print(str1[2:])           # 输出从第三个开始的后的所有字符
print(str1 * 2)           # 输出字符串两次
print(str1 + "TEST")      # 字符串拼接
# 字符串的内容不可改变

# Python3 的六个标准数据类型中：
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个） ：List（列表）、Dictionary（字典）、Set（集合）。

print()  # ...................................................................

print(isinstance(str1, str))  # 判断变量的类型，isinstance承认继承关系，推荐使用isinstance
print(isinstance(str1, int))

print()  # ...................................................................

print(3 // 7)  # //  表示整除
print(3 / 7)   # /  表示精确除
print(7 / 3)
print(7 // 3)
print('     ', 7 // 3)

print()  # ...................................................................

list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素。输出的元素个数是: b - a
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表
