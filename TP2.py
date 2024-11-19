# # Fonction pour "entasser" un élément pour maintenir la propriété de TASmax
# def entasser(tableau, n, i):
#     # n est la taille du tas, i est l'index de l'élément à entasser
#     plus_grand = i   # On initialise le plus grand comme étant la racine
#     gauche = 2 * i + 1   # Indice du fils gauche
#     droite = 2 * i + 2   # Indice du fils droit

#     # Vérifier si le fils gauche est plus grand que la racine
#     if gauche < n and tableau[gauche] > tableau[plus_grand]:
#         plus_grand = gauche

#     # Vérifier si le fils droit est plus grand que le plus grand actuel
#     if droite < n and tableau[droite] > tableau[plus_grand]:
#         plus_grand = droite

#     # Si le plus grand n'est pas la racine, échanger et continuer à entasser
#     if plus_grand != i:
#         tableau[i], tableau[plus_grand] = tableau[plus_grand], tableau[i]  # Échange
#         entasser(tableau, n, plus_grand)  # Récursivement entasser le sous-arbre


# ##############################################################################
# # Fonction pour construire un TASmax à partir d'un tableau
# def construire_tas(tableau):
#     n = len(tableau)

#     # Construire le tas (réorganiser le tableau)
#     for i in range(n // 2 - 1, -1, -1):
#         entasser(tableau, n, i)

# # Fonction pour le tri par tas
# def tri_par_tas(tableau):
#     n = len(tableau)

#     # Construire le TASmax
#     construire_tas(tableau)

#     # Extraire les éléments un par un du tas
#     # for i in range(n - 1, 0, -1):
#     #     # Déplacer la racine actuelle à la fin
#     #     tableau[i], tableau[0] = tableau[0], tableau[i]
        
#     #     # Appliquer entasser sur le tas réduit
#     #     entasser(tableau, i, 0)
#     i = n-1
#     while i >= 0 :
#              tableau[i], tableau[0] = tableau[0], tableau[i] 
             
#              entasser(tableau, i, 0)
#              i=i-1
# # Exemple d'utilisation

# tableau = [10, 22, 5, 18, 20, 25, 40, 30, 35, 12]
# print("Tableau initial :", tableau)

# tri_par_tas(tableau)
# print("Tableau trié par tas de Tab de TP :", tableau)
# ################################################33
# # Exemple d'utilisation
tableau = [50, 20, 100, 80, 2, 3, 200, 300]
print("Tableau initial :", tableau)

# tri_par_tas(tableau)
# print("Tableau trié par tas de tab de TD :", tableau)
# print("#"*50)


def tamisser_insertion(tableau, i):
    if tableau[i] <= tableau[i//2] :
       tableau[i], tableau[i//2] = tableau[i//2], tableau[i] 
       tamisser_insertion(tableau, i//2)
       
    # if tableau[i] <= tableau[(i//2)+1] :
    #    tableau[i], tableau[i//2] = tableau[(i//2)+1], tableau[i] 
    #    tamisser_insertion(tableau,(i//2)+1)   
       
     


def insertion_tasmin(tableau, x):
    tableau.append(x)  
    n = len(tableau)
    print("element inserer :", tableau[n - 1])
    tamisser_insertion(tableau, n-1)

print('#' * 50)


insertion_tasmin(tableau, 109)
print('Tableau aprés linsertion  :', tableau)
      
