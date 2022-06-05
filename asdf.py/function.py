import csv
from datetime import datetime

def date_format():
    while True:
        date = input("Enter Date of departure (dd/mm/yyyy): ")
        if len(date) != 10 or date[2] != '/' or date[5] != '/':
            print("Enter Correct Formate date!")
            continue
        else:
            break

    return date

def ticket_no():
    with open("booking.csv", 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    last = read.pop()

    ticket = int(last[0])

    new_no = ticket + 1

    return new_no

def booking():
    l1 = []
    while True:
        l1.append(ticket_no())
        l1.append(input("Enter name: "))
        l1.append(input("How many seats: "))
        while True:
            clas = input("Class(eco/first): ")
            if clas.lower() == 'eco' or clas.lower() == 'first':
                l1.append(clas)
                break

            else:
                print("select a valid class!")
                continue
        l1.append(date_format())
        l1.append(input("Starting city: "))
        l1.append(input("Ending city: "))

        print("name:",l1[1])
        print("number of seats:",l1[2])
        print("class:",l1[3])
        print("date of departure:",l1[4])
        print("starting city:",l1[5])
        print("ending city:",l1[6])
        
        con = input("Continue? (y/n): ")
        if con in('y','Y'):
            break
        else:
            con2 = input("Enter details again? (y/n): ")
            if con2 in('y','Y'):
                l1 = []
                continue
            else:
                l1 = []
                break

    with open("booking.csv", 'a', newline="") as file1:
        write = csv.writer(file1)
        write.writerow(l1)

    conti = input("book another? (y/n)")
    if conti in('y','Y'):
        booking()
    else:
        return

def cancel():
    with open("booking.csv", 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    ent = []
    tick = input("Enter ticket number")
    check = 0
    
    for entry in read:
        if entry[0] == tick:
            check += 1
            print("name:", entry[1])
            con = input("cancel ticket? (y/n)\n(refund will be generated only before 72 hrs)\n")
            if con in('y','Y'):    
                ent.append(entry)
                read.remove(entry)
            else:
                break


    for k in ent:
        date = (k[4]).split('/')
    
        d = datetime(int(date[2]),int(date[1]),int(int(date[0]) - 3))
            
        if datetime.today() <= d :
            print("refund is generated")
            break
        else:
            print("refund not possible, ticket will only be cancelled")
            break
        
    if check != 0:
        with open("booking.csv", 'w', newline='') as file2:
            writer = csv.writer(file2)
            for j in read:
                writer.writerow(j)
        print("Ticket Cancelled!")
        
    if check == 0:
        print("no passenger with",tick, "ticket number found")

    conti = input("cancel another? (y/n)")
    if conti in('y','Y'):
        cancel()
    else:
        return
       
# main function

cancel()