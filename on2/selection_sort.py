import random
import time
import numpy as np

import vetores


def selection_sort(arr):
    start_time_1 = time.perf_counter()
    print("Começando ")
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    end_time_1 = time.perf_counter()
    execution_time_1 = end_time_1 - start_time_1
    print("Tempo de execução:", execution_time_1, "segundos")
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
    print("Tempo de execução:", execution_time, "segundos")
    return arr


def execute_selection(arr, arr2):
    lista1 = selection_sort(arr)

    print("Selection Sort:")
    print("Lista ordenada:", lista1[:5], "...", lista1[-5:])

    lista2 = selection_sort_improve(arr2)

    print("Selection Sort Aprimorado:")
    print("Lista ordenada:", lista2[:5], "...", lista2[-5:])


tamanho_vetor = 10000
vetor_aleatorio1 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_aleatorio2 = vetor_aleatorio1
vetor_ordenado1 = vetores.vetor_ordenado(tamanho_vetor)
vetor_ordenado2 = vetor_ordenado1
vetor_semiordenado1 = vetores.vetor_quase_ordenado(tamanho_vetor)
vetor_semiordenado2 = vetor_semiordenado1
vetor_inverso1 = vetores.vetor_inversamente_ordenado(tamanho_vetor)
vetor_inverso2 = vetor_inverso1

execute_selection(vetor_aleatorio1, vetor_aleatorio2)
