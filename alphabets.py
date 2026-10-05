#List of all alphabets
alphabets = list("abcdefghijklmnopqrstuvwxyz")
vowels = ["a", "e", "i" "o", "u"]
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
#Separate vowels and consonants
vowel_list = ()
consonant_list = ()

for letter in alphabets:
    if letter in vowels:
        print(letter,  "is a vowel")
    
    else:
        print(letter, "is a Consonant")
        
#Display the results
print("All alphabets:", alphabets)
print("Vowels = ", vowels)
print("Consonants:", consonants)
