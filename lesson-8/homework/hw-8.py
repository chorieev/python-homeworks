# 1.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

try:
    print(5/0)
except ZeroDivisionError as error:
    print('zero division error')

# 2.Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

try:
    n = int(input('please enter integer: '))
    print(n)
except ValueError as error:
    raise ValueError

# 3.Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

try:
    with open('lesson-9/text.txt', 'r') as file:
        file.read()
except FileNotFoundError as error:
    print("the given file is not found")


# 4.Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

try:
    n1 = float(input("enter 1st number: "))
    n2 = float(input("enter 2nd number: "))
    print(n1,n2)
except ValueError:
    raise TypeError("enter only numerical numbers")




# import re

# n1 = input("please enter two numbers(n1/n2), n1: ")
# n2 = input("n2: ")

# if re.fullmatch(r"-?\d+(\.\d+)?", n1) and re.fullmatch(r"-?\d+(\.\d+)?", n2): ## important catch here is the 
#     print(n1)
#     print(n2)
# else:
#     raise TypeError

# 5.Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
import os

with open('lesson-8/info.txt', 'w') as file:
    file.write("hello world")

os.chmod('lesson-8/info.txt', 0o444)

try:
    with open('lesson-8/info.txt', 'w') as file:
        file.write("new content")
except PermissionError as error:
    print("the given file is read-only!")
    
#raise error("the given file is read-only!")


# 6.Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.


list1 = [1,2,3]

try:
    for i in range(4):
        print(list1[i])
except IndexError:
    print('index out of range')


# 7.Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.

try:
    n = input("enter a number: ")
except KeyboardInterrupt:
    print("\nplease dont cancel the input!")

# 8.Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

try:
    print(5/0)
except ArithmeticError:
    print("there was an arithmatic-related error")

# 9.Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

try:
    with open('lesson-8/info.txt', 'r', encoding='utf-16') as file:
        file.read()
except UnicodeDecodeError:
    print("wrong encoding!")

# 10.Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

list1 = [1,2,3,4]

try:
    for i in list1:
        print(list1[i].upper())
except AttributeError:
    print("the written attribute does not exist!")



## Python File Input Output: Exercises, Practice, Solution

# File Input/Output Exercises

# 1.Write a Python program to read an entire text file.

with open("lesson-8/info.txt", 'r') as file:
    file.read()

# 2. Write a Python program to read first n lines of a file.

with open('lesson-8/info.txt', 'r') as file:
    n = int(input("enter the number of lines:"))
    for i in range(n):
        print(file.readline())

# 3.Write a Python program to append text to a file and display the text.

with open('lesson-8/info.txt', 'a+') as file:
    file.write("\n4")
    file.seek(0)
    print(file.read())

# 4.Write a Python program to read last n lines of a file.

n = 5

with open('lesson-8/info.txt', 'r+') as file:
    lines = file.readlines()
    lines = lines[-n:]
    for i in lines:
        print(i)


# 5.Write a Python program to read a file line by line and store it into a list.

list1 = []

with open("lesson-8/info.txt", 'r') as file:
    for i in file: # iterates line by line
        list1.append(i.strip()) # .strip() removes '\n'

print(list1)

# 6.Write a Python program to read a file line by line and store it into a variable.

var = ''

with open("lesson-8/info.txt", 'r') as file:
    for i in file: # iterates line by line
        var+=i.strip() + ' '

print(var)

# 7.Write a Python program to read a file line by line and store it into an array.

list2 = []

with open("lesson-8/info.txt", 'r') as file:
    for i in file: # iterates line by line
        list2.append(i.strip()) # .strip() removes '\n'

print(list2)

# 8.Write a Python program to find the longest words.

# with open("lesson-8/info.txt", 'a') as file:
#     file.write("this_is_the_longest_word")

list3 = []

with open("lesson-8/info.txt", 'r') as file:
    for i in file:
        list3.extend( i.split())

a = ''
for i in list3[:]:
    if len(i) > len(a):
        a = i

print(a)

# 9.Write a Python program to count the number of lines in a text file.

count = 0
with open("lesson-8/info.txt", 'r') as file:
    for i in file:
        count+=1
print(count)

# 10.Write a Python program to count the frequency of words in a file.

list4 = []
with open("lesson-8/info.txt", 'r') as file:
    for i in file:
        list4.extend(i.split())

dict1 = {}
# dict1.update()
for i in list4:
    list4.count(i)
    if i in dict1:
        continue
    else:
        dict1[i] = list4.count(i)

print(dict1)


# 11.Write a Python program to get the file size of a plain file.

import os

size = os.path.getsize("lesson-8/info.txt")

print(f"lesson-8/info.txt --> {size} bytes")

# 12.Write a Python program to write a list to a file.

with open('lesson-8/info.txt', 'w') as file:
    list1 = ['math', 'history', 'subject']
    file.write(','.join(list1))

# 13.Write a Python program to copy the contents of a file to another file.

import shutil

shutil.copy('lesson-8/info.txt', 'lesson-8/info1.txt')


with open('lesson-8/info1.txt', 'r') as file:
    file.read()

# different method - not originally copying

list3 = []

with open("lesson-8/info.txt", 'r') as file:
    for i in file:
        list3.extend( i.split())

with open('lesson-8/info1.txt', 'w') as file:
    for i in list3:
        file.write(i)

# different method

with open("lesson-8/info.txt", 'r') as s_file:
    with open('lesson-8/info1.txt', 'w') as d_file:
        for i in s_file:
            d_file.write(i)

# 14.Write a Python program to combine each line from the first file with the corresponding line in the second file.

dict2 = {}

with open("lesson-8/info.txt", 'r') as file:
    count1 = 1
    for i in file:
        dict2[count1]= i
        count1+=1

dict2

dict3 = {}
with open("lesson-8/info1.txt", 'r') as file:
    count2 = 1
    for i in file:
        dict3[count2]= i
        count2+=1


dict3

dict4 = []
for i in dict2.keys():
    for j in dict3.keys():
        if i == j:
            dict4.append(dict2[i].rstrip('\n') +  dict3[j])

# # more efficient way:
# for i in dict2.keys() & dict3.keys():
#     dict4.append(dict2[i].rstrip('\n') +  dict3[i])


dict4

with open('lesson-8/info2.txt', 'w') as file:
    for i in range(len(dict4)):             
        file.write(dict4[i])                

# # more efficient way:
# for i in dict4:
# file.write(i)



# 15. Write a Python program to read a random line from a file.

import random

with open('lesson-8/info.txt', 'r') as file:
    ln = file.readlines()

r = random.choice(ln)
print(r)

# 16.Write a Python program to assess if a file is closed or not.

# file.closed() -- returns boolean - tells whether file is closed or not

with open("lesson-8/info.txt", 'r') as file:
    file.read()

if file.closed:
    print("the file is closed")
else:
    print("the file is open")

# 17.Write a Python program to remove newline characters from a file.

list1 = []

with open('lesson-8/info.txt', 'r') as file:
    for i in file.readlines():
        list1.append(i.rstrip('\n')) # .append() - moves as a full string to list

list1
with open('lesson-8/info2.txt', 'w') as file:
    for i in list1:
        file.write(i)

# 18.Write a Python program that takes a text file as input and returns the number of words in a given text file.
# Note: Some words can be separated by a comma with no space.

list1 = []

with open('lesson-8/info.txt', 'r') as file:
    list1 = file.read().replace(',',' ').split()
print(len(list1))

# 19.Write a Python program to extract characters from various text files and put them into a list.


list1 = []

with open('lesson-8/info.txt', 'r') as file:
    list1.extend(file.read())

list2 = []

with open('lesson-8/info1.txt', 'r') as file:
    list2.extend(file.read())

list3 = []

with open('lesson-8/info2.txt', 'r') as file:
    list3.extend(file.read())

final_list = list1 + list2 + list3
print(final_list)

# 20.Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

import string

a = string.ascii_uppercase

direct = 'lesson-8/'

for i in a:
    i = i + '.txt'
    with open(direct+i, 'w') as file:
        file.write(i)

# 21.Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.

b = string.ascii_letters
b = list(b)
n = 7
with open('lesson-8/allletters.txt', 'w') as file:
    for i in range(0, len(b), n):
        file.write(''.join(b[i:i+n]) + '\n') # used .join cause we cant add '\n' to list - error: can only concatenate list (not "str") to list
