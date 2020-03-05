import sys

def factorielle(n):
    if n == 1:
        return n
    else:
        return n * factorielle(n-1)

n = int(input("Entrez un nombre: "))
if n < 0:
    print("Factoriel ne peut être trouvé pour les nombres négatifs")
elif n == 0:
    print("Factorielle de 0 est 1")
else:
    print("Factorielle de", n, "est: ", factorielle(n))


