count = 1
# while loop
while count<=10:
    print("Hello",count)
    count+=1

i = 1
while i<=10:
    print("pratibha",i)
    i+=1

n = int(input("Enter the number: "))
i = 1
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1

num = [10,20,30,40,50]
i = 0
while i<len(num):
    print(num[i])
    i+=1


# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 49
# i = 0
# while i<len(nums):
#     if nums[i]==x:
#         print("Element found at index",i)
#         break
#     else:
#         print("Element not found")
#     i+=1


#For LOOPs

list1 = [10,20,30,40,50]
for i in list1:
    print(i)

str1 = "Pratibha"
for char in str1:
    print(char)
else:
    print("No items left")


for i in range(1,11):
    print(i)


n = 5
fact = 1
for i in range(1,n+1):
    fact = fact*i

print("Factorial of",n,"is",fact)