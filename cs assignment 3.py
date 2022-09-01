import csv

def add():
    l1 = []
    while True:
        l2 = []
        l2.append(input("Enter employee ID: "))
        l2.append(input("Enter employee Name: "))
        l2.append(input("Enter employee Salary: "))
        l1.append(l2)

        ch = input("add more? (n/y)")
        if ch.lower() == 'n':
            break

    with open('employee.csv','a',newline='') as file1:
        writer = csv.writer(file1)
        writer.writerows(l1)

def display():
    with open('employee.csv','r',newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]
    print('ID,NAME,SALARY')

    for i in read:
        print(i[0],i[1],i[2])

def count():
    with open('employee.csv','r',newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    ct = 0

    for i in read:
        ct += 1

    print("Number of records present in the file: ",ct)

def salary(s):
    with open('employee.csv','r',newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]
    ct = 0
    
    for i in read:
        if i[2] >= s:
            ct += 1

    print("Number of employees who have salary more than", s, ": ", ct)
    
while True:
    choice = int(input('''Select function: 
        1. Add a new record
        2. Display all records
        3. count the number of records in file
        4. Search and count the number of employees whose salary is greater than a  certain value
        5. exit
        '''))

    if choice == 1:
        add()

    elif choice == 2:
        display()

    elif choice == 3:
        count()

    elif choice == 4:
        s = input("Enter the salary value: ")
        salary(s)

    elif choice == 5:
        break

    else:
        print("Enter a valid input!")