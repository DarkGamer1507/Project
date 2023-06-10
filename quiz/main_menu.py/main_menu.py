while True:
    print ("_______________________________________")
    print("WELLCOME TO QUIZ!!!!!!!!")
    print ("_______________________________________\n")

    ch = input('''Choose from the following options...
        1. new user
        2. old user
        3. exit
        ''')
    
    if ch == '1':
        id = input("Enter your quiz id: ")

    elif ch == '2':
        print('')

    elif ch == '3':
        break

    else:
        print('enter a valid input!')