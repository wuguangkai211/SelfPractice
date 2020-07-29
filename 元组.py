# 我会推荐你总是使用括号
# 来指明元组的开始与结束
# 尽管括号是一个可选选项。
# 明了胜过晦涩，显式优于隐式。
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

# 将老动物园的动物转移到新动物园里，而不改变其原本的身份
new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])

# 在这里要注意到元组中所包含的元组不会失去其所拥有的身份
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
      len(new_zoo) - 1 + len(new_zoo[2]))



""" 一个空的元组由一对圆括号构成，就像 `myempty = ()` 这样。
然而，一个只拥有一个项目的元组并不像这样简单。
你必须在第一个（也是唯一一个）项目的后面加上一个逗号来指定它，如此一来 Python 才可以识别出在这个表达式想表达的究竟是一个元组还是只是一个被括号所环绕的对象，也就是说，如果你想指定一个包含项目 `2` 的元组，你必须指定 `singleton = (2, )`。 """

""" 元组内置函数
Python元组包含了以下内置函数

序号	方法及描述	实例
1	len(tuple)
计算元组元素个数。	
>>> tuple1 = ('Google', 'Runoob', 'Taobao')
>>> len(tuple1)
3
>>> 
2	max(tuple)
返回元组中元素最大值。	
>>> tuple2 = ('5', '4', '8')
>>> max(tuple2)
'8'
>>> 
3	min(tuple)
返回元组中元素最小值。	
>>> tuple2 = ('5', '4', '8')
>>> min(tuple2)
'4'
>>> 
4	tuple(iterable)
将可迭代系列转换为元组。	
>>> list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
>>> tuple1=tuple(list1)
>>> tuple1
('Google', 'Taobao', 'Runoob', 'Baidu')

元组运算符
与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。

Python 表达式	结果	描述
len((1, 2, 3))	3	计算元素个数
(1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	连接
('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
3 in (1, 2, 3)	True	元素是否存在
for x in (1, 2, 3): print (x,)	1 2 3	迭代 """
