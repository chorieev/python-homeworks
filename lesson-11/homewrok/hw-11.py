# 1.the environment was created and the packages were installed
# 2.

# inside math_operations.py module:
def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a / b


# inside string_utils.py module:

def reverse(s):
    return s[::-1]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for i in s:
        if i in vowels:
            count+=1
    return count

# 3.
# inside geometry package:
# __init__.py
# circle.py :
def calculate_area(r):
    return 3.14 * (r**2)

def calculate_circumference(r):
    return 2 * 3.14 * r


# inside file_operations:
# __init__.py
# file_reader.py:
def read_file(file_path):
    with open(file_path, 'r') as file:
        file.read()
# file_writer.py:
def write_file(file_path, content):
    with open(file_path,'w') as file:
        file.write(content)

