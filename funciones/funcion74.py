def sumar_mayores(diccionario, umbral):
    return sum(v for v in diccionario.values() if v > umbral)