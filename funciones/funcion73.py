def claves_largas(diccionario, minimo):
    return [k for k in diccionario if len(k) >= minimo]