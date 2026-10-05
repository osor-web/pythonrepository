# Python List Methods

fruits = ["apple", "banana", "orange"]
#Append() - adds an item to the end
fruits.append("mango")
print("After append:", fruits)

#Insert() - adds an item at a specific position
fruits.insert(1, "grape")
print("After insert:", fruits)

#Extend() - adds multiple items
fruits.extend(["watermelon", "pineapple"])
print("After extend:", fruits)

#Remove() - removes a specific item
fruits.remove("banana")
print("After remove:", fruits)

#Pop() - removes the last item
removed_item = fruits.pop()
print("Removed item:", removed_item)
print("After pop:", fruits)

#Index() - finds the position of an item
position = fruits.index("orange")
print("Position of orange:", position)

#Count() - counts how many times an item appears
fruits.append("apple")
print("Number of apples:", fruits.count("apple"))

#Sort() - sorts the list
fruits.sort()
print("After sort:", fruits)

#Reverse() - reverses the list
fruits.reverse()
print("After reverse:", fruits)

#Copy() - creates a copy of the list
new_fruits = fruits.copy()
print("Copied list:", new_fruits)

#Clear() - removes everything
fruits.clear()
print("After clear:", fruits)
        