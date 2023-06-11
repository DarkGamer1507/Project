def div():
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
        print("division of ",x,'and ', y,'is =',z)

div()