import time
import numpy as np


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    start_time = time.time()
    n = len(arr)

    # Construir o max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrair os elementos um por um
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    end_time = time.time()
    execution_time = end_time - start_time
    print("Tempo de execução:", execution_time, "segundos")

    return arr


def heapify_improve(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort_improve(arr):
    start_time = time.time()
    n = len(arr)

    # Construir o max heap começando do meio do array
    for i in range(n // 2 - 1, -1, -1):
        heapify_improve(arr, n, i)

    # Extrair os elementos um por um
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify_improve(arr, i, 0)

    end_time = time.time()
    execution_time = end_time - start_time
    print("Tempo de execução:", execution_time, "segundos")

    return arr


def heapify2(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    while True:
        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest == i:
            break

        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest
        left = 2 * i + 1
        right = 2 * i + 2


def heap_sort2(arr):
    start_time2 = time.time()
    n = len(arr)

    # Construir o max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify2(arr, n, i)

    # Extrair os elementos um por um
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify2(arr, i, 0)

    end_time2 = time.time()
    execution_time2 = end_time2 - start_time2
    print("Tempo de execução:", execution_time2, "segundos")

    return arr



# criando o array
size = 500000
# Gerar o array com números aleatórios não repetidos
lista = np.random.choice(range(1, 600000), size=size, replace=False)
lista2 = lista
# Imprimir o array
# print(lista)

# size = 1000000
# sorted_part = np.arange(size//3)  # Primeira parte ordenada
# random_part = np.random.choice(range(size//3, 2*size//3), size//3, replace=False)  # Parte desordenada
# sorted_part_2 = np.arange(2*size//3, size)  # Segunda parte ordenada
#
# partially_sorted_array = np.concatenate((sorted_part, random_part, sorted_part_2))
#
# partially_sorted_array2 = partially_sorted_array

# Calcular o tempo de execução
sorted_arr = heap_sort(lista)
print("Array ordenado:", sorted_arr)

sorted_arr2 = heap_sort2(lista2)
print("Array ordenado 2", sorted_arr2)

# sorted_arr_improve = heap_sort_improve(partially_sorted_array2)
# print("Array ordenado:", sorted_arr_improve)


