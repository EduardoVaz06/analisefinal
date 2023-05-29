import random
import time
import numpy as np


def selection_sort(arr):
    start_time_1 = time.perf_counter()
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    end_time_1 = time.perf_counter()
    execution_time_1 = end_time_1 - start_time_1
    #print("Tempo de execução:", execution_time_1, "segundos")
    return arr


def selection_sort_improve(arr):
    start_time2 = time.perf_counter()
    n = len(arr)
    left = 0
    right = n - 1

    while left < right:
        min_idx = left
        max_idx = right

        for i in range(left, right + 1):
            if arr[i] < arr[min_idx]:
                min_idx = i
            if arr[i] > arr[max_idx]:
                max_idx = i

        if min_idx == max_idx:
            # Special case when the minimum and maximum elements are the same
            arr[left], arr[right] = arr[min_idx], arr[min_idx]
        else:
            arr[left], arr[min_idx] = arr[min_idx], arr[left]
            arr[right], arr[max_idx] = arr[max_idx], arr[right]

        left += 1
        right -= 1
    end_time2 = time.perf_counter()
    execution_time = end_time2 - start_time2
    #print("Tempo de execução:", execution_time, "segundos")
    return arr


#criando o array
# Definir o tamanho do array
size = 1000000
# Gerar o array com números aleatórios não repetidos
lista = np.random.choice(range(1, 2000000), size=size, replace=False)
# Imprimir o array
#print(lista)

sorted_list_1 = selection_sort(lista)

print("Selection Sort:")
#print("Lista ordenada:", sorted_list_1)

sorted_list2 = selection_sort_improve(lista)

print("Selection Sort Aprimorado:")
#print("Lista ordenada:", sorted_list2)
