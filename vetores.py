import random


def vetor_aleatorio(size):
    arr = random.sample(range(1, size + 1), size)
    return arr


def vetor_quase_ordenado(size):
    arr = list(range(1, size + 1))
    # Intercalação aleatória de alguns elementos para torná-lo parcialmente ordenado
    for i in range(1, size, 5):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


def vetor_inversamente_ordenado(size):
    arr = list(range(size, 0, -1))
    return arr


def vetor_ordenado(size):
    arr = list(range(1, size + 1))
    return arr

