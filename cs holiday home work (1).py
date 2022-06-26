import csv
from datetime import datetime


def date_format():
    while True:
        date=input("enter date of departure(dd/mm/yyyy):")
        if len(date)!= 10 or date[2]!='/' or date[5]!='/':
            print("enter correct date format")
        else:
            break
    return date

def ticket_no():
    with open("booking.csv",'r',newline='') as file1:
        reader=csv.reader(file1)
        read=[i for i in reader]
    last=read.pop()
    if last==int:
        ticket=int(last[0])
    else:
        ticket=0
    new_no=ticket+1
    return new_no
            
def booking():
    l1=[]
    count=0
    while True:
        l1.append(ticket_no())
        l1.append(input("enter your name:"))
        l1.append(input("how many seats:"))
        while True:
            clas=input("class(eco/buisness):")
            if clas.lower()=='eco' or clas.lower()=='business':
                l1.append(clas)
                break
            else:
                print("select a a valid class")
                continue
        l1.append(date_format())
        l1.append(input("depart from:"))
        l1.append(input("destination:"))
        print("name",l1[1])
        print("no. of seats",l1[2])
        print("class",l1[3])
        print("date of departure",l1[4])
        print("departure place",l1[5])
        print("arrival place",l1[6])

        con=input("continue? (y/n): \n")
        if con in('y','Y'):
            break
        else:
            con2=input("enter your details again?(y/n):")
            if con2 in('y','Y'):
                l1=[]
                continue
            else:
                l1=[] 
                break
    flight_no = flight_ticket(l1)
    if flight_no != 'none':
        l1.append(flight_no)
        count += 1
    else:
        l1= []
        count = 0

    if count != 0:
        with open("booking.csv", 'a', newline="") as file1:
            write = csv.writer(file1)
            write.writerow(l1)

        print("\nTicket Booked!")
        print("\n Your Ticket no. is: ", l1[0])

    conti = input("\nbook another? (y/n)\n")
    if conti in('y','Y'):
        booking()
    else:
        return

def flight_ticket(s):
    with open("flight.csv", 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    count = 0
    ct = 0
    flight = []
    for j in read:
        if j[3] == s[4]:
            if (j[4].lower()) == (s[5].lower()):
                if (j[5].lower()) == (s[6].lower()):
                    if j[2] > s[2]:
                        count += 1
                        flight.append(j)

    
    while ct == 0 and count != 0:
        for k in flight:
            print(k)

        sel = input("\nSelect a flight (enter flight no.): ")

        for ent in flight:
            if ent[0] == sel:
                print ("ok")
                count += 1
                ct += 1
                break
        if ct == 0:
            print("\nSelect a valid flight!\n")    
            


    if count == 0:
        print ("\nNo flight found\n")
        return 'none'   
    
    for l in read:
        if l[0] == sel:
            l[2] = int(l[2]) - int(s[2])
            
    with open("flight.csv" , 'w', newline='') as file2:
        writer = csv.writer(file2)
        for entry in read:
            writer.writerow(entry)       
    
    return sel
    
def flights():
    l2=[]
    while True:
        l2.append(input("airline number:"))
        l2.append(input("airline name:"))
        l2.append(int(input("flight capacity:")))
        l2.append(date_format())
        l2.append(input("starting city:"))
        l2.append(input("arrival city:"))
        print("flight number",l2[0])
        print("flight name",l2[1])
        print("capacity",l2[2])
        print("date of departure",l2[3])
        print("starting city",l2[4])
        print("arrival city",l2[5])

        con=input("continue? (y/n):")
        if con in('y','Y'):
            break
        else:
            con2=input("enter your details again?(y/n):")
            if con2 in('y','Y'):
                l2=[]
                continue
            else:
                l2=[] 
                break
    with open("flight.csv",'a',newline="") as file1:
        write=csv.writer(file1)
        write.writerow(l2)
    conti=input("book another ticket?(y/n):")
    if conti in ('y','Y'):
        flights()
    else:
        return

def cancel():
    with open("booking.csv",'r',newline='') as file1:
        reader=csv.reader(file1)
        read=[i for i in reader]
    ent=[]    
    tick=input("enter your ticket number:")
    check=0
    for entry in read:
        if entry[0]==tick:
            check+=1
            print("name:",entry[1])
            con=input("cancellation of ticket ?(y/n):\n(refund will be generated only before 72 hours before departure time)\n")
            if con in('y','Y'):
                ent = entry
                read.remove(entry)
            else:
                break
    
            
    date=(ent[4]).split('/')
    d=datetime(int(date[2]),int(date[1]),int(int(date[0])-3))
    if  datetime.today()<=d:
        print("refund will be given")
        
    else:
        print("refund is not possible, only ticket can be cancelled")
        
    if check !=0:
        with open("booking.csv",'w',newline='') as file2:
            writer=csv.writer(file2)
            for j in read:
                writer.writerow(j)
        print("ticket cancelled!")
        cancel_(ent)
    if check==0:
        print("no passenger with this ticket found",tick)
    conti=input("cancel another?(y/n)")
    if conti in('y','Y'):
        cancel()
    else:
        return

def cancel_(s):
    with open("flight.csv", 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    for j in read:
        if j[0] == s[7]:
            j[2] = int(j[2]) + int(s[2])

    with open("flight.csv", 'w', newline='') as file2:
        writer = csv.writer(file2)
        for k in read:
            writer.writerow(k)

def flight_update():
    with open("flight.csv",'r',newline='')as file1:
        reader=csv.reader(file1)
        read=[i for i in reader]
    no=input("enter flight no.:\n")
    count=0
    for j in read:
        if j[0]==no:
            count=count+1
            while True:
                op=int(input(''' select what to update:
                1. Date of departure
                2.Starting city
                3. Ending city
                '''))
                if op==1:
                    date=date_format()
                    j[3]=date
                    print("updated date of departure")
                    break
                elif op==2:
                    city=input("eneter the new starting city:\n")
                    j[4]=city
                    print("starting city has been updated")
                    break
                elif op==3:
                    city=input("eneter new ending city:\n")
                    j[4]=city
                    print("ending city is updated")
                    break
                else:
                    print("\nselect a valid choice")
                    continue
        if count==0:
            print("\nFlight not found")
        if count!=0:
            with open("flight.csv",'w',newline='')as file2:
                writer=csv.writer(file2)
                for entry in read:
                    writer.writerow(entry)
        conti=input("\nupdate another?(y/n)")
        if conti in('y','Y'):
            flight_update()
        else:
            return




while True:
    print("SELECT FROM THE FOLLOWING MENU")
    print("-----------------------------------------------------")

    method = int(input('''
    1.booking
    2.flights
    3.cancellation
    4.flight updates
    5.exit
    '''))

    if method == 1:
        print("-----------------------------------------------------")
        booking()
        print("-----------------------------------------------------")

    elif method == 2:
        print("-----------------------------------------------------")
        flights()
        print("-----------------------------------------------------")

    elif method == 3:
        print("-----------------------------------------------------")
        cancel()
        print("-----------------------------------------------------")

    elif method == 4:
        flight_update()

    elif method == 5:
        break

    else:
        print("\nSelect a valid Option!\n")