import random

texte = " JANKEN"
longueur = len(texte)

symbole1 = "-"
symbole2 = "|"

print(symbole1*(longueur + 21))


print("{0}{1:^2{2}}{0}".format(symbole2, texte, longueur -1))

print(symbole1*(longueur + 21))

choices = ("Pierre", "Feuille", "Ciseaux")

mes_points = 0
ia_points = 0

ask = input("Voulez-vous jouer ?\n\nSi oui, appuyez sur Entree\nSi non, appuyez sur 'n'\n: ")

while mes_points < 3 and ia_points < 3:
    if ask == "n":
        exit()
    a = int(input("\nChoisissez un chiffre :\n0 - Pierre\n1 - Feuille\n2 - Ciseaux\n: "))
    if a > 2:
        print("\nVeuillez choisir un chiffre allant de 0 à 2 svp !")
        continue
    b = random.choice(range(3))
    
    print("\nChoix de l'IA : {}\n\t|| VS ||\nVotre choix : {}\n".format(choices[b],choices[a]))
    if a == b:
        print("Egalite !")
    elif (a > b and b + 1 == a) or (a < b and a + b == 2):
        mes_points += 1
        print("Vous avez gagne !\n\nVotre score : {}\nScore de l'IA : {}".format(mes_points, ia_points))
        
        
    else:
        ia_points += 1
        print("Vous avez perdu !\n\nVotre score : {}\nScore de l'IA : {}".format(mes_points, ia_points))


if mes_points == 3:
    print("\nBravo, vous avez remporte la partie !\n")
elif ia_points == 3:
    print("\nDommage, vous avez perdu, retentez votre chance !\n")

 







    