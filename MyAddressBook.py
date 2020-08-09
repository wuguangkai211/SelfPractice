# coding=utf-8
# My Address Book

class Person:
    """ 这是一个·人·类 """

    def __init__(self, name = '(Empty)', address = '(Empty)', reship = '(Empty)', email = '(Empty)', tel = '(Empty)'):
        """ 初始化函数，包含一个人的姓名等信息（共计5个） """
        self.__name    = str(name)                           # 姓名
        self.__address = str(address)                        # 住址
        self.__reship  = str(reship)                         # 关系
        self.__email   = str(email)                          # 电子邮箱地址
        self.__tel     = str(tel)                            # 电话号码

    def getName(self):
        """ 获取此人的姓名 """
        return self.__name

    def getAddress(self):
        """ 获取此人的住址 """
        return self.__address

    def getRelationship(self):
        """ 获取与此人的关系 """
        return self.__reship

    def getEmail(self):
        """ 获取此人的电子邮箱地址 """
        return self.__email

    def getTel(self):
        """ 获取此人的电话号码 """
        return self.__tel
    # end
# end

class Adbook:
    """ 这是一个·地址簿·类 """

    def __init__(self):
        """ 初始化函数 """
        self.__now = 0                          # ·此·地址簿现有人数

    def addPerson(self):
        print("Please follow my guidence to finish this task (end each one with 'Enter'): ")
        name    = str(input("Name: "))                         
        address = str(input("Address: "))
        reship  = str(input("Relationship: "))
        email   = str(input("E-mail: "))
        tel     = str(input("Telephone number: "))

        # 附加此地址簿所拥有的实体人对象（空白）
        self.__dict__[f"Person {self.__now+1}"] = Person(name, address, reship, email, tel)       
        self.__now += 1                        # 此地址簿人数增加：1  
        print("Added successfully!")     
    
    def getSum(self):
        """ 获取此地址簿现存人数 """
        return self.__now           
    # end
        


myadbook = Adbook()         # 创建一个新的地址簿对象

for i in range(2):
    myadbook.addPerson()
    print("Now we have {0} people.".format(myadbook.getSum()))
    print(myadbook.__dict__[f"Person {i+1}"].getName())
