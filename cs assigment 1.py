
def add():
    file = open('records.txt', 'a')
    while True:
        file.write(input("Enter name: "))
        file.write(',')
        file.write(input("Enter class: "))
        file.write(',')
        file.write(input("Enter percentage: "))
        file.write(',')
        file.write(' \n')

        ch = input("add more records? (n/y)")
        if ch.lower() == 'n':
            break
    
    file.close()

def display():
    file = open('records.txt', 'r')
    read = file.readlines()
    print("NAME,CLASS,PERCENTAGE")
    
    for i in read:
        print(i)

    file.close()

def count_rec():
    file = open('records.txt', 'r')
    read = file.readlines()
    
    print('Number of lines present in the file is: ',len(read))

    file.close()

def search_1():
    file = open('records.txt','r')
    read = file.read()

    word = input("Enter what word to search for: ")
    
    ct = read.count(word + ',') #to make sure it doesnt count it as a part of another word
    
    print("The word appears",ct,'times')

    file.close()

def search_2():
    file = open('records.txt','r')
    read = file.read()

    ct = 0

    for i in read:
        if i.isalpha() == False:
            if i != '\n':
                if i != ',':
                    ct += 1
            
    print("Number of digits,special characters present in file: ",ct)
    
    file.close()


while True:    
    choice = int(input('''Select one of the following: :
        1. Add records to the file
        2. Display all contents of the file
        3. Count the number of lines in the file
        4. Search and count the number of times a particular word appears in the file
        5. Count the number of digits and special characters in the file
        6. exit
        '''))

    if choice == 1:
        print("-----------------------------------------------------")
        add()
        print("-----------------------------------------------------")

    elif choice == 2:        
        print("-----------------------------------------------------")
        display()
        print("-----------------------------------------------------")

    elif choice == 3:
        print("-----------------------------------------------------")
        count_rec()
        print("-----------------------------------------------------")

    elif choice == 4:
        print("-----------------------------------------------------")
        search_1()
        print("-----------------------------------------------------")

    elif choice == 5:
        print("-----------------------------------------------------")
        search_2()
        print("-----------------------------------------------------")

    elif choice == 6:
        break
    else:
        print("Select a valid function!")