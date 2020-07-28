while True :
    try :
        x = int(input())
        y = int(input())    # 一行一个整数
        print(x+y)
    
    except :
        break


# input通过识别异常来中断

""" while True :
    try :
        s = input()
        l = s.split()
        # 一行两个整数，中间用空格隔开
        print(int(l[0])+int(l[1]))
    
    except :
        break """