import csv

def display_flights():
    with open("flight.csv", 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    