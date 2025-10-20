import random
def numeros_aleatorios(n, minimo, maximo):
    return [random.randint(minimo, maximo) for _ in range(n)]