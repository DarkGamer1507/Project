import csv

l1 = []
l2 = []

while True:
    l1.append(input("Addmission Number: "))
    l1.append(input("Name: "))
    l1.append(input("Class: "))
    l1.append("none")

    l2.append(l1)
    l1 = []

    x = input("Continue (n/y): ")
    if x in ('n', 'N'):
        break
    else:
        continue

with open("students.csv", 'a', newline='') as file_students:
    student_writer = csv.writer(file_students)
    for i in (l2):
        student_writer.writerow(i)