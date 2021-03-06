
height = input("How tall are you, in inches?")
height = int(height)                        # 这里使用 int() 完成强制转换：str -> int

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
