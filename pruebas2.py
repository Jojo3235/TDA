#dijkstra

import sys

def dijkstra(grafo, origen):
    if origen not in grafo:
        print("El nodo de origen no existe en el grafo.")
        return

    origen_nodo = grafo[origen]
    origen_nodo.distancia = 0
    nodos_restantes = set(grafo.values())

    while nodos_restantes:
        nodo_actual = min(nodos_restantes, key=lambda n: n.distancia)
        nodos_restantes.remove(nodo_actual)

        for arista in nodo_actual.vecinos:
            distancia_total = nodo_actual.distancia + arista.peso

            if distancia_total < arista.destino.distancia:
                arista.destino.distancia = distancia_total

def imprimir_rutas(grafo, origen):
    for nombre, nodo in grafo.items():
        if nodo.distancia == sys.maxsize:
            print(f"No hay ruta desde el nodo {origen} al nodo {nombre}.")
        else:
            print(f"La distancia mínima desde el nodo {origen} al nodo {nombre} es {nodo.distancia}.")


# Ejemplo de uso
from grafos import Grafo

grafo = Grafo()

grafo.agregar_nodo("A")
grafo.agregar_nodo("B")
grafo.agregar_nodo("C")
grafo.agregar_nodo("D")

grafo.agregar_arista("A", "B", 3)
grafo.agregar_arista("A", "C", 2)
grafo.agregar_arista("A", "D", 5)
grafo.agregar_arista("B", "D", 2)
grafo.agregar_arista("C", "D", 1)

dijkstra(grafo, "A")
imprimir_rutas(grafo, "A")
