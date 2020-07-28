


print("---------------!游戏开始!-----------------")

guess = int(input("猜猜我心里想的是哪个数字？"))        #输入一个整数
cnt   = 0

while 1:
    #Python里没有++和--，因为整形数字不可改变。赋值操作实际上是分配新内存并命名而已
    cnt += 1  
    if cnt > 3:
        print("机会已经用完！ヾ(￣▽￣)Bye~Bye~")
        break
    elif guess == 8:
        print("OMG, you are right!")
        print("没有奖励哦！Bye~ /滑稽")
        break
    else:
        if guess < 8:
            print("哎呀，小了！重新猜一次吧：")
            guess = int(input())
        else:
            print("哎呀，大了！重新猜一次吧：")
            guess = int(input())

print("---------------!游戏结束!-----------------")
