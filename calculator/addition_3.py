def add():
    l1 = []
    while True:
        try:
            ch = int(input("Enter the number of elements present in summation: "))
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

add()