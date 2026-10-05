# Python String Methods

text = "  hello python programming  "
#Upper() - converts to uppercase
print(text.upper())

#Lower() - converts to lowercase
print(text.lower())

#Capitalize() - capitalizes the first letter
print(text.capitalize())

#Title() - capitalizes each word
print(text.title())

#Strip() - removes spaces from both sides
print(text.strip())

#Replace() - replaces part of a string
print(text.replace("python", "Java"))

#Split() - converts string into a list
words = text.split()
print(words)

#Find() - finds the position of a word
print(text.find("python"))

#Count() - counts how many times something appears
print(text.count("o"))

#Startswith() - checks how the string starts
print(text.startswith("  hello"))

#Endswith() - checks how the string ends
print(text.endswith("  "))

#Isalpha() - checks if all characters are letters
name = "John"
print(name.isalpha())

#Isdigit() - checks if all characters are numbers
age = "25"
print(age.isdigit())

#Isalnum() - checks if characters are letters or numbers
code = "Python123"
print(code.isalnum())
