import time
import numpy as np


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


def insertion_sort_improve(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Find the correct position and shift elements to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


#criando o array
size = 1000
# Gerar o array com números aleatórios não repetidos
lista = np.random.choice(range(1, 2000), size=size, replace=False)
# Imprimir o array
#print(lista)

sorted_list_1 = insertion_sort(lista)

print("Selection Sort:")
print("Lista ordenada:", sorted_list_1)