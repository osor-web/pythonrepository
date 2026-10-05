try:
    number1 = int(input("Enter first number: "))

    number2 = int(input("Enter second number: "))

    answer =number1/number2

except ValueError:
    print("Please enter numbers only")

except ZeroDivisionError:
    print("You cannot divide by zero")

else:
    print("Answer:", answer)

finally:
    print("Program finished")
    
