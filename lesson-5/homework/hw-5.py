# 1
# def is_leap(year): """ Determines whether a given year is a leap year.
def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("The year is a leap year")
    else:
        print("The year is not a leap year")

is_leap(2024)

# 2. Conditional Statements Exercise

n = int(input("please enter number to check: "))

if n%2 != 0:
    print("Weird")
elif n%2 == 0 and n in range(2,5+1):
    print("Not Weird")
elif n%2 == 0 and n in range(6,20+1):
    print("Weird")
elif n%2 == 0 and n > 20:
    print("Not Weird")

# Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.

a = 3
b = 20

# # with-loop
# for i in range(a,b):
#     if i % 2 ==0:
#         print(i, "Even")

# without-loop
a = 3
b = 100

alist = []
if a % 2 == 0:
    alist = list(range(a, b + 1, 2))
else:
    a+=1
    alist = list(range(a, b + 1, 2))

print(alist)

# without - loop / without if/else
a = 5
b = 100

alist = []

a = a + (a%2)
alist = list(range(a, b + 1, 2))

print(alist)
