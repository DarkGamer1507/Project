import csv

def new_user():
    with open("user.csv","a",newline="") as f: 
        csv.read = csv.reader(f)
        for i in csv.read:
            print(i)
        try:
            user = [i for i in read]
        except:
            id = 0

    for i in user:
        print (i)
    if id != 0:
        id = user[0] + 1

    nam = input("Enter name:    ")

    score = 0

    n_user = [id,nam,score]

    with open('user.csv', 'a', newline = '') as f:
        write = csv.writer(f)
        write.writerow(n_user)

new_user()