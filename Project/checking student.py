import csv

def student_checking(s):
    print("hello")
    print(s)
    with open("students.csv", 'r') as file1:
        
        read = csv.reader(file1)
        check = [i for i in read]

    for j in check:

        if j[0] == s[0]:
            print("\nThis student already exsits!\n")
            return (1)

print("\nADDING A NEW ENTRY\n")
print("--------------------------------------------------------------------------------")

l1 = []
con2 = 0 # to confirm if student is added or not

while True:
    l1.append(input("Addmission Number: "))
    l1.append(input("Name: "))
    l1.append(input("Class: "))
    l1.append(input("Current Book Status (none/rented): "))
    

    print("Addmission number:",l1[0] ,
    "\nName:",l1[1] ,
    "\nClass:",l1[2] ,
    "\nBook Status:",l1[3]) 
    # to make sure corrrect information has been inputed

    x = input("Continue (n/y): ")

    check = student_checking(l1)
    if check == 1:
        break
    else:
        pass

    if x in ('y', 'Y'):
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
    
