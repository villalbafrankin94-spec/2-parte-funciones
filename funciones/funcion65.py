def contar_mayores(lista, umbral):
    return sum(1 for x in lista if x > umbral)
