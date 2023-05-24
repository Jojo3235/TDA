import sys

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.visitado = False
        self.distancia = sys.maxsize
        self.vecinos = []

    def agregar_vecino(self, vecino, peso):
        self.vecinos.append(Arista(vecino, peso))

class Arista:
    def __init__(self, destino, peso):
        self.destino = destino
        self.peso = peso

class Vertice:
    def __init__(self, nombre):
        self.nombre = nombre

class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, nodo):
        self.nodos[nodo.nombre] = nodo

    def obtener_nodo(self, nombre):
        return self.nodos.get(nombre)

    def dijkstra(self, origen):
        if origen not in self.nodos:
            print("El nodo de origen no existe en el grafo.")
            return

        origen_nodo = self.nodos[origen]
        origen_nodo.distancia = 0
        nodos_restantes = set(self.nodos.values())

        while nodos_restantes:
            nodo_actual = min(nodos_restantes, key=lambda n: n.distancia)
            nodos_restantes.remove(nodo_actual)

            for arista in nodo_actual.vecinos:
                distancia_total = nodo_actual.distancia + arista.peso

                if distancia_total < arista.destino.distancia:
                    arista.destino.distancia = distancia_total

    def imprimir_rutas(self, origen):
        for nombre, nodo in self.nodos.items():
            if nodo.distancia == sys.maxsize:
                print(f"No hay ruta desde el nodo {origen} al nodo {nombre}.")
            else:
                print(f"La distancia mínima desde el nodo {origen} al nodo {nombre} es {nodo.distancia}.")


# Ejemplo de uso
nodo_a = Nodo("A")
nodo_b = Nodo("B")
nodo_c = Nodo("C")
nodo_d = Nodo("D")
nodo_e = Nodo("E")

nodo_a.agregar_vecino(nodo_b, 10)
nodo_a.agregar_vecino(nodo_c, 15)
nodo_b.agregar_vecino(nodo_d, 12)
nodo_b.agregar_vecino(nodo_e, 15)
nodo_c.agregar_vecino(nodo_d, 10)
nodo_d.agregar_vecino(nodo_e, 2)

grafo = Grafo()
grafo.agregar_nodo(nodo_a)
grafo.agregar_nodo(nodo_b)
grafo.agregar_nodo(nodo_c)
grafo.agregar_nodo(nodo_d)
grafo.agregar_nodo(nodo_e)

grafo.dijkstra("A")
grafo.imprimir_rutas("A")
