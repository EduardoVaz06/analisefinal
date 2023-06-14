import time
import numpy as np
import vetores


def m_insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Chama recursivamente a função merge_sort para ordenar as metades esquerda e direita
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combina as duas metades ordenadas
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Compara os elementos dos subarrays e adiciona o menor ao array mesclado
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Adiciona os elementos restantes, se houver, de um dos subarrays ao array mesclado
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


def merge_sort_2(arr):
    if len(arr) <= 16:
        m_insertion_sort(arr)  #usar o insertion para subarrays pequenos
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort_2(left_half)
    right_half = merge_sort_2(right_half)

    # pular o merge se os subarrays ja estiverem ordenados
    if left_half[-1] <= right_half[0]:
        return left_half + right_half

    return merge_2(left_half, right_half)


def merge_2(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


def execute_merge(arr, arr2):
    # Calcular o tempo de execução do merge_sort
    start_time = time.time()
    arr = merge_sort(arr)
    end_time = time.time()
    execution_time1 = end_time - start_time

    # Imprimir o array ordenado e o tempo de execução
    print("Array ordenado (merge_sort):", arr[:5], "...", arr[-5:])
    print("Tempo de execução (merge_sort):", execution_time1, "segundos")

    # Calcular o tempo de execução do merge_sort_optimized
    start_time2 = time.time()
    arr2 = merge_sort_2(arr2)
    end_time2 = time.time()
    execution_time2 = end_time2 - start_time2

    # Imprimir o array ordenado e o tempo de execução
    print("Array ordenado (merge_sort_optimized):", arr2[:5], "...", arr2[-5:])
    print("Tempo de execução (merge_sort_optimized):", execution_time2, "segundos")


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

execute_merge(vetor_semiordenado1, vetor_inverso1)