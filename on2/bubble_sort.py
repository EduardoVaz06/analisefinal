import time
import random
import vetores


def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def bubble_sort_swap(arr):
    n = len(arr)

    for i in range(n - 1):
        swap = False  # Flag de troca

        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True

        if not swap:
            break

    return arr


def execute_bubble(arr, arr2):
    start_time_1 = time.time()
    bubble_sort_swap(arr)
    end_time_1 = time.time()
    execution_time_1 = end_time_1 - start_time_1

    print("Bubble Sort:")
    print("Lista ordenada:", arr[:5], "...", arr[-5:])
    print("Tempo de execução:", execution_time_1, "segundos")

    start_time_2 = time.time()
    bubble_sort_swap(arr2)
    end_time_2 = time.time()
    execution_time_2 = end_time_2 - start_time_2

    print("Bubble Sort com Flag de Troca:")
    print("Lista ordenada:", arr2[:5], "...", arr2[-5:])
    print("Tempo de execução:", execution_time_2, "segundos")


#criar o vetor a partir do vetores.py e escolher o tamanho
tamanho_vetor = 50000
vetor_aleatorio1 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_aleatorio2 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_ordenado1 = vetores.vetor_ordenado(tamanho_vetor)
vetor_ordenado2 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_semiordenado1 = vetores.vetor_quase_ordenado(tamanho_vetor)
vetor_semiordenado2 = vetores.vetor_aleatorio(tamanho_vetor)
vetor_inverso1 = vetores.vetor_inversamente_ordenado(tamanho_vetor)
vetor_inverso2 = vetores.vetor_aleatorio(tamanho_vetor)

#escolher o tipo de vetor e executar
execute_bubble(vetor_semiordenado1, vetor_inverso1)



