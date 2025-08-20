
# 1. Circle Class
# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

class Circle:
    def __init__(self, r):
        self.r = r
        self.pi = 3.14

    def area(self):
        return self.pi * (self.r**2)
        # print(f'Area: {self.pi * (self.r**2)}')

    def perimetr(self):
        return float(2 * self.r * self.pi)
        # print(f'Perimetr: {float(2 * self.r * self.pi)}')

c1 = Circle(5)
print(f'Area: {c1.area()}')
print(f'Perimetr: {c1.perimetr()}')

# 2. Person Class
# Write a Python program to create a Person class. 
# Include attributes like name, country, and date of birth. Implement a method to determine the person's age.

from datetime import date, datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
        
    
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year
    
p1 = Person('Behruz', 'Uzb', date(2007,7,16))

print(p1.age())

# 3. Calculator Class
# Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

## addition - substraction - multiplication - division 

class Calculator:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b
    
    def substraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b
    
    def division(self):
        return self.a / self.b
    
v1 = Calculator(10,5)

print(v1.addition())
print(v1.substraction())
print(v1.multiplication())
print(v1.division())


# 4. Shape and Subclasses
# Write a Python program to create a class that represents a shape. 
# Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.

class Shape:
    def __init__(self):
        pass

    def area(self):
        pass
    
    def perimetr(self):
        pass
    

class Circle(Shape):
    def __init__(self, r):
        self.r = r
        self.pi = 3.14

    def area(self):
        return self.pi * (self.r ** 2)
    
    def perimetr(self):
        return 2 * self.r * self.pi
    
import math

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a)*(s - self.b)*(s - self.c))
        return area
    
    def perimetr(self):
        return self.a + self.b + self.c
    

class Square(Shape):
    def __init__(self, a):
        self.a = a
    
    def area(self):
        return self.a**2

    def perimetr(self):
        return self.a * 4


c1 = Circle(5)
t1 = Triangle(2,3,4)
s1 = Square(3)

print(f'Circle area: {c1.area()}')
print(f'Circle perimetr: {c1.perimetr()}')
print(f'Triangle area: {t1.area()}')
print(f'Triangle perimetr: {t1.perimetr()}')
print(f'Square area: {s1.area()}')
print(f'Square perimetr: {s1.perimetr()}')

# 5. Binary Search Tree Class
# Write a Python program to create a class representing a binary search tree. 
# Include methods for inserting and searching for elements in the binary tree.

class BinerySearchTree:
    def  __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinerySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinerySearchTree(value)
            else:
                self.right.insert(value)
    
    def search(self, value):
        if value == self.value:
            return True
        
        if value < self.value:
            if self.left is not None:
                return self.left.search(value)
            else:
                return False
            
        if value > self.value:
            if self.right is not None:
                return self.right.search(value)
            else:
                return False
        


p1 = BinerySearchTree(10)

p1.insert(5)
p1.insert(4)
p1.insert(3)
p1.insert(6)
p1.insert(7)
p1.insert(8)


print(p1.left.left.left.value) # to get value
print(p1.search(2)) # to search value


# 6. Stack Data Structure
# Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

class StackDataStructure:

    def __init__(self):
        self.list1 = []

    def push(self, value):
        self.list1.append(value)

    def pop(self):
        if len(self.list1) > 0:
            self.list1.pop()
        else:
            return 'stack is empty'
    
p1 = StackDataStructure()
p2 = StackDataStructure()

p1.push('bread')
p1.push('pancake')
p1.push('cake')

print(p2.pop())

print(p1.list1)

# 7. Linked List Data Structure
# Write a Python program to create a class representing a linked list data structure. 
# Include methods for displaying linked list data, inserting, and deleting nodes.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # def 
            
        

# list1 = ''
# dir(list1)

# 8. Shopping Cart Class
# Write a Python program to create a class representing a shopping cart. 
# Include methods for adding and removing items, and calculating the total price.


class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add(self, item, cost):
            self.cart[item] = cost
            return self.cart
    
    def remove(self, item):
        del self.cart[item]
        return self.cart
    
    def total_price(self):
        total_price = 0
        for i in self.cart.values():
            total_price+=i
        items = ', '.join(self.cart.keys())
        return f'Total price for {items} is {total_price} usd'
    
    def display(self):
        str1 = ''
        for key, value in self.cart.items():
            str1+= f'{key}: {value} usd\n'
        return str1.strip()


item1 = ShoppingCart()
item1.add('cola', 2)
item1.add('pepsi', 2.3)
print(item1.add('fanta', 3.3))

item1.remove('pepsi')
print(item1.display())

print(item1.total_price())

# 9. Stack with Display
# Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.

class StackDataStructure:

    def __init__(self):
        self.list1 = []

    def push(self, value):
        self.list1.append(value)

    def pop(self):
        if len(self.list1) > 0:
            return self.list1.pop()
        else:
            return 'stack is empty'
    
    def display(self):
        if len(self.list1) == 0 :
            return 'stack is empty'
        all_data = ', '.join(map(str, self.list1))
        return f'all data in list: {all_data}'
    
p1 = StackDataStructure()
p2 = StackDataStructure()

p1.push('bread')
p1.push('pancake')
p1.push('cake')

p1.pop()
print(p1.display())
print(p2.display())

# 10. Queue Data Structure
# Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

class QueueData:
    def __init__(self):
        self.lis1 = []

    def enqueueing(self, data):
        self.lis1.append(data)

    def dequeueing(self):
        removed_data = self.lis1.pop(0)
        return removed_data

    def display(self):
        all_data = ', '.join(map(str,self.lis1))
        return f'Queue is as follows: {all_data}'

data = QueueData()

data.enqueueing('bread')
data.enqueueing('fuse tea')
data.enqueueing('cola')
data.enqueueing('pepsi')

data.dequeueing()

print(data.display())


# 11. Bank Class
# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

class Bank:
    def __init__(self):
        self.customer_list = {}

    def add_customer(self, customer, initial_deposit):
        self.customer_list[customer] = initial_deposit

    def remove_customer(self, customer):
        return  self.customer_list.pop(customer, 'Customer does not exist!')
         
    
    def add_deposit(self, name, amount):
        if name in self.customer_list:
            self.customer_list[name]+= amount
        else:
            return 'Customer does not exist!'
    
    def withdraw(self, name, amount):
        if name in self.customer_list:
            self.customer_list[name]-=amount
        else:
            return 'Customer does not exist!'
        
            
    def display(self):
        for key,value in self.customer_list.items():
                print(f"{key}'s balance: {value}")



c2 = Bank()

c2.add_customer('Behruz', 20000)
c2.add_customer('Akmal', 120000)
c2.display()
print('-'*20)
c2.add_deposit('Behruz',5000)
c2.add_deposit('Akmal',5000)
c2.display()
print('-'*20)
c2.withdraw('Behruz',5000)
c2.withdraw('Akmal',5000)
c2.display()
print('-'*20)
c2.remove_customer('Behruz')
c2.display()

