def even():
    even_total = 0
    odd_total = 0
    for num in range(1, 21):
        if num % 2 == 0:
            print(num, "is even")
            even_total += num
        print("The sum of even numbers is = ", even_total)

        if num % 2 > 0:
            print(num, "is odd" ) 
            odd_total += num
        print("The sum of odd numbers is = ", odd_total)          
even()
