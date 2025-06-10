# ..create account class with 2 atributes balance and account no and create debit,credit methods and printing balance

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no =acc
        
    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("total balane:", self.get_balance())

     # credit method
    def credit(self,amount):
        self.balance +=amount
        print("Rs", amount, "was created")
        print("total balane:", self.get_balance())

    # return the final value
    def get_balance(self):
        return self.balance

acc1 = Account(10000,1345)
acc1.debit(1000)
acc1.credit(500)

# ..del keyword
# class Student:
#     def __init__(self,name):
#         self.name = name

# s1 = Student("binaya")
# print(s1.name)
# del(s1.name)
# print(s1.name)

# --create a circle class with radius r using constructor,define area()method to calculate area and define perimeter()method to calculate perimeter

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

