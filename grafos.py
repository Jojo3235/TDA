class nodoArista(object):
    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.sig = None

class nodoVertice(object):
    def __init__(self, info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()

class Grafo(object):
    def __init__(self, dirigido=True):
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0

class Arista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0

def insertar_vertice(grafo, dato):
    nodo = nodoVertice(dato)
    if grafo.inicio is None or grafo.inicio.info > dato:
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig  
        while act is not None and act.info < nodo.info:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1

def insertar_arista(grafo, dato, origen, destino):
    agregar_arista(origen.adyacentes, dato, destino.info)
    if not grafo.dirigido:
        agregar_arista(destino.adyacentes, dato, origen.info)

def agregar_arista(origen, dato, destino):
    nodo = nodoArista(dato, destino)
    if origen.inicio is None or origen.inicio.destino > destino:
        nodo.sig = origen.inicio
        origen.inicio = nodo
    else:
        ant = origen.inicio
        act = origen.inicio.sig
        while act is not None and act.destino < nodo.destino:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.tamanio += 1

def eliminar_vertice(grafo, clave):
    x = None
    if grafo.inicio.info == clave:
        x = grafo.inicio.info
        grafo.inicio = grafo.inicio.sig
        grafo.tamanio -= 1
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while act is not None and act.info != clave:
            ant = act
            act = act.sig
        if act is not None:
            x = act.info
            ant.sig = act.sig
            grafo.tamanio -= 1
    if x is not None:
        aux = grafo.inicio
        while aux is not None:
            if aux.adyacentes.inicio is not None:
                eliminar_arista(aux.adyacentes, x)
            aux = aux.sig
    return x

def eliminar_arista(vertice, destino):
    x = None
    if vertice.inicio.destino == destino:
        x = vertice.inicio.info
        vertice.inicio = vertice.inicio.sig
        vertice.tamanio -= 1
    else: 
        ant = vertice.inicio
        act = vertice.inicio.sig
        while act is not None and act.destino != destino:
            ant = act
            act = act.sig
        if act is not None:
            x = act.info
            ant.sig = act.sig
            vertice.tamanio -= 1
    return x

def buscar_vertice(grafo, buscado):
    aux = grafo.inicio
    while aux is not None and aux.info != buscado:
        aux = aux.sig
    return aux

def buscar_arista(vertice, buscado):
    aux = vertice.adyacentes.inicio
    while aux is not None and aux.destino != buscado:
        aux = aux.sig
    return aux

def tamanio(grafo):
    return grafo.tamanio

def grafo_vacio(grafo):
    return grafo.inicio is None 

def existe_paso(grafo, origen, destino):
    resultado = False
    if not origen.visitado:
        origen.visitado = True
        vadyacentes = origen.adyacentes.inicio
        while vadyacentes is not None and not resultado:
            if vadyacentes.info == destino.info:
                return True
            elif not vadyacentes.visitado:
                resultado = existe_paso(grafo, vadyacentes, destino)
            vadyacentes = vadyacentes.sig
    return resultado

def adyacentes(vertice):
    aux = vertice.adyacentes.inicio
    while aux is not None:
        print(aux.destino, aux.info)
        aux = aux.sig

def es_adyacente(vertice, destino):
    resultado = False
    aux = vertice.adyacentes.inicio
    while aux is not None and not resultado:
        if aux.destino == resultado:
            resultado = True
        aux = aux.sig
    return resultado

def marcar_no_visitado(grafo):
    aux = grafo.inicio
    while aux is not None:
        aux.visitado = False
        aux = aux.sig

def barrido_vertices(grafo):
    aux = grafo.inicio
    while aux is not None:
        print(aux.info)
        aux = aux.sig

def barrido_profundidad(grafo, vertice):
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            print(vertice.info)
            adyacentes = vertice.adyacentes.inicio
            while adyacentes is not None:
                adyacente = buscar_vertice(grafo, adyacentes.destino)
                if not adyacente.visitado:
                    barrido_profundidad(grafo, adyacente)
                adyacentes = adyacentes.sig
        vertice = vertice.sig

from colas import Cola
def barrido_amplitud(grafo, vertice):
    cola = Cola()
    Cola.arrive(cola, vertice)
    marcar_no_visitado(grafo)  # Marcar todos los vértices como no visitados
    vertice.visitado = True  # Marcar el vértice inicial como visitado

    while not Cola.cola_vacia(cola):
        nodo = Cola.atencion(cola)
        print(nodo.info)

        adyacentes = nodo.adyacentes.inicio
        while adyacentes is not None:
            adyacente = buscar_vertice(grafo, adyacentes.destino)
            if not adyacente.visitado:
                adyacente.visitado = True
                Cola.arrive(cola, adyacente)
            adyacentes = adyacentes.sig


def mostrar_aristas(grafo):
    aux = grafo.inicio
    while aux is not None:
        print("Nodo:", aux.info)
        adyacentes = aux.adyacentes.inicio
        while adyacentes is not None:
            print("Arista de ", aux.info, "con", adyacentes.destino, "peso:", adyacentes.info)
            adyacentes = adyacentes.sig
        aux = aux.sig

def grado(grafo, vertice):
    grado = 0
    aux = grafo.inicio
    while aux is not None:
        adyacentes = aux.adyacentes.inicio
        while adyacentes is not None:
            if adyacentes.destino == vertice.info:
                grado += 1
            adyacentes = adyacentes.sig
        aux = aux.sig
    return grado

from heap import Heap, arribo as arribo_heap, atencion as atencion_heap, heap_vacio, buscar as buscar_heap, intercambio as intercambio_heap, cambiar_prioridad as cambiar_prioridad_heap
import sys 

def dijkstra(grafo, origen):
    distancias = {}
    previos = {}
    heap = Heap(tamanio(grafo))
    for vertice in grafo.inicio:
        distancias[vertice.info] = sys.maxsize
        previos[vertice.info] = None
        arribo_heap(heap, vertice.info, sys.maxsize)
    distancias[origen.info] = 0
    cambiar_prioridad_heap(heap, buscar_heap(heap, origen.info), 0)
    while not heap_vacio(heap):
        actual = atencion_heap(heap)
        vertice_actual = buscar_vertice(grafo, actual)
        for adyacente in vertice_actual.adyacentes:
            distancia = distancias[actual] + adyacente.info
            if distancia < distancias[adyacente.destino]:
                distancias[adyacente.destino] = distancia
                previos[adyacente.destino] = actual
                intercambio_heap(heap, buscar_heap(heap, adyacente.destino), distancia)
    return distancias, previos


grafo = Grafo(True)
insertar_vertice(grafo, 1)
insertar_vertice(grafo, 2)
insertar_vertice(grafo, 3)
insertar_vertice(grafo, 4)
insertar_vertice(grafo, 5)
insertar_vertice(grafo, 6)

vertice1 = buscar_vertice(grafo, 1)
vertice2 = buscar_vertice(grafo, 2)
vertice3 = buscar_vertice(grafo, 3)
vertice4 = buscar_vertice(grafo, 4)
vertice5 = buscar_vertice(grafo, 5)

insertar_arista(grafo, 5, vertice1, vertice2)
insertar_arista(grafo, 1, vertice1, vertice3)
insertar_arista(grafo, 1, vertice1, vertice2)

print("Mostrar aristas:")
mostrar_aristas(grafo)

print("Grado de vertice2:")
print(grado(grafo, vertice2))

print("Barrido profundidad:")
barrido_profundidad(grafo, grafo.inicio)

print("Barrido amplitud:")
barrido_amplitud(grafo, grafo.inicio)

print("Dijkstra:")
distancias, previos = dijkstra(grafo, vertice1)