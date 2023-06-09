def add():
    how = int(input("How many elements? "))
    x = 0
    for i in how:
        x += int(input("Enter element: "))

    print("Sum of all the elements is : ", x)

add()