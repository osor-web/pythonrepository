while True:
    score = 0

    print("Welcome to Paul's Quiz Application")
    print()

    print("1. what is the capital of Nigeria?")
    print("A. Lagos")
    print("B. Kano")
    print("c. Abuja")
    print("D. Niger")
     
    answer = input("Enter your answer")
    if answer == "C" or answer == "c":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong!")
    print()

    print("2. Which language are we using")
    print("A. Java")
    print("B. C++")
    print("C. HTML")
    print("D. Python")

    answer = input("Enter your answer")
    if answer == "D" or answer == "d":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong!")
    print()

    print("3. What does CPU stand for?")
    print("A. Central processing unit")
    print("B. Computer personal unit")
    print("C. central people union")
    print("D. computer processing user")

    answer= input("Enter your answer: ")
    if answer == "A" or answer == "a":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong!")
    print()

    print("4. Which is not a computer system brand")
    print("A. Hp")
    print("B. bugatti")
    print("C. dell")
    print("D. lenovo")

    answer = input("Enter your name: ")
    if answer == "B" or answer == "b":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong!")
        print()
    print("5. What does CIA stand for?")
    print("A. come induce attack")
    print("B. confidentility  integrity availability")
    print("C. crown intermediate account")
    print("D. corrupt inbox accunt")

    if answer == "B" or answer == "b":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong!")
        print()

    print("Quiz finished!")
    print("Your score is:", score, "out of 5")

    restart = input("Do you want to restart the quiz? (yes / no): ")
    if restart == "no" or "No":
       print("Thank you for playing!")
    break
    print()
