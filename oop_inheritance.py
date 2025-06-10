class Car:
    @staticmethod
    def star():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("fortune")
car2 = ToyotaCar("pirus")

print(car1.star())

# ..multilevel inheritance
class Cars:
    @staticmethod
    def star():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

class Fortune(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortune("diesel")
car2 = ToyotaCar("pirus")

print(car1.star())


# proprerty decorator
class student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem= chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
    
stu1 = student(98,99,96)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)