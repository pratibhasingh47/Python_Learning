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
with open("practice.txt", "w") as f:
    data = f.read()

new_data = data.replace("JAVA", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)