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
    flight_no = flight_ticket(l1)
    if flight_no:
        l1.append(flight_no)

    
    with open("booking.csv", 'a', newline="") as file1:
        write = csv.writer(file1)
        write.writerow(l1)

    print("\nTicket Booked!")
    print("\n Your Ticket no. is: ", l1[0])

    conti = input("book another? (y/n)")
    if conti in('y','Y'):
        booking()
    else:
        return

def flight_ticket(s):
    with open("flight.csv", 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]
    
    count = 0
    flight = []
    for j in read:
        if j[3] == s[4] and j[4] == s[5] and j[5] == s[6] and j[2] > s[2]:
            flight.append(j)
    
    while True:
        for k in flight:
            print(k)

        sel = input("Select a flight (enter flight no.):")

        for ent in flight:
            if ent[0] == sel:
                count += 1
                break
        
        if count == 0:
            print("Select a valid flight!")
            continue    
        break    


        
    for l in flight:
        if sel == l[0]:
            l[2] = int(l[2]) - int(s[2])
            return l[0]


# main function
booking()