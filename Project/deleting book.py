import csv

def book_delete():

    # used to delete a existing record

    print("DELETING A EXSISTING ENTRY")
    print("--------------------------------------------------------------------------------")

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

book_delete() 