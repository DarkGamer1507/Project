import math
def helper(n):
    if n == 1 or n == 0:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False


    sqn = int(math.sqrt(n)) + 1
    for i in range(2,sqn):
        if n%i == 0:
            return False
    
    return True



def checkprime(s):
    p = 0

    for i in (s):
        if helper(i):
            print(i)
            p += 1

    return p


l0 = []
count = int(input("Number of elements: ")) 

for i in range(count):
    l0.append(int(input("Enter element: ")))

x = checkprime(l0)
 
print("number of prime numbers present is: ", x)