
#Déclaration d'une Variable MAX_WIDTH pour  définir  la largeur maximale
MAX_WIDTH = 100
#Création du Dictionnaire
sentences = {
    "p1":"Le code propre facilite la maintenance",
    "p2":"Tester souvent évite beaucoup d erreurs",
    "p3":"Cette phrase ne doit pas s afficher",
    "p4":"Cette phrase ne doit pas s afficher",
    "p5":"Un bon code doit rester simple et clair",
    "p6":"La simplicité améliore la qualité du code",
    "p7":"Refactoriser améliore la compréhension"
}
#Création de l'ordre des blocs dans un tableau 
units = [
            ["p1"],
            ["p2"],
            ["p5", "p6", "p7"],
        ]
#Déclaration de la fonction qui affichera les blocs
def affichageBlocs(key):
    #Création de la Liste fullLine qui contiendra une Ligne Complète 
    fullLine = [sentences[key].lower() for key in key] 
    #Création de la variable innerWidth qui calculera la largeur de la ligne en fonction de la longueur de la ligne la plus longue
    innerWidth = min(max(len(line) for line in fullLine) + 2, MAX_WIDTH)
    #Création de la Bordure
    border = "+" + "-" * innerWidth + "+"
    #Affichage de la Bordure
    print(border)
    #Pour Chaque ligne Complète
    for line in fullLine:
        #Affichage des Lignes en minuscules 
        cutLine = line[:MAX_WIDTH - 2]
        #Affichage de la Ligne avec une Bordure
        print("| " + cutLine.ljust(innerWidth - 2) + " |")
    #Affichage de la Bordure
    print(border)

#Appel de la fonction affichageBlocs avec pour parametre unit
for i, unit in enumerate(units, start=1):
    affichageBlocs(unit)
    print()
