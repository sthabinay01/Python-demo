# class is a blueprint for creating objects
class student: #creating class
    name ="binaya"

#creating object
s1 = student()
print(s1.name)

class car:
    color = "blue"
    model = "bmw"

c1 = car()
print(c1.color)
print(c1.model)

# ..constructor (_init_)
class student: #creating class
#   name ="binaya"

# parameterized constructor
 def __init__(self,fullname):
      self.name = fullname
      print("adding student")

#creating object
s1 = student("karan")
print(s1.name)

# ..Methods
# class student:

# # parameterized constructor
#  def __init__(self,name,marks):
#       self.name = name
#       self.marks = marks
      
#       def asd(self):
#          print("welcome student:",self.name)
 
# def marks(self):
#    return self.marks

# #creating object
# s1 = student("karan",36)
# s1.asd()
# print(s1.marks())

# ..abstraction 
class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("car has starated")

car1 = car()
car1.start()