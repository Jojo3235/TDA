class nodoArbol(object):
    def __init__(self, info):
        self.info = info
        self.izq = None
        self.der = None

def eliminar_nodo(raiz, clave):
    x = None
    if raiz is not None:
        if clave < raiz.info:
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif clave > raiz.info:
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            if raiz.izq is None: 
                raiz = raiz.der
            elif raiz.der is None:
                raiz = raiz.izq
            else:
                raiz.izq, aux = remplazar(raiz.izq)
                raiz.info = aux.info            
    return raiz, x

def insertar_nodo(raiz, dato):
    if raiz is None:
        raiz = nodoArbol(dato)
    elif dato < raiz.info:
        raiz.izq = insertar_nodo(raiz.izq, dato)
    elif dato > raiz.info:
        raiz.der = insertar_nodo(raiz.der, dato)
    return raiz

def arbolvacio(raiz):
    return raiz is None

def remplazar(raiz):
    aux = None
    if raiz.der is None:
        aux = raizraiz = raiz.izq
    else:
        raiz.der, aux = remplazar(raiz.der)
    return raiz, aux

from colas import Cola
def por_nivel(raiz):
    pendientes = Cola()
    Cola.arrive(pendientes, raiz)
    while not Cola.cola_vacia(pendientes):
        nodo = Cola.atencion(pendientes)
        print(nodo.info)
        if nodo.izq is not None:
            Cola.arrive(pendientes, nodo.izq)
        if nodo.der is not None:
            Cola.arrive(pendientes, nodo.der)

def buscar(raiz, clave):
    pos = None
    if raiz is not None:
        if raiz.info == clave:
            pos = raiz
        elif clave < raiz.info:
            pos = buscar(raiz.izq, clave)
        else:
            pos = buscar(raiz.der, clave)
    return pos

def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)

def preorden(raiz):
    if raiz is not None:
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)

def postorden(raiz):
    if raiz is not None:
        postorden(raiz.izq)
        postorden(raiz.der)
        print(raiz.info)

def profundidad(raiz):
    if raiz is None:
        return 0
    else:
        return 1+max(profundidad(raiz.izq), profundidad(raiz.der))
    
def profundidad_real(raiz):
    if raiz is None:
        return 0
    else:
        n = profundidad(raiz)
        return n-1

arbol = nodoArbol(5)
arbol = insertar_nodo(arbol, 7)
arbol = insertar_nodo(arbol, 2)
arbol = insertar_nodo(arbol, 1)
arbol = insertar_nodo(arbol, 3)
arbol = insertar_nodo(arbol, 6)
arbol = insertar_nodo(arbol, 8)
arbol = insertar_nodo(arbol, 9)
arbol = insertar_nodo(arbol, 10)

print("Inorden")
inorden(arbol)
print("Preorden")
preorden(arbol)
print("Postorden")
postorden(arbol)
print("Por nivel")
por_nivel(arbol)

print("Profundidad")
print(profundidad_real(arbol))