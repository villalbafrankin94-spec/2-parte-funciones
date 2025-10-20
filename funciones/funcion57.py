def eliminar_vocales(texto):
    return "".join(c for c in texto if c.lower() not in "aeiou")