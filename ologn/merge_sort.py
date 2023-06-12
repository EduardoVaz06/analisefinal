import time
import numpy as np

import vetores


#
#
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

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     # Dividir o array ao meio
#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]
#
#     # Chamar recursivamente o Merge Sort nas duas metades
#     left_half = merge_sort(left_half)
#     right_half = merge_sort(right_half)
#
#     # Combinação das duas metades ordenadas
#     return merge(left_half, right_half)
#
#
# def merge(left, right):
#     merged = []
#     left_index = 0
#     right_index = 0
#
#     # Comparar elementos das duas metades e inserir na ordem correta em merged
#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] <= right[right_index]:
#             merged.append(left[left_index])
#             left_index += 1
#         else:
#             merged.append(right[right_index])
#             right_index += 1
#
#     # Adicionar elementos restantes, se houver, de left e right
#     while left_index < len(left):
#         merged.append(left[left_index])
#         left_index += 1
#
#     while right_index < len(right):
#         merged.append(right[right_index])
#         right_index += 1
#
#     return merged
#
#
# # criando o array
# size = 100
# # Gerar o array com números aleatórios não repetidos
# lista = np.random.choice(range(1, 200), size=size, replace=False)
# # Imprimir o array
# # print(lista)
#
# # Calcular o tempo de execução
# start_time = time.time()
# sorted_arr = merge_sort(lista)
# end_time = time.time()
#
# # Imprimir o array ordenado e o tempo de execução
# print("Array ordenado:", sorted_arr)
# execution_time = end_time - start_time
# print("Tempo de execução:", execution_time, "segundos")


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
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


def merge_sort_optimized(arr):
    if len(arr) <= 16:
        m_insertion_sort(arr)  # Switch to Insertion Sort for small subarrays
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort_optimized(left_half)
    right_half = merge_sort_optimized(right_half)

    # Skip merge step if subarrays are already sorted
    if left_half[-1] <= right_half[0]:
        return left_half + right_half

    return merge_optimized(left_half, right_half)


def merge_optimized(left, right):
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
    merge_sort(arr)
    end_time = time.time()
    execution_time1 = end_time - start_time

    # Imprimir o array ordenado e o tempo de execução
    print("Array ordenado (merge_sort):", arr[:5], "...", arr[-5:])
    print("Tempo de execução (merge_sort):", execution_time1, "segundos")

    # Calcular o tempo de execução do merge_sort_optimized
    start_time2 = time.time()
    merge_sort_optimized(arr2)
    end_time2 = time.time()
    execution_time2 = end_time2 - start_time2

    # Imprimir o array ordenado e o tempo de execução
    print("Array ordenado (merge_sort_optimized):", arr2[:5], "...", arr2[-5:])
    print("Tempo de execução (merge_sort_optimized):", execution_time2, "segundos")


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

execute_merge(vetor_aleatorio1, vetor_aleatorio2)