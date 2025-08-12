# 1. Create and Access List Elements
# Create a list containing five different fruits and print the third fruit.

fruits_list = ['apple', 'banana', 'orange', 'mango', 'kiwi']

print(fruits_list[3])

# 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list.

list1 = [1,2,3]
list2 = [4,5,6]

print(list1+list2)

# list1.extend(list2)
# list1

# 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

list = [1,2,3,4,5,6,7,8,9,0]

list1 = []

list1.extend([list.pop(0)])
list1.extend([list.pop(4-1)])
list1.extend([list.pop()])

print(list1)

# 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.

movies = ['gorge', 'divergant', 'f1','in time', 'la la land']
movies_tuple = tuple(movies)

print(movies_tuple)

# 5. Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.

cities = ['London', 'Paris', 'Germany', 'Japan']

if cities.count('Paris') == 0:
    print("Paris does not exist")
else:
    print("Paris exists")

# 6. Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.
import copy

list = [1,2,3,4,5]

list1 = copy.deepcopy(list)
print(list1)

# 7. Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.

list = [1,2,3,4,5]
list1 = list.copy()
list1[0] = list[len(list)-1]
list1[len(list1)-1] = list[0]
print(list1)

# different method
list[0],list[-1] = list[-1], list[0]
print(list)

# 8. Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

tp = (1,2,3,4,5,6,7,8,9,10)
print(tp[3:7])

# 9. Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.

colors = ['black','red', 'blue', 'red', 'blue']
print(colors.count('blue'))

# 10. Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".

animals = ('rabbit','snake','lion', 'tiger')

print(animals.index('lion'))

# 11. Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.
atp = (1,2,3,4,5)
btp = (6,7,8,9,10)

print(atp + btp)

# 12. Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths.

l = [1,2,3,4,5]
t = (2,3,4,5,6,7,8)

print(len(l))
print(len(t))

# 13. Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.

t1 = (1,2,3,4,5)
t2 = [*t1] # * - unpacks the items from tuple
print(t2)

# 14. Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.

tup = (1,2,3,4,5)
max_tup = max(tup)
min_tup = min(tup)
print(f"Max value in a tuple is {max_tup}, and min value in a tuple is {min_tup}")

# 15. Reverse a Tuple
# Create a tuple of words and print it in reverse order.

tup = (1,2,3,4,5)
print(tup[::-1])
