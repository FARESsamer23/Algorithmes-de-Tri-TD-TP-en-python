# def calculer_frequences_v1(T):
#     n = len(T)
#     for i in range(n):
#         trouve = False
#         j = 0
#         # Vérifier si T[i] a déjà été traité en parcourant les éléments à gauche
#         while j < i and not trouve:
#             if T[i] == T[j]:
#                 trouve = True
#             j += 1

#         # Si l'élément n'a pas été trouvé à gauche, compter sa fréquence
#         if not trouve:
#             frequence = 1
#             for j in range(i + 1, n):
#                 if T[i] == T[j]:
#                     frequence += 1
#             print(f"Fréquence de {T[i]} = {frequence}")

# # Exemple d'utilisation
# T = [3, 1, 3, 2, 1, 4]

# calculer_frequences_v1(T)



# def calculer_frequences_v2(T):
#     n = len(T)
#     for i in range(n):
#         if T[i] != -1:
#             frequence = 1
#             for j in range(i + 1, n):
#                 if T[j] == T[i]:
#                     frequence += 1
#                     T[j] = -1  # Marquer l'élément comme traité
#             print(f"Fréquence de {T[i]} = {frequence}")

# # Exemple d'utilisation
# T = [3, 1, 3, 2, 1, 4]
# calculer_frequences_v2(T)
def calculer_frequences_v3(T):
    # Trouver la valeur maximale dans le tableau
    max_val = max(T)
    
    # Initialiser le tableau de fréquences à 0 pour chaque valeur de 0 à max_val
    frequences = [0] * (max_val + 1)
    
    # Parcourir le tableau pour compter les occurrences de chaque nombre
    for i in range(len(T)):
        frequences[T[i]] += 1
    
    # Afficher les fréquences pour chaque valeur positive rencontrée
    for i in range(1, max_val + 1):
        if frequences[i] > 0:
            print(f"Fréquence de {i} = {frequences[i]}")

# Exemple d'utilisation
T = [3, 1, 3, 2, 1, 4]

calculer_frequences_v3(T)





def tri_rapide(liste, debut, fin):
    # Condition d'arrêt : sous-liste d'un seul élément ou vide
    if debut < fin:
        # Obtenir l'index du pivot après partitionnement
        pivot_index = partition(liste, debut, fin)
        # Trier récursivement les sous-listes à gauche et à droite du pivot
        tri_rapide(liste, debut, pivot_index - 1)
        tri_rapide(liste, pivot_index + 1, fin)

def partition(liste, debut, fin):
    # Choisir le pivot (ici, le dernier élément)
    pivot = liste[fin]
    i = debut - 1

    # Parcourir la sous-liste et comparer chaque élément avec le pivot
    for j in range(debut, fin):
        if liste[j] <= pivot:
            i += 1
            # Échanger les éléments pour placer les plus petits à gauche
            liste[i], liste[j] = liste[j], liste[i]
    
    # Placer le pivot à sa position finale et retourner son index
    liste[i + 1], liste[fin] = liste[fin], liste[i + 1]
    return i + 1

# Exemple d'utilisation
liste = [38, 27, 43, 3, 9, 82, 10]
tri_rapide(liste, 0, len(liste) - 1)
print("Liste triée :", liste)




def tri_fusion(liste):
    # Si la liste a une taille de 1 ou moins, elle est déjà triée
    if len(liste) <= 1:
        return liste

    # Trouver le milieu de la liste
    milieu = len(liste) // 2

    # Diviser la liste en deux moitiés
    partie_gauche = liste[:milieu]
    partie_droite = liste[milieu:]

    # Appliquer le tri de fusion sur chaque moitié
    gauche_triee = tri_fusion(partie_gauche)
    droite_triee = tri_fusion(partie_droite)

    # Fusionner les deux moitiés triées
    return fusion(gauche_triee, droite_triee)

def fusion(gauche, droite):
    liste_triee = []
    i = j = 0

    # Comparer les éléments de chaque moitié et les ajouter à la liste triée
    while i < len(gauche) and j < len(droite):
        if gauche[i] < droite[j]:
            liste_triee.append(gauche[i])
            i += 1
        else:
            liste_triee.append(droite[j])
            j += 1

    # Ajouter les éléments restants
    liste_triee.extend(gauche[i:])
    liste_triee.extend(droite[j:])

    return liste_triee


