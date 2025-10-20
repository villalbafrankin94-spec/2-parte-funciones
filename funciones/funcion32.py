def contraseña_segura(clave):
    return len(clave) >= 8 and any(c.isdigit() for c in clave)