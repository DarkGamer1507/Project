import csv

def serial_no():
    with open("books.csv", 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    last = read.pop()

    try:
        serial_no = int(last[0])
    except:
        serial_no = 0

    new_no = serial_no + 1

    return new_no