def exo():
    while True:
        try:
            x = int(input('Enter first number: '))
            y = int(input('Enter second number: '))
            break   
        except:
            print('Please enter an integer value!!!')
    z = x ** y

    print(x,'raised to the power of ', y,'is =',z)

exo()