import random

urls = {}
long_url = input("Enter a long URL: ")

number = random.randint(10000, 99999)

short_url = "short.ly/" + str(number)

urls[short_url] = long_url

print("Your shortened URL is:", short_url)
print("Original URL is:", urls[short_url])