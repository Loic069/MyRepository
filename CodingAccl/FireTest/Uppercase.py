string = input("Enter a string : ")
position = 0
char = 0

while position < len(string):
    if string[position] == " ":
        print(" ",end="")
        position += 1
    if char % 2 == 0:
        print(string[position].upper(),end="")
        char += 1
    else:
        print(string[position].lower(),end="")
        char += 1
    position += 1

print(" ")
