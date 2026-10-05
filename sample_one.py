# comment
print("hello, world!")
# variables
name = "alice"
age = 25
price = 19.9
is_active = True
# Input
name = input("Enter yoour name")
# if/eilf/else
if age >= 18:
    print ("Adult")
elif age >== 13:
    print ("Teenager")
else:
    print("Child")
# For loop 
for i in range(5):
    print(i)
# While loop
count = 0
while count <5:
    print(count)
    count +=1
#Function
def add(a,b):
    return a + b
result = add(5,3)
#list
fruits = ["apple", "banana", "orange"]
fruits.append("mango")
# Dictionary
person ={
    "name": "Alice"
    "age": 25
}
print(person["name"])
# Class
class person:
    def __init__(self, name):
        self .name = name
    def greet(self):
        print(f"hello,{self.name}!")
person = person("Alice")
person.greet()
#Exception handling
try:
    number = int(input("Enter a number: "))
    exceot valueError:
    print("Invalid number")
    