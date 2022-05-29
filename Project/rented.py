import csv

def rented():
    with open("students.csv", 'r') as file_read:
        file_reader = csv.reader(file_read)

        read = [i for i in file_reader]
        rented = []
        count = 0

        for ent in read:
            if (ent[3]).lower() == "rented":
                rented.append(ent)

        print("Number of students who have rented a book: ", count)
        print("List of students who have rented: ")
        for stud in rented:
            print("Name: ", stud[1], "Class: ", stud[2])

rented()