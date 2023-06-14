import time
import numpy as np
import random
import vetores


def partition(arr, low, high):
    pivot = arr[high]  # utimo elemento com pivo
    i = low - 1  # indice do menor elemento

    for j in range(low, high):#loop para percorrer o array
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        # particionar o array e receber o indice do pivo
        pivot_index = partition(arr, low, high)

        # Chamada recursiva
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def partition2(arr, low, high):
    # selectionar o pivo randomico
    pivot_index = random.randint(low, high)
    # posicionar o pivo randomico para o fim
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1  # idice do menor elemento

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
    start_time = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    end_time = time.time()
    execution_time = end_time - start_time

    print("Array ordenado:", arr[:5], "...", arr[-5:])
    print("Tempo de execução (quick_sort):", execution_time, "segundos")

    start_time2 = time.time()
    quick_sort2(arr2, 0, len(arr2) - 1)
    end_time2 = time.time()
    execution_time2 = end_time2 - start_time2

    print("Array ordenado:", arr2[:5], "...", arr2[-5:])
    print("Tempo de execução:", execution_time2, "segundos")

tamanho_vetor = 1000000
vetor_aleatorio1 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_aleatorio2 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_ordenado1 = vetores.vetor_ordenado(tamanho_vetor)
vetor_ordenado2 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_semiordenado1 = vetores.vetor_quase_ordenado(tamanho_vetor)
vetor_semiordenado2 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_inverso1 = vetores.vetor_inversamente_ordenado(tamanho_vetor)
vetor_inverso2 = vetores.vetor_aleatorio(tamanho_vetor)

execute_quick(vetor_semiordenado1, vetor_semiordenado2)