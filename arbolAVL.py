class nodoArbolAVL(object):

    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info
        self.altura = 0

def altura(raiz):
    if raiz is None:
        return -1
    else:
        return raiz.altura
    
def actualizar_altura(raiz):
    if raiz is not None: 
        alt_izq = altura(raiz.izq)
        alt_der = altura(raiz.der)
        raiz.altura = max(alt_izq, alt_der) + 1

def rotar_simple(raiz, control):
    if control:
        aux = raiz.iz1
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz
    actualizar_altura(raiz)
    actualizar_altura(aux)
    raiz = aux
    return raiz

def rotar_doble(raiz, control):
    if control:
        raiz.izq = rotar_simple(raiz.izq, False)
        raiz = rotar_simple(raiz, True)
    else:
        raiz.der = rotar_simple(raiz.der, True)
        raiz = rotar_simple(raiz, False)
    return raiz

def balancear(raiz):
    if raiz is not None:
        if altura(raiz.izq) - altura(raiz.der) == 2:
            if altura(raiz.izq.izq) >= altura(raiz.izq.der):
                raiz = rotar_simple(raiz, True)
            else:
                raiz = rotar_doble(raiz, True)
        elif altura(raiz.der) - altura(raiz.izq) == 2:
            if altura(raiz.der.der) >= altura(raiz.der.izq):
                raiz = rotar_simple(raiz, False)
            else:
                raiz = rotar_doble(raiz, False)
        actualizar_altura(raiz)
    return raiz

def insertar_nodo(raiz, dato):
    if raiz is None:
        raiz = nodoArbolAVL(dato)
    elif dato < raiz.info:
        raiz.izq = insertar_nodo(raiz.izq, dato)
    else:
        raiz.der = insertar_nodo(raiz.der, dato)
    raiz = balancear(raiz)
    actualizar_altura(raiz)
    return raiz

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
                raiz.info, raiz.nrr = aux.info, aux.nrr
    raiz = balancear(raiz)
    actualizar_altura(raiz)
    return raiz, x

def remplazar(raiz):
    if raiz.der is None:
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = remplazar(raiz.der)
    raiz = balancear(raiz)
    actualizar_altura(raiz)
    return raiz, aux

def __str__(self):
    return str(self.info)

# arbol = nodoArbolAVL(10)
# arbol = insertar_nodo(arbol, 5)
# arbol = insertar_nodo(arbol, 15)
# arbol = insertar_nodo(arbol, 3)
# arbol = insertar_nodo(arbol, 7)
# arbol = insertar_nodo(arbol, 13)
# arbol = insertar_nodo(arbol, 17)
# arbol = insertar_nodo(arbol, 1)
# arbol = insertar_nodo(arbol, 4)
# arbol = insertar_nodo(arbol, 6)
# arbol = insertar_nodo(arbol, 8)
# arbol = insertar_nodo(arbol, 12)
# arbol = insertar_nodo(arbol, 14)
# arbol = insertar_nodo(arbol, 16)
# arbol = insertar_nodo(arbol, 18)
# arbol = insertar_nodo(arbol, 2)
# arbol = insertar_nodo(arbol, 9)
# arbol = insertar_nodo(arbol, 11)
# arbol = insertar_nodo(arbol, 19)
# arbol = insertar_nodo(arbol, 20)
# arbol = insertar_nodo(arbol, 21)
# arbol = insertar_nodo(arbol, 22)    
# arbol = insertar_nodo(arbol, 23)
# arbol = insertar_nodo(arbol, 24)
# arbol = insertar_nodo(arbol, 25)
# arbol = insertar_nodo(arbol, 26)
# arbol = insertar_nodo(arbol, 27)
# arbol = insertar_nodo(arbol, 28)
# arbol = insertar_nodo(arbol, 29)
# arbol = insertar_nodo(arbol, 30)
# arbol = insertar_nodo(arbol, 31)
# arbol = insertar_nodo(arbol, 32)
# arbol = insertar_nodo(arbol, 33)
# arbol = insertar_nodo(arbol, 34)
# arbol = insertar_nodo(arbol, 35)
# arbol = insertar_nodo(arbol, 36)
# arbol = insertar_nodo(arbol, 37)
# arbol = insertar_nodo(arbol, 38)
# arbol = insertar_nodo(arbol, 39)
# arbol = insertar_nodo(arbol, 40)

# arbol = balancear(arbol)

# print(18*" ",arbol.info,8*" ")
# print(8*" ",arbol.izq.info,16*" ",arbol.der.info,4*" ")
# print(4*" ",arbol.izq.izq.info, 6*" ", arbol.izq.der.info, 6*" ", arbol.der.izq.info, 8*" ", arbol.der.der.info)
# print(" ",arbol.izq.izq.izq.info, 2*" ",arbol.izq.izq.der.info, 2*" ",arbol.izq.der.izq.info," ", arbol.izq.der.der.info, " ",arbol.der.izq.izq.info, 2*" ", arbol.der.izq.der.info, " ", arbol.der.der.izq.info, 2*" ", arbol.der.der.der.info)
# print(arbol.izq.izq.izq.izq.info, arbol.izq.izq.izq.der.info, arbol.izq.izq.der.izq.info, arbol.izq.izq.der.der.info, arbol.izq.der.izq.izq.info, arbol.izq.der.izq.der.info, arbol.izq.der.der.izq.info, arbol.izq.der.der.der.info, arbol.der.izq.izq.izq.info, arbol.der.izq.izq.der.info, arbol.der.izq.der.izq.info, arbol.der.izq.der.der.info, arbol.der.der.izq.izq.info, arbol.der.der.izq.der.info, arbol.der.der.der.izq.info, arbol.der.der.der.der.info)