def div():
    ch = input('''Select from the following:
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
div()