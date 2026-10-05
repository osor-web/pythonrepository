import random
import string

length = int(input("Enter password length: "))
if length < 4:
    print("Password must be at least 4 characters long")
else:
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = "!@#$%^&*"
    
    password = ""

    password = password + random.choice(uppercase)
    password = password + random.choice(lowercase)
    password = password + random.choice(numbers)
    password = password + random.choice(symbols)
     
    characters = uppercase + lowercase + numbers + symbols

    for i in range(length - 4): password = password + random.choice(characters)

    print("Generated passwor:", password)




