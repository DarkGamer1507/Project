import csv

def date_format():
    while True:
        date = input("Enter Date of departure (dd/mm/yyyy): ")
        if len(date) != 10 or date[2] != '/' or date[5] != '/':
            print("Enter Correct Formate date!")
            continue
        else:
            break

    return date

def flight():
    l1 = []
    while True:
        l1.append(input("Flight number: "))
        l1.append(input("Flight name: "))
        l1.append(int(input("Flight Capacity ")))
        l1.append(date_format())
        l1.append(input("Starting city: "))
        l1.append(input("Ending city: "))

        print("Flight number:",l1[0])
        print("Flight name:",l1[1])
        print("Capcity:",l1[2])
        print("date of departure:",l1[3])
        print("starting city:",l1[4])
        print("end city:",l1[5])
        
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

    with open("flight.csv", 'a', newline="") as file1:
        write = csv.writer(file1)
        write.writerow(l1)

    conti = input("enter another entry for a flight? (y/n)")
    if conti in('y','Y'):
        flight()
    else:
        return
flight()