import csv

def student_book(s):
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

def date_format():

    # used to make sure corrent formate of date is used for futher usage

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

def verifying_student(s):
    with open("students.csv", 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    confirm = '0'
    for stud in read:
        if stud[0] == s:
            if stud[3].lower() in('none'):
                stud[3] = 'rented'
                date = date_format()
                stud[4] = date
                confirm = 'updated'
                break
                
            else:
                confirm = 'rented'
                break 

    with open('students.csv', 'w', newline='') as file2:
                    writer = csv.writer(file2)
                    for j in read:
                        writer.writerow(j)

    if confirm == 0:
        return "none","none"
    elif confirm in('updated'):
        return "break", date
    elif confirm in("rented"):
        return "rented", "none"

def book_update():

    # used to update a existing record
    
    print("UPDATING A EXSISTING BOOK ENTRY")
    print("--------------------------------------------------------------------------------")
    
    with open("books.csv", 'r', newline='') as file_read:
        file_read = csv.reader(file_read)

        S_no = input("Enter Serial Number of book:\n ")
        read = [i for i in file_read]

        book = 0 # to check if mentioned book exsists in file

        for j in read:
            if j[0] == S_no:
                book += 1 # book exsists in file
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
                                    s = input("Rented by (student's addmission number):\n ")
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
                            s = input("Rented by (student's addmission number):\n ")
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

book_update()