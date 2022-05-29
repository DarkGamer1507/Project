def pal(s):
    count = 0

    for i in (s):
        if i == i[::-1]:
            count +=1

    return count

l1 = []
l2 = []

x = int(input("Enter the number of elements: "))

for i in range(x):
    l1.append(input("Enter element: "))

n = pal(l1)

print("Number of palindrome of present in the list: ", n)