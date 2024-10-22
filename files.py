import os

# open("demo.txt", "r")
# f = open("demo.txt", "r")
f = open("demo.txt", "a")
# print(f.read())
# print(type(f))

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

f.write("I am learning python")

f.close()

f = open("sample.txt", "w")
# f = open("sample.txt", "a")
f.write("This is sample writing")
f.close

os.remove("sample.txt")

# with open("practice.txt", "w") as f:
#     f.write("This is practice writing JAVA")
# with open("practice.txt", "w") as f:
#     data = f.read()

# new_data = data.replace("JAVA", "Python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)


count = 0   
with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    """
    num = ""
    for i in range(len(data)):
        if(data[i] ==","):
            print(num)
            num = ""
        else:
            num += data[i]
    """

    nums = data.split(",")
    print(nums)
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)