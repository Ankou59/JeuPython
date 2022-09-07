from gestiondegats import *

def gestioncombat(joueur, monstre):
    while(joueur[1] > 0 and monstre[1] > 0):
        #combat ?
        monstre[1] = gestiondegats(monstre[1], joueur[2], monstre[3])
        print(f"Le joueur {joueur[0]} attaque : le monstre {monstre[0]} a encore {monstre[1]} points de vie")
        if (monstre[1] > 0):
            joueur[1] = gestiondegats(joueur[1], monstre[2], joueur[3])
            print(f"{monstre[0]} attaque : il reste à {joueur[0]} {joueur[1]} points de vie")
        
    if(joueur[1] > 0):
        print(f"Le joueur a vaincu le monstre {monstre[0]}")

    return joueur