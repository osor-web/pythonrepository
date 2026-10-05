#list of aphabets
alphabets = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"

#Seperte vowels from consonants
vowels_list = []
consonants_list = []

#To count
vowels_count = 0
consonants_counts = 0

for letter in alphabets:
    if letter in vowels:
        vowels_list.append(letter)
        vowels_count += 1
    else:
        consonants_list.append(letter)
        consonants_counts += 1

print("Vowels:", vowels_list)
print("Consonants:", consonants_list)

print("Number of vowels:", vowels_count)
print("Number of Consonants:", consonants_counts)


