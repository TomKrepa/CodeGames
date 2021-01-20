def main():
    
    # Initialisation d'un booléen, d'un compteur, d'une liste et sa taille
    switch = True
    count = 0
    tableau = []
    nbr = int(input("Nombre d'éléments\n"))

    # On boucle sur la taille de la liste pour la remplir avec des inputs
    for i in range(nbr):
        tableau.append(int(input("Valeur de l'élément " + str(i+1) + "\n")))

    while switch == True:
        switch = False
        count = count + 1
        for i in range(0, len(tableau) - count):
            if tableau[i] > tableau[i + 1]:
                switch = True
                # On echange les deux elements
                tableau[i], tableau[i + 1] = \
                tableau[i + 1],tableau[i]

    print(tableau)

if __name__ == "__main__":
 main()