arg = int(input("Please enter a integer : "))

for i in range(1,arg + 1):
    print(" " * (arg - i) + "#" * i)
