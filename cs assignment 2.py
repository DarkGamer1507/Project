import pickle

def add():
    with open('students.dat', 'rb') as file1:
        l1 = pickle.load(file1)

    while True:
        l2 = []
        l2.append(input("Enter Name: "))
        l2.append(input("Enter Class: "))
        l2.append(input("Enter Percentage: "))
        l1.append(l2)

        ch = input("add more? (n/y)")
        if ch.lower() == 'n':
            break

    with open('students.dat', 'wb') as file2:
        pickle.dump(l1,file2)

def display():
    with open('students.dat', 'rb') as file1:
        l1 = pickle.load(file1)

    print("NAME,CLASS,PERCENTAGE")
    for i in l1:
        print(i[0],i[1],i[2])

def count():
    with open('students.dat', 'rb') as file1:
        l1 = pickle.load(file1)

    ct = 0

    for i in l1:
        ct += 1

    print("Number of records present in the file: ", ct)

def search(s):
    with open('students.dat', 'rb') as file1:
        l1 = pickle.load(file1)

    ct = 0

    for i in l1:
        if i[2] >= s:
            ct += 1

    print("Number of students with percentage higher than",s,";", ct)

def modify(s):
    with open('students.dat', 'rb') as file1:
        l1 = pickle.load(file1)
    ct =0
     
    for i in l1:
        if i[0] == s:
            ct += 1
            i[0] = input("Enter new name: ")
            i[1] = input("Enter new class: ")
            i[2] = input("Enter new percentage: ")

    with open('students.dat', 'wb') as file2:
        pickle.dump(l1,file2)

    if ct == 0 :
        print("student not found")
    
def dele(s):
    with open('students.dat', 'rb') as file1:
        l1 = pickle.load(file1)
    ct =0
     
    for i in l1:
        if i[0] == s:
            ct += 1
            l1.remove(i)

    with open('students.dat', 'wb') as file2:
        pickle.dump(l1,file2)

    if ct == 0 :
        print("student not found")

while True:
    choice = int(input('''Select function: 
        1. Add a new record
        2. Display all records
        3. count the number of records in file
        4. Search and count the number of students whose percentage is greater than a  certain value
        5. Modify a record
        6. Delete a record
        7. exit
        '''))

    if choice == 1:
        add()

    elif choice == 2:
        display()

    elif choice == 3:
        count()

    elif choice == 4:
        s = input("Enter percentage: ")
        search(s)

    elif choice == 5:
        s = input("Enter name: ")
        modify(s)

    elif choice == 6:
        s = input("Enter name: ")
        dele(s)

    elif choice == 7:
        break

    else:
        print("select a valid input!")