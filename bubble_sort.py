import time
import random


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

#
# lista = [3, 2, 15, 1]
# sorted_list = bubble_sort(lista)
# print(sorted_list)
#
# Lista de exemplo
# Definir o tamanho do array
n = 200
# Gerar o array com números aleatórios
lista = [random.randint(1, 1000) for _ in range(n)]
#lista = [4, 2, 13, 15, 18, 24, 25, 26, 30, 35, 41, 55, 57, 60, 61, 65, 69, 77, 88, 119, 127, 133, 133, 136, 139, 142, 144, 146, 152, 154, 160, 164, 167, 170, 176, 182, 186, 190, 191, 196, 198, 204, 206, 213, 226, 232, 240, 242, 244, 249, 251, 260, 265, 275, 283, 287, 303, 306, 310, 322, 326, 332, 341, 343, 350, 360, 364, 376, 385, 391, 395, 404, 411, 412, 419, 421, 422, 428, 430, 441, 443, 446, 448, 450, 453, 459, 464, 479, 500, 503, 506, 512, 527, 541, 554, 556, 564, 567, 575, 578, 581, 585, 586, 593, 595, 604, 609, 610, 614, 614, 626, 629, 631, 637, 641, 642, 645, 645, 646, 648, 649, 652, 658, 681, 682, 683, 684, 687, 692, 694, 704, 714, 718, 723, 723, 724, 727, 728, 735, 735, 736, 743, 743, 754, 760, 760, 772, 773, 774, 787, 791, 794, 807, 807, 809, 814, 815, 815, 826, 838, 838, 839, 840, 851, 853, 855, 857, 863, 866, 876, 886, 895, 896, 898, 905, 906, 913, 916, 919, 920, 923, 926, 928, 928, 929, 934, 936, 937, 941, 953, 962, 971, 971, 973, 975, 989, 996, 996, 998, 999]


# Medição de tempo - Bubble Sort
start_time_1 = time.time()
sorted_list_1 = bubble_sort(lista)
end_time_1 = time.time()
execution_time_1 = end_time_1 - start_time_1

print("Bubble Sort:")
print("Lista ordenada:", sorted_list_1)
print("Tempo de execução:", execution_time_1, "segundos")

# Medição de tempo - Bubble Sort com Flag de Troca
start_time_2 = time.time()
sorted_list_2 = bubble_sort_swap(lista)
end_time_2 = time.time()
execution_time_2 = end_time_2 - start_time_2

print("Bubble Sort com Flag de Troca:")
print("Lista ordenada:", sorted_list_2)
print("Tempo de execução:", execution_time_2, "segundos")