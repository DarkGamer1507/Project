def add():
    while True:
        try:
            x = int(input('Enter first number: '))
            y = int(input('Enter second number: '))
            break   
        except:
            print('Please enter an integer value!!!')
    z = x + y

    print("Sum of ",x,'and ', y,'is =',z)

add()