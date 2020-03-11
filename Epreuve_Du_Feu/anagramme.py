pr_argument = input("Entrez un mot en minuscule sans caractere spécial : ")
if not pr_argument.isalpha():
    print("Veuillez respecter les consignes svp")
elif pr_argument != pr_argument.lower():
    print("Veuillez entrer un mot en MINUSCULE svp")
    exit()
pr_argument = list(pr_argument)
pr_argument.sort()

dx_argument = input("Entrez un deuxieme mot en respectant les memes consignes : ")
if not dx_argument.isalpha():
    print("Veuillez respecter les consignes svp")
elif dx_argument != dx_argument.lower():
    print("Veuillez entrer un mot en MINUSCULE svp")
    exit()
dx_argument = list(dx_argument)
dx_argument.sort()

if pr_argument == dx_argument:
    print("Ces mots sont des anagrammes")
else:
    print("Ces mots ne sont pas des anagrammes")





