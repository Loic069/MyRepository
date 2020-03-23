import random

nombre_mystere = random.randint(0, 30)
nombre_essais = 5
essais = 0
tentatives = 0
nb_2 = 5

while essais < nombre_essais:
    nombre = input("Quel est le nombre mystère ? : ")


    if not nombre.isdigit():
        print("SVP, entrez un nombre valide.")
        nb_2 -= 1
        tentatives += 1
        essais += 1
        print("Il vous reste {} essais !".format(nb_2))
        continue    
    nombre = int(nombre)

    if nombre > nombre_mystere:
        nb_2 -= 1
        print("Le nombre mystère est plus petit que {}, il vous reste {} essais !".format(nombre, nb_2))
    elif nombre < nombre_mystere:
        nb_2 -= 1
        print("Le nombre mystère est plus grand que {}, il vous reste {} essais !".format(nombre, nb_2))
    elif nombre == nombre_mystere:
        tentatives += 1
        print("Bravo, vous avez trouvé le nombre mystère en {} essais !".format(tentatives))
        exit()
    
    tentatives += 1
    essais += 1

print(f"Vous avez perdu. Le nombre mystère était {nombre_mystere}")


