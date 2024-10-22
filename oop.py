class Student:
    # name = "John"
    def __init__(self, name, age, marks, subjects):
        self.name = name
        self.age = age
        self.marks = marks
        self.subjects = subjects

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    @staticmethod
    def hello():
        print("Hello")



# s2 = Student()
# print(s2.name)

s1 = Student("a", 20, 90, ["Math", "Science"])
print(s1.name)
print(s1.age)
print(s1.marks)
print(s1.subjects)
print(s1.get_name())
print(s1.get_age())
s1.hello()

s2 = Student("b", 21, 80, ["Math", "Science"])
print(s2.name, s2.age, s2.marks, s2.subjects)
del s2


class Car:
    def __init__(self):
        self.acc = False
        self.clutch = False
        self.brake = False

    def start(self):
        self.acc = True
        self.clutch = True
        self.brake = False
        print("Car started")

c1 = Car()
c1.start()

class TataCar(Car):
    def __init__(self,name):
        self.name = name
        super().__init__()

t1 = TataCar("Tata")
t1.start()


class Account:
    def __init__(self, acc, balance,password):
        self.acc = acc
        self.balance = balance
        self.__password = password

    def deposit(self, amount):
        self.balance += amount
        print("Deposited", amount)

    def withdraw(self, amount):
        self.balance -= amount
        print("Withdrawn", amount)

    def get_balance(self):
        return self.balance

a1 = Account("123", 1000,"PASS")
a1.deposit(100)
print(a1.get_balance())
a1.withdraw(50)
print(a1.get_balance())



class Person:
    name = "anonymous"

    @classmethod
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

p1 = Person("John")
p1.display()
print(Person.name)



class ComplexNum:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def showNum(self):
        print(f"{self.real} + {self.imag}i")

    # def add(self, c):
    #     return ComplexNum(self.real + c.real, self.imag + c.imag)

    def __add__(self, c):
        return ComplexNum(self.real + c.real, self.imag + c.imag)

    def __sub__(self, c):
        return ComplexNum(self.real - c.real, self.imag - c.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


c1 = ComplexNum(1, 2)
c1.showNum()
c2 = ComplexNum(3, 4)
c2.showNum()
c3 = c1 + c2
c3.showNum()
c4 = c1 - c2
c4.showNum()



class Employee:
    def __init__(self, dept,role, salary):
        self.dept = dept
        self.role = role
        self.salary = salary

    def showDetails(self):
        print(f"Role: {self.role}, Salary: {self.salary}, Dept: {self.dept}")

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineering", "HR", "23000")

e1 = Employee("HR", "Engineer", 100000)
e1.showDetails()

e2 = Engineer("John", 30)
e2.showDetails()