import csv

def date_format():
    while True:
        date = input("Enter Return Date (dd/mm/yyyy): ")
        if len(date) != 10 or date[2] != '/' or date[5] != '/':
            print("Enter Correct Formate date!")
            continue
        else:
            break

    return date

def verifying_book(s,p):

    # used to verify if book exists, or is it already rented or is it not
    # also if book is rented mentioned student, it also updates return date

    with open("book.csv", 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    confirm = '0' # to confirm if rented or not or is exists
    for book in read:
        if book[0] == s:
            if book[4].lower() in('available'):
                book[4] = 'rented' # student hasnt rented
                book[5] = p
                date = date_format()
                book[6] = date
                confirm = 'updated'
                break
                
            else:
                confirm = 'rented' # student has rented
                break 

    with open('books.csv', 'w', newline='') as file2:
        writer = csv.writer(file2)
        for j in read:
            writer.writerow(j)

    if confirm == 0:
        return "none","none" # student doesnt exsits in database

    elif confirm == 'updated': # student hasnt rented
        return "break", date

    elif confirm == "rented": # student has rented
        return "rented", "none"