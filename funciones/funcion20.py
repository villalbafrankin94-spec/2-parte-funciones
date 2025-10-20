def es_palindromo(texto):
    limpio = texto.replace(" ", "").lower()
    return limpio == limpio[::-1]
