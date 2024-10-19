# """
age = int(input("Enter your age : "))

if age >= 18:
    print("You are eligible to vote")
elif age >= 0 and age < 18:
    print("You are underage")
else:
    print("Invalid age")


light = input("Enter the color of the light: ")

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Wait")
elif light == "green":
    print("Go")
else:
    print("Invalid color")


marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80 and marks < 90:
    print("Grade B")
elif marks >= 70 and marks < 80:
    print("Grade C")
elif marks >= 60 and marks < 70:
    print("Grade D")
else:
    print("Grade F . You have failed")

    # """


food = input("Enter the food item: ")
eat = "Yes" if food == "Pizza" else "No"
print(eat)


sal = float(input("Enter your salary: "))
tax = sal*(0.1,0.2) [sal >= 50000]
print(tax)


#Best Practice
#Single instructions
#one instruction per task
#short & meaningful names
#use appropriate comments
#avoid complex expressions

p = float(input("Enter the principal amount: "))
t = float(input("Enter the time: "))
r = float(input("Enter the rate: "))
si = p*t*r/100
print("Simple Interest is", si)

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
if a > b and a > c:
    print("A is the greatest number")
elif b > a and b > c:
    print("B is the greatest number")
else:
    print("C is the greatest number")

