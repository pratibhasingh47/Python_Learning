marks = [90, 80, 70, 60]
grades = ["A", "B", "C", "D"]
print(marks)
print(grades)
print(type(marks))
print(type(grades))
print(marks[0])
print(grades[0])
print(len(marks))
print(len(grades))

students = ["John", "Doe", 25, 90.5]
print(students)
print(students[0])
print(students[1])
print(students[2])
print(students[3])
students[0] = "Jane"

print(students)

print(students)

print(students[1:3])
print(students[1:])
print(students[:3])

students.append("Smith")
students.insert(2, "Doe")
print(students)
students.remove("Doe")
students.pop()
print(students)


list1 = [1, 4, 3,10,81,3, 7, 8, 9, 10]
print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
# print(list1.sort()) #None


