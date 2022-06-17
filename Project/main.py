import csv
from datetime import datetime

# defined functions 

def book_rented():

    # used to print the list of all rented books

    with open("books.csv", 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    count = 0 # to check if any book is rented at all or not
    rented = []
    for ent in read:
        if ent[4] == 'rented':
            count += 1
            rented.append(ent)

    if count == 0:
        print("\nNo book is currently rented")

    if count!= 0:
        print("\nList of all rented books: \n")
        for entry in rented:
            print(entry[2],' by ', entry[1],"\nRented by:",entry[5],'\nReturn date: ',entry[6] )

def book_checking(s):

    # used to check if a new added entry already exists in datebase or not

    with open("books.csv", 'r') as file1:
        
        read = csv.reader(file1)
        check = [i for i in read]

        for j in check:
            if j[1] == s[1] and j[2] == s[2]: # if author and book name of new entry matches an old one
                print("\nThis book already exsits!\n")
                return (1)

        return

def book_serial_number():

    # to find a book by its serial number

    with open('books.csv', 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    S_no = input("Enter books serial number: ")
    S_no_list = []
    count = 0 # to check if book exists or not

    for entry in read:
        if entry[0] in(S_no):
            S_no_list.append(entry)
            count += 1
            break

    if count == 0:
        print("\nBook not found!")
        
    if count != 0:
        print(S_no_list[2], " by ", S_no_list[1], " \nCurrently: ", S_no_list[4])

    ext = input("\nFind another book? (y/n): ")
    if ext in ("y", 'Y'):
        book_serial_number()
    else:
        return

def book_name():

    # to find a book by its name

    with open('books.csv', 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    name = input("Enter books name: ")
    name_list = []
    count = 0 # to check if book exists or not

    for entry in read:
        if entry[2].lower() == name.lower():
            name_list.append(entry)
            count += 1

    if count == 0:
        print("\nBook not found!")

    if count != 0:
        for ent in name_list:
            print("S.no:",ent[0],ent[2], " by ", ent[1], " \nCurrently: ", ent[4])

    ext = input("\nFind another book? (y/n): ")
    if ext in ("y", 'Y'):
        book_name()
    else:
        return

def book_genre():

    # used to print the list of all books of a genre

    with open('books.csv', 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]
    
    genre_list = []
    genre = input("Enter genre: ")
    count = 0 # to check if books of a genre exists or not

    for entry in read:
        if entry[3].lower() == genre.lower():
            count += 1
            genre_list.append(entry)

    if count == 0:
        print("\nNo books of ",genre," genre found.")
    
    if count != 0:
        print("\nAll the ",genre," books:")
        for ent in genre_list:
            print("S.no:",ent[0],ent[2]," by ",ent[1],"\nCurrently:",ent[4],'\n')

    ext = input("\nFind books of another genre? (y/n): ")
    if ext in ("y", 'Y'):
        book_genre()
    else:
        return

def book_author():

    # used to print the list of all the books of a author

    with open('books.csv', 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]
    
    author_list = []
    author = input("Enter the name of author: ")
    count = 0 # to check if any books by the mentioned author exists or not

    for entry in read:
        if entry[1].lower() in (author.lower()): # because python is case sensitive
            count += 1
            author_list.append(entry)

    if count == 0:
        print("\nNo works by ",author," found.")
    
    if count != 0:
        print("\nAll the works by ",author," :\n")
        for ent in author_list:
            print("S.no:",ent[0],"Name:",ent[2],"\nCurrently:",ent[4],'\n')

    ext = input("\nFind works by another author? (y/n): ")
    if ext in ("y", 'Y'):
        book_author()
    else:
        return

def book_searching():

    # used for searching a book from book's database

    while True:
        print("SEARCHING A BOOK")
        print("-----------------------------------------------------")

        method = int(input('''Select a method to find a book: 
        1.Print a list of all books by a author
        2.Print a list of all books of a genre
        3.Enter book's serial number
        4.Enter book's name
        5.Return to previous menu
        '''))

        if method == 1:
            print("-----------------------------------------------------")
            book_author()
            print("-----------------------------------------------------")

        elif method == 2:
            print("-----------------------------------------------------")
            book_genre()
            print("-----------------------------------------------------")

        elif method == 3:
            print("-----------------------------------------------------")
            book_serial_number()
            print("-----------------------------------------------------")

        elif method == 4:
            print("-----------------------------------------------------")
            book_name()
            print("-----------------------------------------------------")

        elif method == 5:
            break
        else:
            print("\nSelect a valid Option!\n")

def book_student(s):

    # when the book status of student is updated to 'available' ,it updates rented book's status to availabe
    # also used to update book when only rented book is changed

    book_no = s[5]
    with open("books.csv", 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    for j in read:
        if book_no == j[0]:
            j[4] = 'available'
            j[5] = 'none'
            j[6] = 'none'    
    
    with open("books.csv", 'w', newline='') as file2:
        writer = csv.writer(file2)
        for k in read:
            writer.writerow(k)

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
            j[5] = 'none'
    
    with open("students.csv", 'w', newline='') as file2:
        writer = csv.writer(file2)
        for k in read:
            writer.writerow(k)

def verifying_book(s,p):

    # used to verify if book exists, or is it already rented or is it not
    # also if book is rented mentioned student, it also updates return date

    with open("books.csv", 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    confirm = 0 # to confirm if rented or not or is exists
    for book in read:
        if book[0] == s:
            if book[4].lower() in('available'):
                book[4] = 'rented' # book isnt rented
                book[5] = p
                date = date_format()
                book[6] = date
                confirm = 'updated'
                break
                
            else:
                confirm = 'rented' # book is rented
                break 

    with open('books.csv', 'w', newline='') as file2:
        writer = csv.writer(file2)
        for j in read:
            writer.writerow(j)

    if confirm == 0:
        return 0, 0 # book doesnt exsits in database

    elif confirm == 'updated': # book isnt rented
        return 1 , date

    elif confirm == "rented": # book is rented
        return 3 , "none"

def verifying_student(s,p):

    # used to verify if students exists, or has he already rented or has he not
    # also if student has rented mentioned book, it also updates return date

    with open("students.csv", 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    confirm = 0 # to confirm if rented or not or is exists
    for stud in read:
        if stud[0] == s:
            if stud[3].lower() in('none'):
                stud[3] = 'rented' # student hasnt rented
                date = date_format()
                stud[4] = date
                stud[5] = p
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

    elif confirm == 'updated': # student hasnt rented
        return "break", date

    elif confirm == "rented": # student has rented
        return "rented", "none"

def book_update():

    # used to update a existing record
    
    print("UPDATING A EXISTING BOOK ENTRY")
    print("-----------------------------------------------------")
    
    with open("books.csv", 'r', newline='') as file_read:
        file_read = csv.reader(file_read)
        read = [i for i in file_read]

    book = 0 # to check if mentioned book exists in file
    S_no = input("Enter Serial Number of book:\n ")
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
                            if j[4] == 'rented': # in case the user tries to change book status from rented to rented
                                print("\n!Book is already rented (to change renter use renter function)")
                                break
                            else:
                                s = input("Rented by (student's admission number):\n ")
                                stud1,date1 = verifying_student(s,j[0])
                                if stud1 in('break'):
                                    student_book(j)
                                    j[4] = updated
                                    j[5] = s
                                    j[6] = date1
                                    print("\nBook Status Updated!\n")
                                    break
                                elif stud1 in('none'):
                                    print("\nStudent does not exsits! Try again")
                                    continue
                                elif stud1 in("rented"):
                                    print("\nStudent already has rented!")
                                    break
                            
                        else:
                            print("\n Invalid status try again")
                            continue   

                elif what == 2:
                    while True:
                        s = input("Rented by (student's admission number):\n ")
                        stud2,date2 = verifying_student(s,j[0])
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

    if book != 0:    
        with open("books.csv", 'w', newline='') as file_write:   
            file_write = csv.writer(file_write)
            for x in (read):
                file_write.writerow(x)
        print("\nBook updated!\n")

    ext = input("\nUpdate another book? (y/n): ")
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
        read = [i for i in file_read]

    S_no = input("Enter Serial number of the book whose entry is to be deleted: ")
    check = 0 # used to check if mentioned book exists in the database
    for j in read:
        if j[0] == S_no:
            check += 1
            print("Author: ", j[1],"\nName: ", j[2]) # to confirm if the serial number entered is correct or not
            con = input("Delete this entry? (y/n): ")
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

    if check != 'yes':
        with open("books.csv", 'w', newline='') as file2:
            file_write = csv.writer(file2)
            for k in read:
                file_write.writerow(k)
        print("\nEntry Deleted!\n ")

    ext = input("Delete another entry? (y/n): ")
    if ext in ('y', 'Y'):
        book_delete()
    else:
        return   

def serial_no():

    #   used to automatically give a new book a serial number
    #   it is used in order to aviod two books having the same serial number

    with open("books.csv", 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    last = read.pop()   #   takes the last entry of book's database

    try: # to check if there is a last entry or not
        serial_no = int(last[0]) 
    except:
        serial_no = 0

    new_no = serial_no + 1

    return new_no

def book_add():

    # used for adding a new entry to the book's database

    print("ADDING A NEW BOOK")
    print("-----------------------------------------------------")

    l1 = []
    check = 0 # to confirm if book is added or not

    while True:
        l1.append(serial_no())
        l1.append(input("Author: "))
        l1.append(input("Book name: "))
        l1.append(input("Genre: "))
        l1.append('available')
        l1.append('none')       #by default a new entry hasnt been rented by anyone at the time of adding the entry
        l1.append('none')

        print("\nSerial number:",l1[0] ,
        "\nName:",l1[1] ,
        "\nClass:",l1[2] ,
        "\nGenre:",l1[3],
        "\nBook Status:",l1[4],
        "\nRented by:" ,l1[5],
        "\nReturn date:",l1[6],
        "\n(by default a new book is not rented by anyone)") 
        # to make sure correct information has been inputted

        x = input("\nContinue (n/y): ")

        if x in ('y', 'Y'):
            check1 = book_checking(l1) # to check if the book already exists in database or not
            if check1 == 1:
                l1 = []
                break
            else:
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

    if check != 0:
        with open("books.csv", 'a', newline='') as file_books:
            book_writer = csv.writer(file_books)
            book_writer.writerow(l1)
        print("\nBook Added!\n")
        
    cho = input("\nAdd another entry? (y/n): ")
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
    count = 0 # to count number of people who have rented a book
    for ent in read:
        if (ent[3]).lower() == "rented":
            count += 1
            rented.append(ent)

    print("\nNumber of students who have currently rented a book: ", count)
    
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
    count = 0 # to check number of defaulters
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

    print("\nNumber of defaulters are: ", count)
    
    if count != 0:
        print("List of defaulters: ")
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
        read = [i for i in file_read]
        
    add_no = input("Enter admission number of the student whose entry is to be deleted: ")
    check = 0 # used to check if mentioned student exists in the database
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

    if check != 'yes':
        with open("students.csv", 'w', newline='') as file2:
            file_write = csv.writer(file2)
            for k in read:
                file_write.writerow(k)
                print("\nEntry Deleted!\n ")

    ext = input("\nDelete another entry? (y/n): ")
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
            print("\nEnter Correct Format date!\n")
            continue
            
        else:
            break

    return date

def student_add():

    # used for adding a new entry to the student's database

    print("\nADDING A NEW STUDENT")
    print("-----------------------------------------------------")

    l1 = []
    con2 = 0 # to confirm if student is added or not

    while True:
        l1.append(input("admission Number: "))
        l1.append(input("Name: "))
        l1.append(input("Class: "))
        l1.append('none')             
        l1.append('none')      #by default a new entry has no book rented 
        l1.append('none')


        print("Admission number:",l1[0] ,
        "\nName:",l1[1] ,
        "\nClass:",l1[2] ,
        "\nBook Status:",l1[3], 
        "\nRented book:",l1[5],
        "\nReturn date:",l1[4],
        "\n(by default new entries have no rented book)") 
        # to make sure correct information has been inputted

        x = input("\nContinue (n/y): ")

        if x in ('y', 'Y'):
            check = student_checking(l1) # to make sure new student is already not added
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
        
    cho = input("\nAdd another entry? (y/n): ")
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
        read = [i for i in file_read]

    ad = input("Enter admission Number of student:\n")
    student = 0 # to check if mentioned student exists in file

    for j in read:
        if j[0] == ad:
            student += 1 # student exists in file
            print("Name: ", j[1], "\nClass: ", j[2] )
            up = input("\nUpdate? (y/n): ")
            if up in ('y', 'Y'):
                print("\nCurrent class:",j[2],"\nCurrent Book status:",j[3],"\nCurrently rented book:",j[5],"\nCurrent return date:",j[4],'\n')
                what = int(input("Update: \n  1.Class \n  2.Book Status \n  3.Rented Book\n  4.Return Date\n  "))

                if what == 1:
                    updated = input("Updated Class: ")
                    j[2] = updated
                    print("\nClass Updated!\n")
                    break
            
                elif what == 2:
                    while True:
                        updated = input("Current Book status (none/rented): ")
                        if updated.lower() in("none"):
                            book_student(j)
                            j[3] = updated
                            j[4] = 'none'
                            j[5] = 'none'
                            print("\nBook Status Updated!\n")
                            break

                        elif updated.lower() in('rented'):
                            s = input("Rented book (book's serial number):\n ")
                            stud1,date1 = verifying_book(s,j[0])
                            if stud1 == 1:
                                book_student(j)
                                j[3] = updated
                                j[5] = s
                                j[4] = date1
                                print("\nBook Status Updated!\n")
                                break
                            elif stud1 == 0:
                                print("\nBook does not exsits! Try again")
                                continue
                            elif stud1 == 3:
                                print("\nBook is already rented!")
                                break

                        else:
                            print("\nEnter a Valid Status!\n")
                            continue

                elif what == 3:
                    s = input("Rented book (book's serial number):\n ")
                    stud2,date2 = verifying_book(s,j[0])
                    if stud2 == 1:
                        book_student(j)
                        j[3] = 'rented'
                        j[5] = s
                        j[4] = date2
                        print("\nBook Status Updated!\n")
                        break
                    elif stud2 == 0:
                        print("\nBook does not exsits! Try again")
                        continue
                    elif stud2 == 3:
                        print("\nBook is already rented!")
                        break
                
                elif what == 4:
                    j[4] = date_format()
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

    ext = input("\nUpdate another student? (y/n)")
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
    3.Exit
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
            book = int(input('''SELECT ONE OF THE FUNCTIONS:
            1.Add a new record
            2.Deleting a existing record
            3.Update a existing record
            4.Search a book/books
            5.To print the list of all rented books
            6.Return to previous menu
            '''))

            if book == 1:
                print("-----------------------------------------------------")
                book_add()
                print("-----------------------------------------------------")  
                        

            elif book == 2:
                print("-----------------------------------------------------")
                book_delete()
                print("-----------------------------------------------------")

            elif book == 3:
                print("-----------------------------------------------------")
                book_update()
                print("-----------------------------------------------------")

            elif book == 4:
                print("-----------------------------------------------------")
                book_searching()
                print("-----------------------------------------------------")

            elif book == 5:
                print("-----------------------------------------------------")
                book_rented()
                print("-----------------------------------------------------")

            elif book == 6:
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
