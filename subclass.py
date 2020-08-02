# coding=UTF-8

class SchoolMember:
    '''代表任何学校里的成员'''
    def __init__(self, name, age):
        self.__name__ = name
        self.__age__  = age
        print('(Initialized SchoolMember: {})'.format(self.__name__))

    def tell(self):
        '''告诉我有关我的细节'''
        print('Name:"{}" Age:"{}"'.format(self.__name__, self.__age__), end = " ")


class Teacher(SchoolMember):
    '''代表一位老师'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.__salary__ = salary
        print('(Initialized Teacher: {})'.format(self.__name__))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.__salary__))


class Student(SchoolMember):
    '''代表一位学生'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.__marks__ = marks
        print('(Initialized Student: {})'.format(self.__name__))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.__marks__))





t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

# 打印一行空白行
print()

members = [t, s]
for member in members:
    # 对全体师生工作
    member.tell()
