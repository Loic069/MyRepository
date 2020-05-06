a = []
number = int(input("Please enter the total number of items : "))
for i in range(number):
    value = int(input("Please enter the %d item from your list : " %i))
    a.append(value)

for i in range(number -1):
    for j in range(number - i - 1):
        if(a[j] < a[j + 1]):
             temp = a[j]
             a[j] = a[j + 1]
             a[j + 1] = temp

print("The list sorted in descending order is : ", a)
