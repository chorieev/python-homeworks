# 1. Age Calculator
# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

name = input("Ismingizni kiriting: ")
year_of_birth = int(input('Tug\'ilgan yilingizni kiriting: '))
current_year = 2025
print(f"{name}ning yoshi {current_year-year_of_birth} da")

# 2. Extract Car Names
# Extract car names from the following text:
txt = 'LMaasleitbtui'
print(txt[0:len(txt):2]) # Lasetti
print(txt[1:len(txt):2]) # Malibu

# 3. Extract Car Names
# Extract car names from the following text:
txt = 'MsaatmiazD'
print(txt[0:len(txt):2]) # Matiz
print(txt[len(txt):0:-2]) # Damas

# 4. Extract Residence Area
# Extract the residence area from the following text:
txt = "I'am John. I am from London"
print(txt[-6:])

# 5. Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.

user_input = input("please enter smth to reverse: ")
print(user_input[::-1])

# 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.

vowels = 'Python is an amazing programming language'

counts = vowels.count('a') + vowels.count('e') + vowels.count('i')+vowels.count('o')+vowels.count('u')+vowels.count('A')+vowels.count('E')+vowels.count('I')+vowels.count('O')+vowels.count('U')
print(counts)

# 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.

max_num = input("son kriting: ")
list_ofnum = map(int, max_num.split() ) # map(function, iterable) - applies the function to each iterable(list, tuple)
print(max(list_ofnum))

# 8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

palindrome = input('enter a word to check palindrome: ')

if palindrome == palindrome[::-1]:
    print("palindrome")
else: 
    print("not palindrome")

# 9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.

email = input("please enter your email: ")
pos = email.find('@')
email = email[pos:len(email)]
print(email)

# 10. Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.

import random # imports the random
import string # imports the string

char  = string.ascii_letters + string.digits + string.punctuation # using string the random digits,letters,and punctuation is added
password = "".join(random.choice(char)for _ in range(5)) # creates a password of 5 which takes random value 5 times and joins them together
print(password)
