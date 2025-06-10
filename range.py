seq = range(10) #range(stop)
for i in seq:
    print(i)

seq = range(2,10) #range(start,stop)
for i in seq:
    print(i)

seq = range(2,10,2) #range(start,stop,step)
for i in seq:
    print(i)

# print even numbers from 1 to 10
for i in range(2,100,2):
   print(i) 

# ..print numbers from 100 to 1
for i in range(100,0,-1):
    print(i)
# .. print multiplication table oa a number 
n = int(input("entee the number:"))

for i in range(1,11):
    print(n*i)

# ..pass statement
for i in range(5):
    pass
print("asjfsjflkjs")

# ..program to find the sum of first n numbers(using while)
n = int(input("enter the number:"))
sum = 0
i=1
while i<=n:
    sum +=i
    i +=1
# for i in range(1,n+1):
#     sum +=i
print("total sum=",sum)

# ..program to find the factorial of first n numbers(using for)
n=5
fact =1
i=1
while i<=n:
    fact *= i
    i+=1

print("factorial:",fact)