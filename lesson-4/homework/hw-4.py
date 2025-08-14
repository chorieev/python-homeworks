# 1. Sort a Dictionary by Value
# Write a Python script to sort (ascending and descending) a dictionary by value.
# del list

dict1 = {
    "name": "Behruz",
    "age": "18",
    "study": "Inha",
    "home": "Tashkent"
}

sorted_items = sorted(dict1.items(), key=lambda item:item[1]) # the important thing that does the task
sorted_items
sorted_dict = dict(sorted_items)
print(sorted_dict)


# 2. Add a Key to a Dictionary
# Write a Python script to add a key to a dictionary.

nums = {0: 10, 1: 20}

nums[2] = 30

print(nums)

# 3. Concatenate Multiple Dictionaries
# Write a Python script to concatenate the following dictionaries to create a new one.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic1.update(dic2)
dic1.update(dic3)
print(dic1)

# 4. Generate a Dictionary with Squares
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

empty = {}
for i in range(1,6):
    empty[i] = i**2

print(empty)

# 5. Dictionary of Squares (1 to 15)
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.


dict_of_squares = {}
for i in range(1,16):
    dict_of_squares[i] = i**2

print(dict_of_squares)


## Set Exercises

# 1. Create a Set
# Write a Python program to create a set.

fruits = {"apple", "banana", "pineapple", "orange"}

# 2. Iterate Over a Set
# Write a Python program to iterate over sets.

fruits = {"apple", "banana", "pineapple", "orange"}

for i in fruits:
    print(i)

# 3. Add Member(s) to a Set
# Write a Python program to add member(s) to a set.

fruits.add("melon")
print(fruits)

# 4. Remove Item(s) from a Set
# Write a Python program to remove item(s) from a given set.

fruits.remove("melon")
print(fruits)

# 5. Remove an Item if Present in the Set
# Write a Python program to remove an item from a set if it is present in the set.

fruits = {"apple", "banana", "pineapple", "orange", "melon"}

if "melon" in fruits:
    fruits.remove("melon")
    print(fruits)
else:
    print("fruit does not exist")
