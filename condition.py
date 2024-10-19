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

    