
# 1. is_prime(n) funksiyasi


import math
def is_Prime():
    n = int(input("enter number to check primality: "))
    if n>0:
        a = True
        for j in range(2,int(math.sqrt(n))+1):
                if n%j == 0:
                    a = False
                    break
        return a
    else:
         print("enter number greater than 0")


is_Prime()

# 2. digit_sum(k) funksiyasi

def digit_sum(k):
    k = list(str(k))
    sum = 0
    for i in k[:]:
          sum = sum + int(i)
    return sum

digit_sum(123)

# 3. Ikki sonning darajalari


def two_score(n):
        result = 0 
        i = 1
        while i<=n:
            result = 2 ** i
            if result>n:
                 break
            print(result)
            i+=1

two_score(30)
