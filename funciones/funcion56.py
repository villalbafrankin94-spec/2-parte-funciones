
def contar_consonantes(texto):
    return sum(1 for c in texto if c.lower() in "bcdfghjklmnpqrstvwxyz")
