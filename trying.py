import csv
from datetime import datetime

def dateinp():
    '''This function inputs return date for book aswell as ensures that the date is in correct 
    format for further use.'''
    while True:
        date = input("Return date(dd-mm-yyyy):")
        if len(date) != 10 or date[2] != '-' or date[5] != '-':
            print('Enter correct format!')
            continue
        else:
            return date

def student_add():
    '''This function adds a new student to csv file.'''
    print("ADDING A NEW ENTRY")
    l1 = []

    while True:         #input data
        l1.append(input("Admission Number: "))
        l1.append(input("Name: "))
        l1.append(input("Class: "))
        l1.append(input("Book status(loan/none): "))
        l1.append(dateinp())

        x = input("Continue (n/y): ")
        if x in ('y', 'Y'):
            break
        else:
            print('Re-enter data!')
            l1 = []
            continue

    try:
        file_students = open("student.csv", 'a', newline='')
    except:
        print('Error Occured while opening file!\nCheck if file is opened in another window!')
        student_add()
    student_writer = csv.writer(file_students)
    for i in (l1):
        student_writer.writerow(i)

    ext = input("Add more entries? (y/n)")
    if ext in ('y', 'Y'):
        student_add()
    else:
        file_students.close()
        return 
        
def student_update():
    '''This function can update student information in the csv file.
    Note: It can only update 'Class' and Book Status! It cannot change student name or admission
    number.'''

    print("UPDATING A EXSISTING ENTRY")
    try:
        file_students = open("student.csv", 'r', newline='')
    except:
        print('Error Occured while opening file!\nCheck if file is opened in another window!')
        student_update()
    file_read = csv.reader(file_students)

    ad = input("Enter Admission no of student: ")
    read = [i for i in file_read]

    for j in read:
        if j[0] == ad:
            print("Name: ", j[1], "\nClass: ", j[2] )
            up = input("Update? (y/n): ")
            if up in ('y', 'Y'):
                what = int(input("Update:\n1. Class\n2. Book Status\n "))
                if what == 1:
                    j[2] = input("Updated Class: ")
            
                if what == 2:
                    while True:     #to ensure correct input of status
                        bs = input("Current Book status(loan/none): ")
                        if bs in ['loan','none']:
                            j[4] = bs
                            break
                        else:
                            print("Enter valid value!")
                            continue
                    j[4] = dateinp()
                
                else:
                    print('Select valid option!')
            else:
                break
    else:
        print('Student not found!')
    
    file_students = open("student.csv", 'w', newline='')
    file_write = csv.writer(file_students)

    file_students.seek(0)
    for x in (read):
        file_write.writerow(x)

    ext = input("Update another student? (y/n)")
    if ext in ('y', 'Y'):
        student_update()
    else:
        file_students.close()
        return

def defaulters():
    '''This function finds students who haven't returned the books in due time.
    Its returns the no of defaulters and their name and class.'''
    try:
        file_students = open(r"C:\Users\abhis\Downloads\students.csv", 'r', newline='')
    except:
        print('Error Occured while opening file!\nCheck if file is opened in another window!')
        defaulters()
    file_read = csv.reader(file_students)

    read = [i for i in file_read]
    defaulterslist = []

    for entry in read:
        date = (entry[4]).split('-')
        try:
            d = datetime(int(date[2]),int(date[1]),int(date[0]))
        except:
            continue
        if d > datetime.today():
            defaulterslist.append(entry)
            continue

    if len(defaulterslist) == 0:
        print('No Defaulters!')

    else:
        print('Number of Defaulters:',len(defaulterslist))
        for ds in defaulterslist:
            print(ds[1], ds[2])

def loanstatus():
    '''This function finds the students who have loaned a book.
    It returns the number of students and their name and class.'''
    
    try:
        file_students = open(r"C:\Users\abhis\Downloads\students.csv", 'r', newline='')
    except:
        print('Error Occured while opening file!\nCheck if file is opened in another window!')
        loanstatus()
    file_read = csv.reader(file_students)

    read = [i for i in file_read]
    loanlist = []

    for entry in read:
        if entry[3] == 'loan':
            loanlist.append(entry)

    print('Number of students who have loaned book:',len(loanlist))

    for stu in loanlist:
        print(stu[1], stu[2])
    
while True:
    print("MAIN MENUE")
    print("--------------------------------------------------------------------------------")

    choice = int(input('''SELECT ONE OF THE FUNCTIONS:
    1.Students Database
    2.Show Defaulters
    3.Loaned Status  
    4.exit
    '''))

    if choice == 1:
        while True:
            print("STUDENTS DATABASE")
            print("--------------------------------------------------------------------------------")
            
            stud = int(input("SELECT ONE OF THE FUNCTIONS: \n1.Update a exsisting entry\n2.Add a new entry\n"))

            if stud == 1:
                student_update()

            elif stud == 2:
                student_add()

            ext2 = input("Return to previous main menu? (y/n): ")
            if ext2 in ("y", 'Y'):
                break
            else:
                 continue
    
    elif choice == 2:
        print("--------------------------------------------------------------------------------")
        defaulters()
        print("--------------------------------------------------------------------------------")

    elif choice == 3:
        print("--------------------------------------------------------------------------------")
        loanstatus()
        print("--------------------------------------------------------------------------------")

    elif choice == 4:
        exit()
