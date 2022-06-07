import csv
from datetime import datetime   

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
       