from turtle import ycor


class Car:
    """ 模拟汽车 """
    
    def __init__(self, make, model, year):
        """ 初始化描述汽车的属性 """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ 返回整洁的描述性信息 """
        long_time = f"{self.year} {self.make} {self.model}"
        return long_time.title()
    
    def read_odometer(self):
        """ 打印汽车历程信息 """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """ 修改里程表的数值（禁止回调） """
        if mileage >= self.odometer_reading:        # 检测欲修改数值是否合法
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles=1):
        """ 将里程数增加指定的量 """
        self.odometer_reading += miles
# end



my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 1114
my_new_car.read_odometer()

my_new_car.update_odometer(1115)
my_new_car.read_odometer()

my_new_car.increment_odometer()
my_new_car.read_odometer()
