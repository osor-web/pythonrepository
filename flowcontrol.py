# if statement
age = 20
if age >= 18:
    print("you are an adult")

# if else
age = 16
if age >= 18:
    print("Adult")
else:
    print("Minor")
# if/elif/else
score = 75
if score >= 70:
    print("Grade A")
elif score >= 60:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Fail")

# For loop
for i in range(5):
    print(i)

# while loop
count = 1
while  count <= 5:
    print(count)
    count += 1

# Break
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue
for i in range(5):
    if i == 2:
        continue
        print(i)

# Pass
age = 20
if age >= 18:
    pass
else:
    print("Minor")
print ("Program finished")
