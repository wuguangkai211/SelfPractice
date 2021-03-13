class Dog:
    """ 小狗类 """

    def __init__(self, name, age):
        """ 初始化属性 name 和 age """
        self.name = name
        self.age = age
    # end

    def sit(self):
        """ 模拟小狗蹲下 """
        print(f"{self.name} is now sitting.")
    # end

    def roll_over(self):
        """ 模拟小狗打滚 """
        print(f"{self.name} rolled over!")
    # end
# end



my_dog = Dog("Pengpeng", 5)
my_dog.roll_over()
my_dog.sit()

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
