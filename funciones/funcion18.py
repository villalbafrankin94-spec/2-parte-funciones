def contar_vocales(texto):
    return sum(1 for c in texto if c.lower() in "aeiou")