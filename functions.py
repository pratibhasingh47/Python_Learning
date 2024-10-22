a = 5
b = 10

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def power(a,b):
    return a**b

def floordiv(a,b):
    return a//b

print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))
print(mod(a,b))
print(power(a,b))

def greet():
    print("Hello")

output = greet()
print(output)


def calc_prod(a = 5,b = 10):
    return a*b

print(calc_prod())
print(calc_prod(10))
print(calc_prod(10,20))


cities = ["delhi","mumbai","pune","bangalore"]
def print_len(cities):
    print(len(cities))

print_len(cities)

heroes = ["batman","superman","captain america","ironman"]

def print_heroes(heroes):
    for hero in heroes:
        print(hero , end=" ")

print_heroes(heroes)
print_heroes(cities)

def cal_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    print("Factorial of",n,"is",fact)
    return fact

cal_factorial(7)

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(5)


def fact(n):
    if(n ==0 or n ==1):
        return 1
    else:
        return n*fact(n-1)

print(fact(5))
print(fact(6))


n = int(input("Enter the number: "))
def cal_sum(n):
    if n == 0:
        return 0
    return n+cal_sum(n-1)

print(cal_sum(n))

list = ['a','b','c','d','e']

def print_list(list , idx=0):
    if(idx == len(list)):
        return
    print(list[idx], end=" ")
    print_list(list,idx+1)

print_list(list)