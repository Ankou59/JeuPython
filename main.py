from personnages  import *
from compteurkill  import *
from gestioncombat  import *
from creationmob  import *


compteurkill = 0
playagain = 0


while playagain == 0:
    monpersonnage = personnage("Sam", 20,6,3)

    while monpersonnage[1] > 0:
        monstreennemi = creationmob()
        gestioncombat(monpersonnage, monstreennemi)

        if monpersonnage[1] > 0:
            compteurkill = compteurennemistues(compteurkill)
    

    print(f"Le joueur {monpersonnage[0]} a succombé à ses blessures, entrainant avec lui pas moins de {compteurkill} monstres !")

    rejouer = input("Voulez vous rejouer ? [o/n] : ")

    while rejouer != "o" and rejouer != "n":
        rejouer = input("Voulez vous rejouer ? [o/n] : ")
    
    if (rejouer == "o"):
        playagain = 0
    else:
        playagain = 1