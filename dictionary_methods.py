student = {
    "name": "osor",
    "age": 19,
    "course": "Cyber Security"
}

#Keys()
print("keys:", student.keys())

#Values()
print("valus:", student.values())

#Items()
print("items:", student.items())

#get()
print("name:", student.get("name"))

#Update()
student.update({"age": 20})
print("After upadate:", student)

#Setdefault
student.setdefault("School", "Ritman University")
print("After setdefault:", student)

#Copy
new_studet = student.copy()
print("copied dictionary:", new_studet)

#pop()
student.pop("age")
print("After pop:", student)

#popitem()
student.popitem()
print("After popitem:", student)

#Clear()
student.clear()
print("After Clear:", student)
