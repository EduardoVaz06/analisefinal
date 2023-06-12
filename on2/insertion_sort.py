import time
import numpy as np

import vetores


def insertion_sort(arr):
    start_time = time.time()
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    end_time = time.time()
    execution_time = end_time - start_time
    print("Tempo de execução:", execution_time, "segundos")
    return arr


def binary_insertion_sort(arr):
    start_time = time.time()
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        left = 0
        right = i - 1

        while left <= right:
            mid = (left + right) // 2
            if key < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        for j in range(i - 1, left - 1, -1):
            arr[j + 1] = arr[j]

        arr[left] = key

    end_time = time.time()
    execution_time = end_time - start_time
    print("Tempo de execução:", execution_time, "segundos")
    return arr


def execute_insertion(arr, arr2):
    lista1 = insertion_sort(arr)

    print("Selection Sort:")
    print("Lista ordenada:", lista1[:5], "...", lista1[-5:])

    lista2 = binary_insertion_sort(arr2)

    print("Binary Selection Sort:")
    print("Lista ordenada:", lista2[:5], "...", lista2[-5:])


#criar o vetor a partir do vetores.py e escolher o tamanho
tamanho_vetor = 1000
vetor_aleatorio1 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_aleatorio2 = vetor_aleatorio1
vetor_ordenado1 = vetores.vetor_ordenado(tamanho_vetor)
vetor_ordenado2 = vetor_ordenado1
vetor_semiordenado1 = vetores.vetor_quase_ordenado(tamanho_vetor)
vetor_semiordenado2 = vetor_semiordenado1
vetor_inverso1 = vetores.vetor_inversamente_ordenado(tamanho_vetor)
vetor_inverso2 = vetor_inverso1

execute_insertion(vetor_aleatorio1, vetor_aleatorio2)
