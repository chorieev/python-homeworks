## warm up exercise

import threading

a = int(input('enter 1st number: '))
b = int(input('enter 2nd number: '))


def even_num(a,b):
    str1 = ''
    for i in range(a,b+1):
        if i % 2 == 0:
            str1+=str(i) + ', '
    print(str1)

t1 = threading.Thread(target=even_num, args=(a, int( (a+b)/2 )))
t2 = threading.Thread(target=even_num, args=(int((a+b)/2),b))

t1.start()
t2.start()

t1.join()
t2.join()

print('threading completed')


## HW

# Exercise 1: Threaded Prime Number Checker

# Write a Python program that checks whether a given range of numbers contains prime numbers. 
# Divide the range among multiple threads to parallelize the prime checking process. 
# Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.

import threading


a = int(input('enter 1st number: '))
b = int(input('enter 2nd number: '))

mid = (a+b)//2

global result
result = []

def is_prime(a,b):
    list1 = []
    
    for i in range(a, b+1):
        if i < 2:
            continue

        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            list1.append(i)
    result.extend(list1)


t1 = threading.Thread(target=is_prime, args=(a,mid))
t2 = threading.Thread(target=is_prime, args=(mid+1,b))

t1.start()
t2.start()

t1.join()
t2.join()


print(f'all the prime numbers found: {result}')
print('threading finished')


# Exercise 2: Threaded File Processing

# Write a program that reads a large text file containing lines of text. 
# Implement a threaded solution to count the occurrence of each word in the file. 
# Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.



with open('text.txt', 'r') as file:
    data = file.read().split()
    mid = len(data)//2
    chunk1 = data[:mid]
    chunk2 = data[mid:]



results = []

def func(chunk, output):
    dict1 = {}
    for i in chunk:
        dict1[i]= dict1.get(i,0)+1
        #dict1[i]=chunk.count(i)
    output.append(dict1)
    #print(dict1)

thread_output = []

c1 = threading.Thread(target=func, args=(chunk1,thread_output))
c2 = threading.Thread(target=func, args=(chunk2,thread_output))

c1.start()
c2.start()


c1.join()
c2.join()


## did not do myself
final_counts = {}

for d in thread_output:       # go through each thread's dictionary
    for word, count in d.items():
        final_counts[word] = final_counts.get(word, 0) + count

print(final_counts)
## till here


print('process has finished')
