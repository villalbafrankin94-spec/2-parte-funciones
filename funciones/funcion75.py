def claves_con_vocal(diccionario):
    return sum(1 for k in diccionario if k[0].lower() in "aeiou")