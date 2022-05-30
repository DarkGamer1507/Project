import csv

def book_add():

    # used for adding a new entry to the book's database

    print("ADDING A NEW BOOK")
    print("--------------------------------------------------------------------------------")

    l1 = []
    check = 0 # to confirm if book is added or not

    while True:
        l1.append(input("Serial Number: "))
        l1.append(input("Author: "))
        l1.append(input("Book name: "))
        l1.append(input("Genre: "))
        l1.append(input("Current Book Status (available/rented): "))
        l1.append(input("Rented by (enter students addmission no. / none): "))

        print("Addmission number:",l1[0] ,
        "\nName:",l1[1] ,
        "\nClass:",l1[2] ,
        "\nGenre:",l1[3],
        "\nBook Status:",l1[4],
        "\nRented by:" ,l1[5],) 
        # to make sure corrrect information has been inputed

        x = input("Continue (n/y): ")

        if x in ('y', 'Y'):
            check += 1
            break
            
        else:
            con = input("\nRe-Enter data? (y/n)\n")
            if con in ('y', 'Y'):
                l1 = []
                continue
            else:
                l1 = []
                break           


    with open("books.csv", 'a', newline='') as file_books:
        book_writer = csv.writer(file_books)
        book_writer.writerow(l1)
    
    if check != 0:
        print("\nBook Added!\n")
        
    cho = input("Add another entry? (y/n) ")
    if cho in ('y','Y'):
        book_add()
        
    else:
        return 
    

book_add()