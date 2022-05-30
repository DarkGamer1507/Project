import csv

def book_serial_number():
    with open('books.csv', 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    S_no = input("Enter books serial number: ")
    S_no_list = []
    count = 0

    for entry in read:
        if entry[0] in(S_no):
            S_no_list.append(entry)
            count += 1
            break

    if count == 0:
        print("\nBook not found!")
    if count != 0:
        print(S_no_list[2], " by ", S_no_list[1], " \nCurrently: ", S_no_list[4])

    ext = input("\nFind another book? (y/n): ")
    if ext in ("y", 'Y'):
        book_serial_number()
    else:
        return

def book_name():
    with open('books.csv', 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]

    name = input("Enter books name: ")
    name_list = []
    count = 0

    for entry in read:
        if entry[2].lower() == name.lower():
            name_list.append(entry)
            count += 1

    if count == 0:
        print("\nBook not found!")
    if count != 0:
        for ent in name_list:
            print(ent[2], " by ", ent[1], " \nCurrently: ", ent[4])

    ext = input("\nFind another book? (y/n): ")
    if ext in ("y", 'Y'):
        book_name()
    else:
        return

def book_genre():
    with open('books.csv', 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]
    
    genre_list = []
    genre = input("Enter genre: ")
    count = 0

    for entry in read:
        if entry[3].lower() == genre.lower():
            count += 1
            genre_list.append(entry)

    if count == 0:
        print("\nNo books of ",genre," genre found.")
    
    if count != 0:
        print("All the ",genre," books:")
        for ent in genre_list:
            print(ent[2]," by ",ent[1],"\nCurrently:",ent[4],'\n')

    ext = input("\nFind books of another genre? (y/n): ")
    if ext in ("y", 'Y'):
        book_genre()
    else:
        return

def book_author():
    with open('books.csv', 'r', newline='') as file1:
        reader = csv.reader(file1)
        read = [i for i in reader]
    
    author_list = []
    author = input("Enter the name of author: ")
    count = 0

    for entry in read:
        if entry[1].lower() == author.lower():
            count += 1
            author_list.append(entry)

    if count == 0:
        print("\nNo works by ",author," found.")
    
    if count != 0:
        print("All the works by ",author," :")
        for ent in author_list:
            print("Name:",ent[2],"\nCurrently:",ent[4],'\n')

    ext = input("\nFind works by another author? (y/n): ")
    if ext in ("y", 'Y'):
        book_author()
    else:
        return

def book_searching():
    while True:
        print("SEARCHING A BOOK")
        print("-----------------------------------------------------")

        method = int(input('''Select a method to find a book: 
        1.Print a list of all books by a author
        2.Print a list of all books of a genre
        3.Enter book's serial number
        4.Enter book's name
        5.Return to previous menu
        '''))

        if method == 1:
            print("-----------------------------------------------------")
            book_author()
            print("-----------------------------------------------------")

        elif method == 2:
            print("-----------------------------------------------------")
            book_genre()
            print("-----------------------------------------------------")

        elif method == 3:
            print("-----------------------------------------------------")
            book_serial_number()
            print("-----------------------------------------------------")

        elif method == 4:
            print("-----------------------------------------------------")
            book_name()
            print("-----------------------------------------------------")

        elif method == 5:
            break
        else:
            print("\nSelect a valid Option!")

book_searching()