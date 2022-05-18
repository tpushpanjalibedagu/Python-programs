# input of list
li = []
n = int(input("Enter size of list "))
for i in range(0, n):
    num = int(input("Enter element of list "))
    li.append(num)

print("Positive numbers in" + str(li) + "are: ")

# traversing
for i in li:
    if i >= 0:
        print(i, end=" ")
