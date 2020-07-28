
# 导入mymodule模块（他在本文件目录内）
import mymodule

# 调用模块方法
mymodule.say_hi()

# 内置的 `dir()` 函数能够返回由对象所定义的名称列表。
# 如果这一对象是一个模块，则该列表会包括函数内所定义的函数、类与变量。
print(dir(mymodule))

# 不使用参数。要注意到被导入的模块也会是这一列表的一部分。
print(dir())

print('Version', mymodule.__version__)
