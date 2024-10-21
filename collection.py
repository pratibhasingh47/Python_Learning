collection = {1,2,2,"hello", "world", "hello", 1}
print(collection)
print(type(collection))
print(len(collection))
collection.add(3)
print(collection)
collection.remove(2)
print(collection)
collection.discard(2)
print(collection)
collection.clear()
print(collection)

col1 = {}
print(type(col1))

col2 = set()
print(type(col2))


set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1.union(set2))
print(set1.intersection(set2))