#String objects
name = "osor"

print(name.upper())
print(name.lower())
print(name.capitalize())

#List object
numbers = [1, 2, 3,]

numbers.append(4)
numbers.remove(2)

#Dictinary objects
student = {
    "name": "osor",
    "age": 19
}
print(student.keys())
print(student.values())
print(student.get("name"))

#Tuple objects
items = (10, 20, 30)

print(items.count(10))
print(items.index(20))

#Set object
fruits = {"apple", "banana"}
fruits.add("orange")
fruits.remove("banana")

print(fruits)
print(fruits)