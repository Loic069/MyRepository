import sys
for my_str in sys.argv:
    print(my_str)

my_str = input("Entrez une phrase :")


argument = my_str
resultat = ""
liste = list(argument)
i = 0
for i in range(len(liste)): 
    if i % 2 == 0:
        resultat += liste[i].lower()
    else: 
        resultat += liste[i].upper()

    
print(resultat)




