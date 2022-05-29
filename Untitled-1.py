def evenodd():
    n = int(input("Enter a number: "))
    if n%2 == 0:
        print(n, "is a even number")
    
    else:
        print(n, "is a odd number")

def smeven():
    lower = int(input("Enter the lower limit: "))
    upper = int(input("Enter the upper limit: "))
    sum1 = 0

    for i in range(lower,upper+1): #upper limit is included
        if i%2 == 0:
            sum1 += i

    print("Sum of all even numbers in range",lower ,"to", upper, "is", sum1)

def smodd():
    lower = int(input("Enter the lower limit: "))
    upper = int(input("Enter the upper limit: "))
    sum1 = 0

    for i in range(lower,upper+1): #upper limit is included
        if i%2 != 0:
            sum1 += i

    print("Sum of all odd numbers in range",lower ,"to", upper, "is", sum1)

def exit():
    exit

while True:
    x = int(input('''Select a function from below: 
                    1. To check whether number is even or odd 
                    2. To find sum of even numbers in a range 
                    3. To find sum of odd numbers in a range 
                    4. Exit 
                     '''))

    if x == 1:
        evenodd()
    elif x == 2:
        smeven()
    elif x == 3:
        smodd()
    elif x == 4:
        break

exit()
