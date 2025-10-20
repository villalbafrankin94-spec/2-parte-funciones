def promedio_ponderado(valores, pesos):
    return sum(v * p for v, p in zip(valores, pesos)) / sum(pesos)