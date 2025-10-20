def contiene_numeros(texto):
    return any(c.isdigit() for c in texto)