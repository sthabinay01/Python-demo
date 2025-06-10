# age = 10
# if(age>=18):
#     print("u r  edigible to vote and apply for liscenc")

# elif(age<=18):
#     print("u cannot vote")

# ....grade students

# marks = int(input("enter your marks:"))
# print(marks)

# if(marks >=90):
#     grade="a"
# elif(marks >=80 and marks<90):
#     grade="b"
# elif(marks >=70 and marks <80):
#     grade="c"
# else:
#     grade="d"
# print("the grade of the student:",grade)

# ...program to find the greatest of 3 numbers entered by the users
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))

if(a>=b and a>=c):
    print("first number is largest:", a)

elif(b>=c):
    print("second number is largest")

else:
    print("third number is greatesdt", c)

# program to check if a number is a mulriple of 7 or mot
num = int(input("enter the number:"))

if(num % 7 ==0):
    print("multiple of 7")
else:
    print("not a multiple")
    