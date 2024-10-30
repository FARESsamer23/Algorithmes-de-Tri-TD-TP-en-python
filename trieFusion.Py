def fusion_A(T1, T2):
    T3 = T1.copy()  # On initialise T3 avec les éléments de T1
    for x in T2:  # Pour chaque élément dans T2
        i = 0
        # Trouver l'endroit où insérer x dans T3 pour respecter l'ordre croissant
        while i < len(T3) and T3[i] < x:
            i += 1
        T3.insert(i, x)  # Insérer l'élément à la bonne position
    return T3

# Exemple
T1 = [1, 3, 5, 7]
T2 = [2, 4, 6, 8]
T3 = fusion_A(T1, T2)
print(T3)  # Résultat attendu : [1, 2, 3, 4, 5, 6, 7, 8]



def fusion_B(T1, T2):
    n = len(T1)
    i1, i2 = 0, 0
    T3 = []
    
    # Tant qu'on n'a pas atteint la fin d'un des tableaux
    while i1 < n and i2 < n:
        if T1[i1] < T2[i2]:
            T3.append(T1[i1])  # Ajout de l'élément de T1
            i1 += 1
        elif T1[i1] > T2[i2]:
            T3.append(T2[i2])  # Ajout de l'élément de T2
            i2 += 1
        else:  # Cas où les deux sont égaux
            T3.append(T1[i1])
            T3.append(T2[i2])
            i1 += 1
            i2 += 1
    
    # Ajouter les éléments restants de T1 ou T2
    while i1 < n:
        T3.append(T1[i1])
        i1 += 1
    
    while i2 < n:
        T3.append(T2[i2])
        i2 += 1
    
    return T3

# Exemple
T1 = [1, 3, 5, 7]
T2 = [2, 4, 6, 8]
T3 = fusion_B(T1, T2)
print(T3)  # Résultat attendu : [1, 2, 3, 4, 5, 6, 7, 8]

