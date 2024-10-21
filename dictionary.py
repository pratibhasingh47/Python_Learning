info ={
    "name": "dictionary",
    "marks": 10,
    "bool": True,
    "description": "A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.",
    "methods": ["clear()", "copy()", "fromkeys()", "get()", "items()", "keys()", "pop()", "popitem()", "setdefault()", "update()", "values()"]
}

print(info)
print(type(info))
print(info["name"])
print(info["marks"])
print(info["bool"])

info["surname"] = "Python"
print(info)


null_dict = {}
print(null_dict)

students = {
    "name": "John",
    "age": 25,
    "marks": 90.5,
    "subjects": {"Maths", "Science", "English"}
}

print(students)
print(students["name"])
print(students["age"])
print(students["marks"])
print(students["subjects"])
print(students.keys())

print(students.values())
print(students.items())
print(students.get("name"))
print(info.get("surname"))
print(students.get("surname", "Not found"))



marks = {}
x = int(input("Enter marks of Physics"))
marks.update({"Physics": x})

y = int(input("Enter marks of Chemistry"))
marks.update({"Chemistry": y})

z = int(input("Enter marks of Maths"))
marks.update({"Maths": z})

print(marks)

values = {
    ("float",9.0),
    ("int",9)
}
print(values)