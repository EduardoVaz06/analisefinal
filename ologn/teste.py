import random
import time
import numpy as np


def median_of_three(a, b, c):
    if a <= b <= c:
        return b
    if c <= b <= a:
        return b
    if a <= c <= b:
        return c
    if b <= c <= a:
        return c
    return a


def partition(L, low, high, ascending=True):
    pivot, pidx = median_of_three(L[low], L[(low + high - 1) // 2], L[high - 1]), low
    L[low], L[pidx] = L[pidx], L[low]
    i = low + 1
    for j in range(low + 1, high, 1):
        if (ascending and L[j] < pivot) or (not ascending and L[j] > pivot):
            L[i], L[j] = L[j], L[i]
            i += 1
    L[low], L[i - 1] = L[i - 1], L[low]
    return i - 1


def quicksort(L, low, high, ascending=True):
    if low < high:
        pivot_index = partition(L, low, high, ascending)
        quicksort(L, low, pivot_index, ascending)
        quicksort(L, pivot_index + 1, high, ascending)


# Criando o array
size = 500000
# Gerar o array com números aleatórios não repetidos
lista = np.random.choice(range(1, 600000), size=size, replace=False)
print("Array antes da ordenação:")
print(lista)

# Measure execution time
start_time = time.time()
quicksort(lista, 0, len(lista)-1)
end_time = time.time()
execution_time = end_time - start_time

print("Array ordenado:")
print(lista)
print("Tempo de execução:", execution_time, "segundos")


sorted_part = np.arange(size//3)  # Primeira parte ordenada
random_part = np.random.choice(range(size//3, 2*size//3), size//3, replace=False)  # Parte desordenada
sorted_part_2 = np.arange(2*size//3, size)  # Segunda parte ordenada

partially_sorted_array = np.concatenate((sorted_part, random_part, sorted_part_2))
print("Array semi antes da ordenação:")
print(partially_sorted_array)

start_time2 = time.time()
quicksort(partially_sorted_array, 0, size-1)
end_time2 = time.time()
execution_time2 = end_time2 - start_time2

print("Array ordenado:")
print(partially_sorted_array)
print("Tempo de execução:", execution_time2, "segundos")
