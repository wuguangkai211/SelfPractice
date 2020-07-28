while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:              # 使用 len() 获取字符串长度
        print('Too small')
        continue
    print('Input is of sufficient length')
    # 自此处起继续进行其它任何处理
