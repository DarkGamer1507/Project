def add():
    x = int(input('\nEnter first number: '))
    y = int(input('Enter second number: '))
    z = x + y

    print("Sum of ",x,'and ', y,'is =',z)


def sub():
    x = int(input('\nEnter first number: '))
    y = int(input('Enter second number: '))
    z = x - y

    print("Difference of ",x,'and ', y,'is =',z)

def mul():
    x = int(input('\nEnter first number: '))
    y = int(input('Enter second number: '))
    z = x * y

    print("product of ",x,'and ', y,'is =',z)

def div():
    x = int(input('\nEnter first number: '))
    y = int(input('Enter second number: '))
    z = x / y

    print("division of ",x,'and ', y,'is =',z)


while True:
    print("________________________\n")
    print("WELLCOME TO CALCULATOR!!")

    ch = input('''Select from the following options:
        1.Addition 
        2.Subtraction
        3.Multiplication
        4.Division
        5.exit
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
        break
    else:
        print("Select a valid option")

print("Thank you for using the program....")