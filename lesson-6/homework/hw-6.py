# 1. Modify String with Underscores

# Given a string txt, insert an underscore (_) after every third character. 
# If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. 
# No underscore should be added at the end.


txt = input("enter string: ")
txt = list(txt)

for i in range(2, len(txt), 3):
    if i in range(len(txt),len(txt)+2 ) or i in range(len(txt)-2, len(txt)):
        break #txt[i] = txt[i]
    if txt[i].lower() in ['a','u','e','o','i'] or (txt[i+1] == ['_'] and txt[i] in ['_']):
        txt[i] = txt[i]
    else:
        txt[i] = txt[i] + "_"

print("".join(txt))


# 2. Integer Squares Exercise

n = int(input("enter number: "))
if 1<=n<=20:
    i = 0
    while 0 <= i < n:
        print(i**2)
        i+=1
else:
    print("enter number greater than 1 and lower then 20")

# 3. Loop-Based Exercises

# Exercise 1: Print first 10 natural numbers using a while loop

i = 1
while 1<=i<=10:
    print(i)
    i+=1

# else:
#     i+=1
#     while 1<=i<=10:
#         print(i)
#         i+=1


# Exercise 2: Print the following pattern

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

i = 1
str1 = ""
while i <=5:
    str1 += str(i) + " "
    print(str1)
    i+=1

# Exercise 3: Calculate sum of all numbers from 1 to a given number

n = int(input("Enter number "))
i = 1
sum = 0

while i<=n:
    sum = sum + i
    i+=1
print(f"Sum is: {sum}")

# Exercise 4: Print multiplication table of a given number

n = int(input("enter number for multiplication table: "))

i = 1
while i<=10:
    print(i*n)
    i+=1

# Exercise 5: Display numbers from a list using a loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i in numbers[1:3] or i == numbers[4]:
        print(i)

# Exercise 6: Count the total number of digits in a number

n = input("enter digits: ")
n = list(n)


i = 0 
while i < len(n):
    i+=1

print("Output:", i)

# Exercise 7: Print reverse number pattern

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1


j = 5
i = 5

while j >=1:
    str1 = ""
    while i >=1:
        str1 += str(i) + " "
        i-=1
    print(str1)
    j-=1
    i=j

    
# Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]

i = 1

while i <=len(list1):
    print(list1[-i])
    i+=1


# Exercise 9: Display numbers from -10 to -1 using a for loop

for i in range(-10,-1+1):
    print(i)


# Exercise 10: Display message “Done” after successful loop execution

n=4
i = 0
while i <=n:
    print(i)
    i+=1
else:
    print("Done")

# Exercise 11: Print all prime numbers within a range:

# Prime numbers between 25 and 50:
# 29
# 31
# 37
# 41
# 43
# 47

import math

n = int(input("given a range, enter first number: "))
n1 = int(input("enter second one: "))

for i in range(n,n1+1):
    is_prime = True
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)

# Exercise 12: Display Fibonacci series up to 10 terms

i = 0
j = 1
next_num = 0
str1 = ""
str1 += " " + str(i)
str1 += " " + str(j)

while True:
    next_num = j + i
    if next_num > 50:
        break
    str1 += " " + str(next_num)
    i = j
    j = next_num

print(str1)


# Exercise 13: Find the factorial of a given number

# with while-loop
n = int(input("enter number:"))

i = 1
fct = 1
while i <=n:
    fct = fct*i
    i+=1
print(f"{n}! = {fct}")

# with for-loop

n = int(input("enter number:"))

fct = 1
for i in range(1,n+1):
    fct = fct*i

print(f"{n}! = {fct}")


# 4. Return Uncommon Elements of Lists

# second try
import copy

list1 = [1, 1, 2, 3, 4, 2]
list11 = copy.deepcopy(list1)
list2 = [1, 3, 4, 5]
list22 = copy.deepcopy(list2)
list3 = []

for i in list11[:]:
    for j in list22[:]:
        if i == j :
            if i in list1:
                list1.remove(i)
            if j in list2:
                list2.remove(j)

list3 = list1 + list2
print(list3)
