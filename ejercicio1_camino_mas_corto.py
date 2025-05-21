import json
import heapq

with open("datos/ejercicio1_datos.json") as f:
    datos = json.load(f)

grafo = datos["grafo"]
origen = datos["origen"]
destino = datos["destino"]

def dijkstra(grafo, origen, destino):
    heap = [(0, origen, [origen])]
    visitados = set()

    while heap:
        costo_actual, nodo, camino = heapq.heappop(heap)

        if nodo == destino:
            return camino, costo_actual

        if nodo in visitados:
            continue

        visitados.add(nodo)

        for vecino, peso in grafo[nodo].items():
            if vecino not in visitados:
                heapq.heappush(heap, (costo_actual + peso, vecino, camino + [vecino]))

    return None, float("inf")

camino, costo_total = dijkstra(grafo, origen, destino)

if camino:
    print("Camino más corto:", camino)
    print("Costo total:", costo_total)
else:
    print("No se encontró un camino desde", origen, "hasta", destino)

