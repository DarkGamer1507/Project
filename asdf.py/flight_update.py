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

def flight_update():
    with open("flight.csv", 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    no = input("Enter flight no.: \n")
    count = 0
    for j in read:
        if j[0] == no:
            print("FLight name:",j[1])
            count += 1
            while True:
                op = int(input('''Select what to update:
                1.Date of departure
                2.Starting city
                3.Ending city
                '''))

                if op == 1:
                    date = date_format()
                    j[3] = date
                    print("Date of departure updated!")
                    break

                elif op == 2:
                    city = input("Enter new starting city:\n")
                    j[4] = city
                    print("Starting city updated!")
                    break

                elif op == 3:
                    city = input("Enter new ending city:\n")
                    j[4] = city
                    print("ending city updated!")
                    break

                else:
                    print("\nselect a valid function!")
                    continue

    if count == 0:
        print("\nFlight not found")

    if count != 0:
        with open("flight.csv", 'w', newline='') as file2:
            writer = csv.writer(file2)
            for entry in read:
                writer.writerow(entry)

    conti = input("\nupdate another? (y/n)")
    if conti in('y','Y'):
        flight_update()
    else:
        return
 

flight_update()