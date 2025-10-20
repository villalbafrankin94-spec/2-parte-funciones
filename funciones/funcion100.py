def ordenar_por_ultimo(lista):
    return sorted(lista, key=lambda x: x[-1] if x else "")