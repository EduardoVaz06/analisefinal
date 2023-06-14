import time
import numpy as np

import vetores


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Verifica se o filho esquerdo é maior que o nó atual
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Verifica se o filho direito é maior que o nó atual
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Se o maior valor não for o nó atual, troca os valores e faz a recursão para o nó trocado
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

    # Constrói o max heap a partir do array
    for i in range(n // 2 - 1, -1, -1):
        heapify2(arr, n, i)

    # Extrai os elementos um por um, colocando-os na posição correta
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify2(arr, i, 0)

    end_time2 = time.time()
    execution_time2 = end_time2 - start_time2
    print("Tempo de execução:", execution_time2, "segundos")

    return arr


def execute_heap(arr, arr2):
    arr = heap_sort(arr)
    print("Array ordenado:", arr[:5], "...", arr[-5:])

    arr2 = heap_sort2(arr2)
    print("Array ordenado 2", arr2[:5], "...", arr2[-5:])


tamanho_vetor = 1000000
vetor_aleatorio1 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_aleatorio2 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_ordenado1 = vetores.vetor_ordenado(tamanho_vetor)
vetor_ordenado2 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_semiordenado1 = vetores.vetor_quase_ordenado(tamanho_vetor)
vetor_semiordenado2 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_inverso1 = vetores.vetor_inversamente_ordenado(tamanho_vetor)
vetor_inverso2 = vetores.vetor_aleatorio(tamanho_vetor)

execute_heap(vetor_semiordenado1, vetor_semiordenado2)