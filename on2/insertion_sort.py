import time
import numpy as np

import vetores


def insertion_sort(arr):
    start_time = time.time()
    n = len(arr)

    # Percorre o array a partir do segundo elemento
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move os elementos maiores que a chave para a direita
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insere a chave na posição correta
        arr[j + 1] = key

    end_time = time.time()
    execution_time = end_time - start_time
    print("Tempo de execução:", execution_time, "segundos")
    return arr


def binary_insertion_sort(arr):
    start_time = time.time()
    n = len(arr)

    # Percorre o array a partir do segundo elemento
    for i in range(1, n):
        key = arr[i]
        left = 0
        right = i - 1

        # Realiza a busca binária para encontrar a posição correta da chave
        while left <= right:
            mid = (left + right) // 2
            if key < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Move os elementos maiores que a chave para a direita
        for j in range(i - 1, left - 1, -1):
            arr[j + 1] = arr[j]

        # Insere a chave na posição correta
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
tamanho_vetor = 1000000
vetor_aleatorio1 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_aleatorio2 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_ordenado1 = vetores.vetor_ordenado(tamanho_vetor)
vetor_ordenado2 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_semiordenado1 = vetores.vetor_quase_ordenado(tamanho_vetor)
vetor_semiordenado2 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_inverso1 = vetores.vetor_inversamente_ordenado(tamanho_vetor)
vetor_inverso2 = vetores.vetor_aleatorio(tamanho_vetor)

execute_insertion(vetor_semiordenado1, vetor_semiordenado2)
