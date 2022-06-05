import csv

def book_student(s):

    # when the book status of student is updated to 'available' , 
    # it updates rented book's status to availabe

    book_no = s[5]
    with open("books.csv", 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    for j in read:
        if int(book_no) == int(j[0]):
            j[4] = 'available'
            j[5] = 'none'
            j[6] = 'none'    
    
    with open("books.csv", 'w', newline='') as file2:
        writer = csv.writer(file2)
        for k in read:
            writer.writerow(k)