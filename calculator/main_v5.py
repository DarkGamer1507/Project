def add():
    l1 = []
    while True:
        try:
            ch = int(input("\nEnter the number of elements present in summation: "))
            break   
        except:
            print('Please enter an integer value!!!')
    
    for i in range(ch):
        x = input("Enter number: ")
        l1.append(x)
    
    y = 0
    for i in l1:
        y += int(i)

    print("sumation of all the provided numbers is : ",y)

def sub():
    l1 = []
    while True:
        try:
            ch = int(input("\nEnter the number of elements present in subtraction: "))
            break   
        except:
            print('Please enter an integer value!!!')
    
    for i in range(ch):
        x = input("Enter number: ")
        l1.append(x)
    
    y = int(l1.pop(0))
    for i in l1:
        y = y - int(i)

    print("The difference of all the provided numbers is (all the numbers are subtracted from first number provided) : ",y)

def mul():
    l1 = []
    while True:
        try:
            ch = int(input("\nEnter the number of elements present in multiplication: "))
            break   
        except:
            print('Please enter an integer value!!!')
    
    for i in range(ch):
        x = input("Enter number: ")
        l1.append(x)
    
    y = int(l1.pop(0))
    for i in l1:
        y = y * int(i)

    print("product of all the provided numbers is : ",y)

def div():
    ch = input('''\nSelect from the following:
        1. Normal division
        2. Floor division
        ''')
    
    if ch == '1':
        while True:
            try:
                x = int(input('Enter first number: '))
                y = int(input('Enter second number: '))
                break   
            except:
                print('Please enter an integer value!!!')

        if y == 0:
            print ("Division by 0 is not difined....")
            return
        
        else:
            z = x / y
            print("Division of ",x,'and ', y,'is =',z)
    
    elif ch == '2':
        while True:
            try:
                x = int(input('Enter first number: '))
                y = int(input('Enter second number: '))
                break   
            except:
                print('Please enter an integer value!!!')

        if y == 0:
            print ("Division by 0 is not difined....")
            return
        
        else:
            z = x // y
            print("Floor division of ",x,'and ', y,'is =',z)

    else:
        print('Select a valid option next time.....')
        return
    
def exo():
    while True:
        try:
            x = int(input('\nEnter first number: '))
            y = int(input('Enter second number: '))
            break   
        except:
            print('Please enter an integer value!!!')
    z = x ** y

    print(x,'raised to the power of ', y,'is =',z)


while True:
    print("________________________\n")
    print("WELLCOME TO CALCULATOR!!")

    ch = input('''Select from the following options:
        1.Addition 
        2.Subtraction
        3.Multiplication
        4.Division
        5.Exponent
        6.exit
        ''')
    
    if ch == '1':
        add()

    elif ch == '2':
        sub()

    elif ch == '3':
        mul()

    elif ch == '4':
        div()

    elif ch == '5':
        exo()

    elif ch == '6':
        break

    else:
        print("Select a valid option")

print("Thank you for using the program....")