import sys
for arg in sys.argv:
    print(arg)
    

marches = int(arg)       
escalier = "#"
espaces = marches 

for marches in range(marches):
    escalier = "#" * (marches + 1)
    espaces -= 1
    print(f" " * espaces + escalier)








   

    
    


    
