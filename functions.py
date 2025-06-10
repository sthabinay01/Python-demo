# def sum(a,b): #passing parameter
#  s= a+b
#  return s

# print(sum(5,6))  #arguments
# print(sum(9,6))
# print(sum(20,6))

# ..arguments
# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# # ,..avaerage of 3 numbers
# def calc_avg(a,b,c):
#   sum = a+b+c
#   avg = sum/3
#   print(avg)
#   return avg

# calc_avg(10,20,30)

# ..default parameter
# def cal_pro(a=3,b=3):
#   print(a*b)
#   return(a*b)

# cal_pro()

# ..program to print the length of a alist
# nums = [1,2,3,4,5,6,7,8,9]
# heros=["thor","iron","batman"]
# def prt_len(list):
#   print(len(list))

#   prt_len(nums)
#   prt_len(heros)


# ..program to print the elements of a list in a single line
# numds = [1,2,3,4,5,6,7,8,9]
# heros=["thor","iron","batman"]

# print(heros[0],end="\n")
# def prt_len(list):
#   print(len(list))

# def print_list(list):
#   for item in list:
#     print(item,end="")

# ..program to find the factoral of n


def cal_fact(n):
  fact = 1
  for i in range(1,n+1):
    fact *= i
  print(fact)


cal_fact(5)

# ..program to convert usd to inr
def converter(usd_val):
  inr_value = usd_val * 113
  print(usd_val,"usd=",inr_value,"INR")

converter(16)

# ..passinhg list as argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# .. sheck odd even
def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
result = check_odd_even(num)
print("The number is {result}.")
