import sys

a = []
number = int(input("Veuillez entrer le nombre total d'elements : "))
for i in range(number):
    value = int(input("Veuillez entrer l'element %d de votre liste : " %i))
    a.append(value)

for i in range(number -1):
    for j in range(number - i - 1):
        if(a[j] < a[j + 1]):
             temp = a[j]
             a[j] = a[j + 1]
             a[j + 1] = temp

print("La liste triee par ordre decroissant est : ", a)