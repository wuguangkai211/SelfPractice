# 次方运算
num1 = 3 ** 4
num2 = 5 ** 7

print("3^4 =", num1)    
# 这里即使‘=’后面没有空格，Python也会为我们自动加上一个空格，使得输出更漂亮
print("5^7 =", num2)

print("3^4 = {0}, 5^7 = {1}".format(num1, num2))
print("3^4 = {}, 5^7 = {}".format(num1, num2))
print("3^4 = {a}, 5^7 = {b}".format(a=num1, b=num2))
