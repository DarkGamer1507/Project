import csv

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
       