# coding=utf-8

def test(name):
    def test_in():      # 函数嵌套
        print(name)     # 内部函数使用外部函数的变量
        return None
    return test_in      # 外部函数的返回值为内部函数（也是对象）
# end

func = test("函数的闭包")
func()                  # 调用函数

# 函数也是对象，也可以当做对象传递
""" 
闭包的概念:
1）函数嵌套
2）内部函数使用外部函数的变量
3）外部函数的返回值为内部函数
"""
