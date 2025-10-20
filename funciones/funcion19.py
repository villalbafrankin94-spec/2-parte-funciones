def ocultar_vocales(texto):
    return "".join("*" if c.lower() in "aeiou" else c for c in texto)