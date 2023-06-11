def sub():
    l1 = []
    while True:
        try:
            ch = int(input("Enter the number of elements present in subtraction: "))
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

sub()