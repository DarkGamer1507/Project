import csv

def ticket_no():
    with open("booking.csv", 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    last = read.pop()

    ticket = int(last[0])

    new_no = ticket + 1

    return new_no