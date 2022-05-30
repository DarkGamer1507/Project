import csv
from datetime import datetime

# defined functions 

def student_book(s):

    # when only the renter of book changes, it updates previous oweners book status and return date

    ad_no = s[5]
    with open("students.csv", 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    for j in read:
        if ad_no == j[0]:
            j[3] = 'none'
            j[4] = 'none'    
    
    with open("students.csv", 'w', newline='') as file2:
        writer = csv.writer(file2)
        for k in read:
            writer.writerow(k)

def verifying_student(s):

    # used to verify if students exists, or has he already rented or has he not
    # also if student has rented mentioned book, it also updates return date

    with open("students.csv", 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    confirm = '0' # to confirm if rented or not or is exists
    for stud in read:
        if stud[0] == s:
            if stud[3].lower() in('none'):
                stud[3] = 'rented' # student hasnt rented
                date = date_format()
                stud[4] = date
                confirm = 'updated'
                break
                
            else:
                confirm = 'rented' # student has rented
                break 

    with open('students.csv', 'w', newline='') as file2:
                    writer = csv.writer(file2)
                    for j in read:
                        writer.writerow(j)

    if confirm == 0:
        return "none","none" # student doesnt exsits in database

    elif confirm in('updated'): # student hasnt rented
        return "break", date

    elif confirm in("rented"): # student has rented
        return "rented", "none"

def book_update():

    # used to update a existing record
    
    print("UPDATING A EXISTING BOOK ENTRY")
    print("-----------------------------------------------------")
    
    with open("books.csv", 'r', newline='') as file_read:
        file_read = csv.reader(file_read)

        S_no = input("Enter Serial Number of book:\n ")
        read = [i for i in file_read]

        book = 0 # to check if mentioned book exists in file

        for j in read:
            if j[0] == S_no:
                book += 1 # book exists in file
                print("Author: ", j[1], "\nName: ", j[2], "\nCurrently: ", j[4] )
                up = input("Update? (y/n):\n ")
                if up in ('y', 'Y'):
                    what = int(input("Update: \n  1.Book Status \n  2.Renter \n  3.Return Date\n"))

                    if what == 1:
                        while True:
                            updated = input("Updated Book Status (available/rented):\n ")
                            if updated.lower() in('available'):
                                student_book(j)
                                j[4] = updated
                                j[5] = 'none'
                                j[6] = 'none'
                                print("\nBook Status Updated!\n")
                                break

                            elif updated.lower() in('rented'):
                                while True:
                                    s = input("Rented by (student's admission number):\n ")
                                    stud1,date1 = verifying_student(s)
                                    if stud1 in('break'):
                                        j[4] = updated
                                        j[5] = s
                                        break
                                    elif stud1 in('none'):
                                        print("\nStudent does not exsits! Try again")
                                        continue
                                    elif stud1 in("rented"):
                                        print("\nStudent already has rented!")
                                        break
                                j[6] = date1
                            else:
                                print("\n Invalid status try again")
                                continue   

                    elif what == 2:
                        while True:
                            s = input("Rented by (student's admission number):\n ")
                            stud2,date2 = verifying_student(s)
                            if stud2 in('break'):
                                student_book(j)
                                j[5] = s
                                break
                            elif stud2 in('none'):
                                print("Student does not exsits! Try again")
                                continue
                            elif stud2 in("rented"):
                                print("\nStudent already has rented!")
                                break
                        j[6] = date2
                        j[4] = 'rented'

                    elif what == 3:
                        dat = date_format()
                        j[6] = dat
                        print("\nReturn Date Updated!\n")

                    else:
                        print("\nSelect a Valid Option!\n")    
                else:
                    break

        if book == 0:
           print("\nBook not found\n")
        
    with open("books.csv", 'w', newline='') as file_write:   
        file_write = csv.writer(file_write)
        for x in (read):
            file_write.writerow(x)

    ext = input("Update another book? (y/n): \n")
    if ext in ('y', 'Y'):
        book_update()
    else:
        return

def book_delete():

    # used to delete a existing record

    print("DELETING A EXISTING BOOK ENTRY")
    print("-----------------------------------------------------")

    with open("books.csv", 'r', newline='') as file1:
        file_read = csv.reader(file1)
            
        S_no = input("Enter Serial number of the book whose entry is to be deleted: ")
        check = 0 # used to check if mentioned book exists in the database
        
        read = [i for i in file_read]

        for j in read:
            if j[0] == S_no:
                check += 1
                print("Author: ", j[1],"\nName: ", j[2]) # to confirm if the serial number entered is correct or not
                con = input("Delete this entry? (y/n) ")
                if con in ('y','Y'):
                    read.remove(j)
                    break
                else:
                    check += 1
                    ext2 = input("\nTry again? (y/n)\n")
                    if ext2 in ('y', 'Y'):
                        check = 'yes'
                        break
                    else:
                        check = 'yes'


        if check == 0:    
            check = 'yes'    
            print("\nBook Not found\n")

    with open("books.csv", 'w', newline='') as file2:
        file_write = csv.writer(file2)
        for k in read:
            file_write.writerow(k)
        if check != 'yes':
            print("\nEntry Deleted!\n ")

    ext = input("Delete another entry? (y/n)")
    if ext in ('y', 'Y'):
        book_delete()
    else:
        return   

def book_add():

    # used for adding a new entry to the book's database

    print("ADDING A NEW BOOK")
    print("-----------------------------------------------------")

    l1 = []
    check = 0 # to confirm if book is added or not

    while True:
        l1.append(input("Serial Number: "))
        l1.append(input("Author: "))
        l1.append(input("Book name: "))
        l1.append(input("Genre: "))
        l1.append(input("Current Book Status (available/rented): "))
        l1.append(input("Rented by (enter students admission no. / none): "))
        l1.append(date_format())

        print("admission number:",l1[0] ,
        "\nName:",l1[1] ,
        "\nClass:",l1[2] ,
        "\nGenre:",l1[3],
        "\nBook Status:",l1[4],
        "\nRented by:" ,l1[5],
        "\nReturn date:",l1[6]) 
        # to make sure correct information has been inputted

        x = input("Continue (n/y): ")

        if x in ('y', 'Y'):
            check += 1
            break
            
        else:
            con = input("\nRe-Enter data? (y/n)\n")
            if con in ('y', 'Y'):
                l1 = []
                continue
            else:
                l1 = []
                break           


    with open("books.csv", 'a', newline='') as file_books:
        book_writer = csv.writer(file_books)
        book_writer.writerow(l1)
    
    if check != 0:
        print("\nBook Added!\n")
        
    cho = input("Add another entry? (y/n) ")
    if cho in ('y','Y'):
        book_add()
        
    else:
        return 
    
def student_rented():

    # to print the list of all students who have rented a book

    with open("students.csv", 'r') as file_read:
        file_reader = csv.reader(file_read)

        read = [i for i in file_reader]
        rented = []
        count = 0

        for ent in read:
            if (ent[3]).lower() == "rented":
                count += 1
                rented.append(ent)

        print("Number of students who have rented a book: ", count)
        
        if count != 0:
            print("List of students who have rented: ")
            for stud in rented:
                print("Name: ", stud[1], "Class: ", stud[2])

def student_defaulter():

    # used to check and print list and number of defaulters

    with open("students.csv", "r") as file_read:
        file_reader = csv.reader(file_read)
        read = [i for i in file_reader]
        defaulter = []    
        count = 0

        for entry in read:
            date = (entry[4]).split('/')
            try: # for checking is return date exists or not
                d = datetime(int(date[2]),int(date[1]),int(date[0])) # converting from dd/mm/yyyy to yyyy/mm/dd
            except:
                continue
            if d < datetime.today():
                defaulter.append(entry)
                count += 1
                continue

    print("Number of defaulters are: ", count)
    
    print("List of defaulters: ")
    if count != 0:
        for stud in defaulter:
            print("Name:",stud[1],"Class:", stud[2],"Return date:", stud[4])

def student_checking(s):

    # used to check if a new added entry already exists in datebase or not

    with open("students.csv", 'r') as file1:
        
        read = csv.reader(file1)
        check = [i for i in read]

        for j in check:
            if j[0] == s[0] and j[2] == s[2]: # if admission number and class of new entry matches an old one
                print("\nThis student already exsits!\n")
                return (1)

        return

def student_delete():

    # used to delete a existing record

    print("DELETING A EXISTING STUDENT ENTRY")
    print("-----------------------------------------------------")

    with open("students.csv", 'r', newline='') as file1:
        file_read = csv.reader(file1)
            
        add_no = input("Enter admission number of the student whose entry is to be deleted: ")
        check = 0 # used to check if mentioned student exists in the database
        
        read = [i for i in file_read]

        for j in read:
            if j[0] == add_no:
                check += 1
                print("Name: ", j[1],"\nClass: ", j[2]) # to confirm if the admission number entered is correct or not
                con = input("Delete this entry? (y/n) ")
                if con in ('y','Y'):
                    read.remove(j)
                    break
                else:
                    check += 1
                    ext2 = input("\nTry again? (y/n)\n")
                    if ext2 in ('y', 'Y'):
                        check = 'yes'
                        break
                    else:
                        check = 'yes'


        if check == 0:    
            check = 'yes'    
            print("\nStudent Not found\n")

    with open("students.csv", 'w', newline='') as file2:
        file_write = csv.writer(file2)
        for k in read:
            file_write.writerow(k)
        if check != 'yes':
            print("\nEntry Deleted!\n ")

    ext = input("Delete another entry? (y/n)")
    if ext in ('y', 'Y'):
        student_delete()
    else:
        return    

def date_format():

    # used to make sure correct format of date is used for further usage

    while True:
        date = input("Enter Return Date (dd/mm/yyyy OR none): ")
        if date.lower() == 'none':
            break

        elif len(date) != 10 or date[2] != '/' or date[5] != '/':
            print("\nEnter Correct Formate date!\n")
            continue
            
        else:
            break

    return date

def student_add():

    # used for adding a new entry to the student's database

    print("ADDING A NEW STUDENT")
    print("-----------------------------------------------------")

    l1 = []
    con2 = 0 # to confirm if student is added or not

    while True:
        l1.append(input("admission Number: "))
        l1.append(input("Name: "))
        l1.append(input("Class: "))
        l1.append(input("Current Book Status (none/rented): "))
        l1.append(date_format())

        print("admission number:",l1[0] ,
        "\nName:",l1[1] ,
        "\nClass:",l1[2] ,
        "\nBook Status:",l1[3], 
        "\nReturn date:",l1[4]) 
        # to make sure correct information has been inputted

        x = input("Continue (n/y): ")

        if x in ('y', 'Y'):
            check = student_checking(l1)
            if check == 1:
                l1 = []
                break
            else:
                con2 += 1
                break
        
        else:
            con = input("\nRe-Enter data? (y/n)\n")
            if con in ('y', 'Y'):
                l1 = []
                continue
            else:
                l1 = []
                break           


    with open("students.csv", 'a', newline='') as file_students:
        student_writer = csv.writer(file_students)
        student_writer.writerow(l1)
    
    if con2 != 0:
        print("\nStudent Added!\n")
        
    cho = input("Add another entry? (y/n) ")
    if cho in ('y','Y'):
        student_add()
        
    else:
        return 
    
def student_update():

    # used to update a existing record
    
    print("UPDATING A EXISTING STUDENT ENTRY")
    print("-----------------------------------------------------")
    
    with open("students.csv", 'r', newline='') as file_read:
        file_read = csv.reader(file_read)

        ad = input("Enter admission Number of student: ")
        read = [i for i in file_read]

        student = 0 # to check if mentioned student exists in file

        for j in read:
            if j[0] == ad:
                student += 1 # student exists in file
                print("Name: ", j[1], "\nClass: ", j[2] )
                up = input("Update? (y/n): ")
                if up in ('y', 'Y'):
                    what = int(input("Update: \n  1.Class \n  2.Book Status \n  3.Return Date\n"))

                    if what == 1:
                       updated = input("Updated Class: ")
                       j[2] = updated
                       print("\nClass Updated!\n")
                       break
                
                    elif what == 2:
                        while True:
                            updated = input("Current Book status (none/rented): ")
                            if updated.lower() in("none"):
                                j[3] = updated
                                j[4] = 'none'
                                print("\nBook Status Updated!\n")
                                break
                            elif updated.lower() in('rented'):
                                j[3] = updated
                                date = date_format()
                                j[4] = date
                                print("\nBook Status Updated!\n")
                                break
                            else:
                                print("\nEnter a Valid Status!\n")
                                continue

                    elif what == 3:
                        dat = date_format()
                        j[4] = dat
                        print("\nReturn Date Updated!\n")

                    else:
                        print("\nSelect a Valid Option!\n")    
                else:
                    break

        if student == 0:
           print("\nStudent not found\n")
        
    with open("students.csv", 'w', newline='') as file_write:   
        file_write = csv.writer(file_write)
        for x in (read):
            file_write.writerow(x)

    ext = input("Update another student? (y/n)")
    if ext in ('y', 'Y'):
        student_update()
    else:
        return

# main program

while True: # to make sure continues running of program
    print("MAIN MENU")
    print("-----------------------------------------------------")

    choice = int(input('''SELECT ONE OF THE FUNCTIONS: 
    1.Students database
    2.Books database
    3.exit
    '''))

    if choice == 1:
        while True:
            print("STUDENTS DATABASE")
            print("-----------------------------------------------------")
            stud = int(input('''SELECT ONE OF THE FUNCTIONS:
            1.Add a new record
            2.Deleting a EXISTING record
            3.Update a EXISTING record
            4.Print list of defaulters
            5.Print list of students who have rented
            6.Return to previous menu
            '''))

            if stud == 1:
                print("-----------------------------------------------------")
                student_add()
                print("-----------------------------------------------------")  
                        

            elif stud == 2:
                print("-----------------------------------------------------")
                student_delete()
                print("-----------------------------------------------------")

            elif stud == 3:
                print("-----------------------------------------------------")
                student_update()
                print("-----------------------------------------------------")

            elif stud == 4:
                print("-----------------------------------------------------")
                student_defaulter()
                print("-----------------------------------------------------")

            elif stud == 5:
                print("-----------------------------------------------------")
                student_rented()
                print("-----------------------------------------------------")

            elif stud == 6:
                print("-----------------------------------------------------")
                break 

            else:
                print("\nSelect a Valid Option!\n")
                continue
    elif choice == 2:
        while True:
            print("BOOKS DATABASE")
            print("-----------------------------------------------------")
            stud = int(input('''SELECT ONE OF THE FUNCTIONS:
            1.Add a new record
            2.Deleting a EXISTING record
            3.Update a EXISTING record
            4.Return to previous menu
            '''))

            if stud == 1:
                print("-----------------------------------------------------")
                book_add()
                print("-----------------------------------------------------")  
                        

            elif stud == 2:
                print("-----------------------------------------------------")
                book_delete()
                print("-----------------------------------------------------")

            elif stud == 3:
                print("-----------------------------------------------------")
                book_update()
                print("-----------------------------------------------------")

            elif stud == 4:
                print("-----------------------------------------------------")
                break 

            else:
                print("\nSelect a Valid Option!\n")
                continue
    elif choice == 3:
        exit()

    else:
        print("\nSelect a Valid Option!\n")
        continue
