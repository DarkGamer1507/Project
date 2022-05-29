import csv
from datetime import datetime

def student_defaulter():
    with open("students.csv", "r") as file_read:
        file_reader = csv.reader(file_read)
        read = [i for i in file_reader]
        defaulter = []    

        for entry in read:
            date = (entry[4]).split('-')
            try:
                d = datetime(int(date[2]),int(date[1]),int(date[0]))
            except:
                continue
            if d > datetime.today():
                defaulter.append(entry)
                continue


    print(defaulter)

student_defaulter()
