import random

print("""
-----------------------
Pierre,Feuille,Ciseaux
-----------------------
""")

g="answer"
answerequality="Egalité"
answerlost="Vous avez perdu"
answerwon="Vous avez gagné"
error="Veuillez entrer une valeur valide"

nbround=0
nbroundlost=0
nbroundwon=0
nbroundequality=0

continuer = True
while continuer:
    nbround=nbround+1
    print("Pierre feuille ou ciseaux?")
    userchoice=str(input().lower())
    print("")

    listeordi= ["pierre", "feuille", "ciseaux"]
    computerchoice=random.choice(listeordi)

    computerchoiceremixed = userchoice

    if computerchoice=="pierre" and userchoice.lower() in"pierres" or computerchoice=="ciseaux" and userchoice.lower() in"ciseaux" or computerchoice=="feuille" and userchoice.lower() in"feuilles papiers":
        print("L'ordinateur à choisis: ",computerchoiceremixed," !")
        print("Résultat:")
    elif userchoice.lower() in "pierres" or userchoice.lower() in "ciseaux" or userchoice.lower() in "feuilles" or userchoice.lower() in "papiers":
        print("L'ordinateur à choisis: ",computerchoice," !")
        print("Résultat:")
    elif userchoice.lower()!="pierres" and "ciseaux" and "feuilles" and "papiers": 
        print('veuillez entrer une valeur valide !')
        g=error

    if computerchoice=="pierre" and userchoice.lower() in"pierres" or computerchoice=="ciseaux" and userchoice.lower() in"ciseaux" or computerchoice=="feuille" and userchoice.lower() in"feuilles papiers":
        g=answerequality
        nbroundequality=nbroundequality+1
        print('Egalité')
    elif computerchoice=="pierre" and userchoice.lower() in"ciseaux" or computerchoice=="ciseaux" and userchoice.lower() in"feuilles papiers" or computerchoice=="feuille" and userchoice.lower() in"pierres":
        g=answerlost
        nbroundlost=nbroundlost+1
        print('Vous avez perdu')
    elif computerchoice=="feuille" and userchoice.lower() in"ciseaux" or computerchoice=="ciseaux" and userchoice.lower() in"pierres" or computerchoice=="pierre" and userchoice.lower() in"feuilles papiers":
        g=answerwon
        nbroundwon=nbroundwon+1
        print('Vous avez gagné')

    choix =input("""
Voulez vous continuer ? """)
    
    if choix not in ('o', 'oui', 'ok',"yes","si tu veux"):
        continuer = False
print("""
-----------------------------
INFO SUPPLEMENTAIRE
-----------------------------
""")
if g==error:
    print("Arrêt: sur une érreur")
elif g==answerequality:
    print("Arrêt: sur une égalitée")
elif g==answerlost:
    print("Arrêt: sur une défaite")
elif g==answerwon:
    print("Arrêt: sur une victoire")

print("Nombre de manches totales: -",nbround,"-")
print("Nombre de manches gagnées: ",nbroundwon)
print("Nombre de manches perdues: ",nbroundlost)
print("Nombre de manches égales: ",nbroundequality)
