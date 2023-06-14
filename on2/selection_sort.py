import random
import time
import numpy as np

import vetores


def selection_sort(arr):
    start_time_1 = time.perf_counter()
    print("Começando ")
    n = len(arr)

    # Percorre o array da esquerda para a direita
    for i in range(n - 1):
        min_index = i

        # Encontra o índice do menor elemento restante no array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Troca o elemento atual com o menor elemento encontrado
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

    # Percorre o array da esquerda para a direita e da direita para a esquerda
    while left < right:
        min_idx = left
        max_idx = right

        # Encontra o índice do menor e do maior elemento restante no array
        for i in range(left, right + 1):
            if arr[i] < arr[min_idx]:
                min_idx = i
            if arr[i] > arr[max_idx]:
                max_idx = i

        # Se o índice do menor elemento é igual ao índice do maior elemento,
        # significa que ambos estão na mesma posição
        if min_idx == max_idx:
            arr[left], arr[right] = arr[min_idx], arr[min_idx]
        else:
            # Caso contrário, troca
            arr[left], arr[min_idx] = arr[min_idx], arr[left]
            arr[right], arr[max_idx] = arr[max_idx], arr[right]

        # Atualiza os limites esquerdo e direito
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
vetor_aleatorio2 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_ordenado1 = vetores.vetor_ordenado(tamanho_vetor)
vetor_ordenado2 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_semiordenado1 = vetores.vetor_quase_ordenado(tamanho_vetor)
vetor_semiordenado2 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_inverso1 = vetores.vetor_inversamente_ordenado(tamanho_vetor)
vetor_inverso2 = vetores.vetor_aleatorio(tamanho_vetor)

execute_selection(vetor_semiordenado1, vetor_semiordenado2)
