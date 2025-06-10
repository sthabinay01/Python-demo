# for loops
list=[1,2,3,4,5,6]
for value in list:
    print(value)

tup=(2,4,6,8,10)
for num in tup:
  print(num)

  str = "binaya"
  for char in str:
     print(char)

# for loop with else
str = "shrestha"
for char in str:
   if(char =='e'):
        print("e found")
        break
   print(char)
else:
   print("end")

# ..print the elements of the following list using tupults
# [1,4,9,16,25,36,49,64,81,100]
list=[1,4,9,16,25,36,49,64,81,100]

for num in list:
   print(num)

# ..seaarch for a number x in this using loop
# [1,4,9,16,25,36,49,64,81,100]
nums = (1,4,9,16,25,36,49,64,81,100,49)
x=4

idx=0
for el in nums:
   if(el == x):
     print("number found ar idx:", idx)
     idx += 1 