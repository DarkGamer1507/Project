import csv

with open("students.csv", 'r+', newline='') as file_students:
    file_read = csv.reader(file_students)
    file_write = csv.writer(file_students)

    ad = input("Enter Addmission Number of student: ")
    read = []

    for i in file_read:
        read.append(i)
    
    for j in read:
        if j[0] == ad:
            print("Name: ", j[1], "\nClass: ", j[2] )
            up = input("Update? (y/n): ")
            if up in ('y', 'Y'):
                what = int(input("Update:\n1. Class\n2. Book Status\n "))
                if what == 1:
                    updated = input("Updated Class: ")
                    j[2] = updated
                    break
                
                else:
                    updated = input("Current Book status: ")
                    j[3] = updated
                    break

            else:
                break
    else:
        print("Student not found")
        
    file_students.seek(0)
    for x in (read):
        file_write.writerow(x)
