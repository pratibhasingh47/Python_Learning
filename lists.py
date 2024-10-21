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

fruits = ["apple", "banana", "cherry" , "orange", "kiwi", "mango"]

fruits.sort()
print(fruits)

movies = []
mov1 = input("Enter 1st movie: ")
mov2 = input("Enter 2nd movie: ")
mov3 = input("Enter 3rd movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

list1 = [1,2,3,2,1]
list2 = [1,2,3]
list3 = ['m', 'o', 'm']

copy_list1 = list1.copy()
copy_list1.reverse()

if list1 == copy_list1:
    print("Palindrome")
else:
    print("Not Palindrome")