l1 = []

while True:         #input data
    l1.append(input("Admission Number: "))
    l1.append(input("Name: "))
    l1.append(input("Class: "))
    l1.append(input("Book status(loan/none): "))

    x = input("Continue (n/y): ")
    if x in ('y', 'Y'):
        break
    else:
        print('Re-enter data!')
        l1 = []
        continue

print(l1)


