import csv
from datetime import datetime

# defined functions 

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
        print("NAME  CLASS  RETURN DATE")
        for stud in defaulter:
            print(stud[1], stud[2], stud[4])

def student_checking(s):

    # used to check if a new added entry already exists in datebase or not

    with open("students.csv", 'r') as file1:
        
        read = csv.reader(file1)
        check = [i for i in read]

        for j in check:
            if j[0] == s[0] and j[2] == s[2]: # if addmission number and class of new entry matches an old one
                print("\nThis student already exsits!\n")
                return (1)

        return

def student_delete():

    # used to delete a existing record

    print("DELETING A EXSISTING ENTRY")
    print("--------------------------------------------------------------------------------")

    with open("students.csv", 'r', newline='') as file1:
        file_read = csv.reader(file1)
            
        add_no = input("Enter Addmission number of the student whose entry is to be deleted: ")
        check = 0 # used to check if mentioned student exists in the database
        
        read = [i for i in file_read]

        for j in read:
            if j[0] == add_no:
                check += 1
                print("Name: ", j[1],"\nClass: ", j[2]) # to confirm if the addmission number entered is correct or not
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

    # used to make sure corrent formate of date is used

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

    print("ADDING A NEW ENTRY")
    print("--------------------------------------------------------------------------------")

    l1 = []
    con2 = 0 # to confirm if student is added or not

    while True:
        l1.append(input("Addmission Number: "))
        l1.append(input("Name: "))
        l1.append(input("Class: "))
        l1.append(input("Current Book Status (none/rented): "))
        l1.append(date_format())

        print("Addmission number:",l1[0] ,
        "\nName:",l1[1] ,
        "\nClass:",l1[2] ,
        "\nBook Status:",l1[3], 
        "\nReturn date:",l1[4]) 
        # to make sure corrrect information has been inputed

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
    
    print("UPDATING A EXSISTING ENTRY")
    print("--------------------------------------------------------------------------------")
    
    with open("students.csv", 'r', newline='') as file_read:
        file_read = csv.reader(file_read)

        ad = input("Enter Addmission Number of student: ")
        read = [i for i in file_read]

        student = 0 # to check if mentioned student exsists in file

        for j in read:
            if j[0] == ad:
                student += 1 # student exsists in file
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
                            if updated.lower() in("none", "rented"):
                                j[3] = updated
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
    print("MAIN MENUE")
    print("--------------------------------------------------------------------------------")

    choice = int(input('''SELECT ONE OF THE FUNCTIONS: 
    1.Students database
    3.exit
    '''))

    if choice == 1:
        while True:
            print("STUDENTS DATABASE")
            print("--------------------------------------------------------------------------------")
            stud = int(input('''SELECT ONE OF THE FUNCTIONS:
            1.Add a new record
            2.Deleting a exsisting record
            3.Update a exsisting record
            4.Print list of defaulters
            5.Print list of students who have rented
            6.Return to previous menu
            '''))

            if stud == 1:
                print("--------------------------------------------------------------------------------")
                student_add()
                print("--------------------------------------------------------------------------------")  
                        

            elif stud == 2:
                print("--------------------------------------------------------------------------------")
                student_delete()
                print("--------------------------------------------------------------------------------")

            elif stud == 3:
                print("--------------------------------------------------------------------------------")
                student_update()
                print("--------------------------------------------------------------------------------")

            elif stud == 4:
                print("--------------------------------------------------------------------------------")
                student_defaulter()
                print("--------------------------------------------------------------------------------")

            elif stud == 5:
                print("--------------------------------------------------------------------------------")
                student_rented()
                print("--------------------------------------------------------------------------------")

            elif stud == 6:
                print("--------------------------------------------------------------------------------")
                break 

            else:
                print("\nSelect a Valid Option!\n")
                continue

    elif choice == 3:
        exit()

    else:
        print("\nSelect a Valid Option!\n")
        continue
