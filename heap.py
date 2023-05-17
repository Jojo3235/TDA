class Heap(object):
    
    def __init__(self, tamanio):
        self.tamanio = 0
        self.vector = [None] * tamanio


def agregar(heap, dato):
    heap.vector[heap.tamanio] = dato
    flotar(heap, heap.tamanio)
    heap.tamanio += 1

def quitar(heap):
    intercambio(heap.vector, 0, heap.tamanio - 1)
    dato = heap.vector[heap.tamanio - 1]
    heap.tamanio -= 1
    hundir(heap, 0)
    return dato

def cantidad_elementos(heap):
    return heap.tamanio

def heap_vacio(heap):
    return heap.tamanio == 0

def heap_lleno(heap):
    return heap.tamanio == len(heap.vector)

def flotar(heap, indice):
    while indice > 0 and heap.vector[indice] > heap.vector[(indice - 1) // 2]:
        padre = (indice - 1) // 2
        intercambio(heap.vector, indice, padre)
        indice = padre

def hundir(heap, indice):
    hijo_izq = indice * 2 + 1
    control = True
    while control and hijo_izq < heap.tamanio:
        hijo_der = hijo_izq + 1
        aux = hijo_izq
        if hijo_der < heap.tamanio:
            if heap.vector[hijo_der] > heap.vector[hijo_izq]:
                aux = hijo_der

        if heap.vector[indice] < heap.vector[aux]:
            intercambio(heap.vector, indice, aux)
            indice = aux
            hijo_izq = indice * 2 + 1
        else:
            control = False

def intercambio(vector, indice1, indice2):
    aux = vector[indice1]
    vector[indice1] = vector[indice2]
    vector[indice2] = aux

def monticulizar(heap):
    for i in range(len(heap.vector)):
        hundir(heap, i)

def arribo(heap, dato, prioridad):
    agregar(heap, [prioridad, dato])

def atencion(heap):
    return quitar(heap)[1]

def cambiar_prioridad(heap, indice, prioridad):
    prioridad_anterior = heap.vector[indice][0]
    heap.vector[indice][0] = prioridad
    if prioridad > prioridad_anterior:
        flotar(heap, indice)
    else:
        hundir(heap, indice)

def heapsort(heap):
    aux = heap.tamanio
    for i in range(heap.tamanio):
        quitar(heap)
    heap.tamanio = aux

def buscar(heap, buscado):
    i = 0
    while i < heap.tamanio and heap.vector[i][1] != buscado:
        i += 1
    if i < heap.tamanio:
        return i
    else:
        return -1

# from random import randint

# heap = Heap(10)

# while not heap_lleno(heap):
#     num = randint(0, 500)
#     prioridad = randint(1,3)
#     agregar(heap, [prioridad, num])


# print(heap.vector)
# heapsort(heap)
# print(heap.vector)

# print(heap.vector)
# while not heap_vacio(heap):
#     dato = atencion(heap)
#     print(dato)

# monticulo = Heap(10)
# arribo(monticulo, 1, 1)
# arribo(monticulo, 2, 2)
# arribo(monticulo, 3, 3)
# arribo(monticulo, 4, 4)
# arribo(monticulo, 5, 5)
# arribo(monticulo, 6, 6)
# arribo(monticulo, 7, 7)
# arribo(monticulo, 8, 8)
# arribo(monticulo, 9, 9)
# arribo(monticulo, 10, 10)

# print(monticulo.vector)

# cambiar_prioridad(monticulo, 0, 11)

# print(monticulo.vector)

# heapsort(monticulo)

# print(monticulo.vector)

# cambiar_prioridad(monticulo, 0, 11)

# print(monticulo.vector)

# heapsort(monticulo)

# print(monticulo.vector)

# heap2 = Heap(10)

# for i in range(10):
#     arribo(heap2, i, i)

# print(heap2.vector)

# print(buscar(heap2, 6541))