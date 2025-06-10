# i = 1
# while i < 6:
#   print(i)
#   i += 1

#   count = 5
#   while count <=5:
#     print("hello")
#     count +=1
#     print(count)

#1 print numbers from 1 to 5
# i = 1
# while i <=5:
#     print(i)
#     i +=1

#     print("loop ended")
# #2 5 to 1
# b=5
# while b >=1:
#     print(b)
#     b -=1

#3 # print numbers from 1 to hundred
# i=1
# while i<=100:
#     print(i)
#     i +=1

#4 # print numbers from 100 t0 1
# a=100
# while a>=1:
#     print(a)
#     a -=1

#5 # print the multiplication table of a number n
# n= int(input("enter the number:"))
# i=1
# while i <=10:
#     print(n*i)
#     i +=1

#.....print the elements of the following list using loop
# [1,4,9,16,25,36,49,64,81,100]
# num = [1,4,9,16,25,36,49,64,81,100]

# idx=0
# while idx<len(num):
#     print(num[idx])
#     idx +=1

# .....Finding numbers
# num = [1,4,9,16,25,36,49,64,81,100]

# x=36
# i = 0
# while i<len(num):
#    if(num[i] == 36):
#       print("founs at idx,",i)
#       break
#    else:
#       print("finfing..")
#       i +=1
    

# 7. break and continue
# i = 1
# while i<=5:
#     print(i)
#     if(i==3):
#       break
#     i +=1

#     print("end of loop")

# i=1
# while i<=5:
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i +=1


i = 1
while i<=10:
    if(i%2 !=0):
        i+=1
        continue
    print(i)
    i+=1