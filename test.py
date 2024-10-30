 # test for a big number 
# import time
# import random
# import matplotlib.pyplot as plt

# print(" its start")
# # Tri par sélection
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]

# # Tri par insertion
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key

# # Tri fusion
# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i = j = k = 0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1

# # Tri rapide
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)

# # Tailles de données
# sizes = [1000, 2000, 4000, 8000, 16000, 32000]
# times_selection = []
# times_insertion = []
# times_merge = []
# times_quick = []

# for size in sizes:
#     data = list(range(size, 0, -1))  # Génère un tableau trié en ordre inverse (pire cas)

#     # Mesurer le temps pour chaque algorithme
#     # Tri par sélection
#     arr = data[:]
#     start = time.time()
#     selection_sort(arr)
#     times_selection.append(time.time() - start)

#     # Tri par insertion
#     arr = data[:]
#     start = time.time()
#     insertion_sort(arr)
#     times_insertion.append(time.time() - start)

#     # Tri fusion
#     arr = data[:]
#     start = time.time()
#     merge_sort(arr)
#     times_merge.append(time.time() - start)

#     # Tri rapide
#     arr = data[:]
#     start = time.time()
#     quick_sort(arr)
#     times_quick.append(time.time() - start)

# # Afficher les résultats sous forme de tableau
# print("n\tSelection\tInsertion\tMerge\tQuick")
# for i, size in enumerate(sizes):
#     print(f"{size}\t{times_selection[i]:.5f}\t{times_insertion[i]:.5f}\t{times_merge[i]:.5f}\t{times_quick[i]:.5f}")
    
    
# plt.plot(sizes, times_selection, label="Tri par sélection")
# plt.plot(sizes, times_insertion, label="Tri par insertion")
# plt.plot(sizes, times_merge, label="Tri fusion")
# plt.plot(sizes, times_quick, label="Tri rapide")
# plt.xlabel("Taille du tableau (n)")
# plt.ylabel("Temps d'exécution (secondes)")
# plt.legend()
# plt.title("Comparaison des temps d'exécution des algorithmes de tri")
# plt.show()
    

# print(" its finished")

import time
import matplotlib.pyplot as plt

# Fonctions de tri
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Tailles de données
sizes_n2 = [100, 200, 400, 800]  # pour sélection et insertion
sizes_nlogn = [100, 200, 400, 800] # pour tri fusion et tri rapide

# Mesures
def measure_time(sort_function, data):
    start = time.time()
    sort_function(data)
    return time.time() - start

times_selection = []
times_insertion = []
times_merge = []
times_quick = []

for size in sizes_n2:
    data = list(range(size, 0, -1))
    times_selection.append(measure_time(selection_sort, data[:]))
    times_insertion.append(measure_time(insertion_sort, data[:]))

for size in sizes_nlogn:
    data = list(range(size, 0, -1))
    times_merge.append(measure_time(merge_sort, data[:]))
    times_quick.append(measure_time(quick_sort, data[:]))

# Affichage
print("Selection Sort Times:", times_selection)
print("Insertion Sort Times:", times_insertion)
print("Merge Sort Times:", times_merge)
print("Quick Sort Times:", times_quick)

# Graphique
plt.plot(sizes_n2, times_selection, label="Tri par sélection")
plt.plot(sizes_n2, times_insertion, label="Tri par insertion")
plt.plot(sizes_nlogn, times_merge, label="Tri fusion")
plt.plot(sizes_nlogn, times_quick, label="Tri rapide")
plt.xlabel("Taille du tableau (n)")
plt.ylabel("Temps d'exécution (secondes)")
plt.legend()
plt.title("Comparaison des temps d'exécution des algorithmes de tri")
plt.show()
