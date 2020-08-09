pcs = int(input())
for i in range(0, pcs):
    text = str(input())
    a, b = text.split(' ', 1)       # 简单运用 split 函数来实现格式化输入
    print(int(a) + int(b))          # 这里要使用强制转换
