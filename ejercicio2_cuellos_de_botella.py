import json
from collections import deque

with open("datos/ejercicio2_datos.json") as f:
    datos = json.load(f)

grafo = datos["grafo"]
inicio = datos["inicio"]
objetivo = datos["objetivo"]

def cuello_botella(grafo, inicio, objetivo):
    cola = [(inicio, [inicio])]
    visitados = set()
    f_nodos = {}

    while cola:
        nodo_actual, camino = cola.pop(0)
        if nodo_actual == objetivo:
            for nodo in camino[1:-1]:
                f_nodos[nodo] = f_nodos.get(nodo, 0) + 1
            continue

        for siguiente in grafo[nodo_actual]:
            if siguiente not in camino:
                nuevo_camino = camino + [siguiente]
                cola.append((siguiente, nuevo_camino))

    return f_nodos

resultado = cuello_botella(grafo, inicio, objetivo)
print(resultado)


