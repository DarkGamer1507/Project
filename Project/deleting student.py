import csv

print("DELETING A EXSISTING ENTRY")
with open("students.csv", 'r', newline='') as file1:
    file_read = csv.reader(file1)
        
    add_no = input("Enter Addmission number of the student whose entry is to be deleted: ")
    check = 0
    
    read = [i for i in file_read]

    for j in read:
        if j[0] == add_no:
            check += 1
            print("Name: ", j[1],"\nClass: ", j[2])
            con = input("Delete this entry? (y/n) ")
            if con in ('y','Y'):
                read.remove(j)

            else:
                print("Try again!")

    if check == 0:        
        print("Student Not found")

with open("students.csv", 'w', newline='') as file2:
    file_write = csv.writer(file2)

    for k in read:
        file_write.writerow(k)