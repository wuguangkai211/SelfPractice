# coding=utf-8
# My Address Book

class Person:
    """ 这是一个·人·类 """

    def __init__(self, name = '(Empty)', address = '(Empty)', reship = '(Empty)', email = '(Empty)', tel = '(Empty)'):
        """ 初始化函数，包含一个人的姓名等信息（共计5个） """
        self.name    = str(name)                           # 姓名
        self.address = str(address)                        # 住址
        self.reship  = str(reship)                         # 关系
        self.email   = str(email)                          # 电子邮箱地址
        self.tel     = str(tel)                            # 电话号码
    # end
# end

class Adbook:
    """ 这是一个·地址簿·类 """

    def __init__(self):
        """ 初始化函数 """
        self.now = 0                          # 此地址簿现有人数
    # end

    def addPerson(self):
        print("Please follow my guidence to finish this task (end each one with 'Enter'): ")
        name    = str(input("Name: "))                         
        address = str(input("Address: "))
        reship  = str(input("Relationship: "))
        email   = str(input("E-mail: "))
        tel     = str(input("Telephone number: "))

        # 附加此地址簿所拥有的实体人对象（空白）
        self.__dict__[f"Person {self.now+1}"] = Person(name, address, reship, email, tel)       
        self.now += 1                        # 此地址簿人数增加：1  
        print("Added successfully!")                
    # end
        


myadbook = Adbook()         # 创建一个新的地址簿对象

for i in range(2):
    myadbook.addPerson()
    print("Now we have {0} people.".format(myadbook.now))
    print(myadbook.__dict__[f"Person {i+1}"].name)
