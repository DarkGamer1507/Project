l1 = []
l2 = []

x = int(input("Enter the number of elements: "))

for i in range(x):
    l1.append(int(input("Enter element: ")))

n = int(input("Enter how many left shifts: "))

for j in range (n):
    l2.append(l1.pop(0))

l2 = l1+l2

print (l2)
