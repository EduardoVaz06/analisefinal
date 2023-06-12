import time
import numpy as np
import random
import vetores


def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1  # Index of the smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # Recursively sort the sub-arrays
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def partition2(arr, low, high):
    # Randomly choose the pivot index
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1  # Index of the smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort2(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition2(arr, low, high)

        # Recursively sort the sub-arrays
        quick_sort2(arr, low, pivot_index - 1)
        quick_sort2(arr, pivot_index + 1, high)


def execute_quick(arr, arr2):
    # Calcular o tempo de execução do quick_sort
    start_time = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    end_time = time.time()
    execution_time = end_time - start_time

    # Imprimir o array ordenado e o tempo de execução
    print("Array ordenado:", arr[:5], "...", arr[-5:])
    print("Tempo de execução (quick_sort):", execution_time, "segundos")

    # quick melhor
    start_time2 = time.time()
    quick_sort2(arr2, 0, len(arr2) - 1)
    end_time2 = time.time()
    execution_time2 = end_time2 - start_time2

    # Print the sorted array and the execution time
    print("Array ordenado:", arr2[:5], "...", arr2[-5:])
    print("Tempo de execução:", execution_time2, "segundos")


#criar o vetor a partir do vetores.py e escolher o tamanho
tamanho_vetor = 500000
vetor_aleatorio1 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_aleatorio2 = vetor_aleatorio1
vetor_ordenado1 = vetores.vetor_ordenado(tamanho_vetor)
vetor_ordenado2 = vetor_ordenado1
vetor_semiordenado1 = vetores.vetor_quase_ordenado(tamanho_vetor)
vetor_semiordenado2 = vetor_semiordenado1
vetor_inverso1 = vetores.vetor_inversamente_ordenado(tamanho_vetor)
vetor_inverso2 = vetor_inverso1

execute_quick(vetor_aleatorio1, vetor_aleatorio2)