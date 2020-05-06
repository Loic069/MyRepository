first_arg = input("Enter a lowercase word without special characters : ")
if not first_arg.isalpha():
    print("Please respect the instructions")
elif first_arg != first_arg.lower():
    print("Please enter a LOWERCASE word")
    exit()
first_arg = list(first_arg)
first_arg.sort()

second_arg = input("Enter a second word following the same instructions : ")
if not second_arg.isalpha():
    print("Please respect the instructions")
elif second_arg != second_arg.lower():
    print("Please enter a LOWERCASE word")
    exit()
second_arg = list(second_arg)
second_arg.sort()

if first_arg == second_arg:
    print("These words are anagrams")
else:
    print("These words aren't anagrams")
