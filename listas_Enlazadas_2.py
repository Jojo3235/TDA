class nodoLista(object):
    info, sig = None, None

class Lista(object):
    def __init__(self):
        self.inicio = None
        self.size = 0

    def eliminar(lista, clave, campo=None):
        dato = None
        if Lista.criterio(lista.inicio.info, campo) == Lista.criterio(clave, campo):
            dato = lista.inicio.info
            lista.inicio = lista.inicio.sig
            lista.size -= 1
        else:
            anterior = lista.inicio
            actual = lista.inicio.sig
            while actual is not None and Lista.criterio(actual.info, campo) != Lista.criterio(clave, campo):
                anterior = anterior.sig
                actual = actual.sig
            if actual is not None:
                dato = actual.info
                anterior.sig = actual.sig
                lista.size -= 1
        return dato
    
    def criterio(dato, campo=None):
        dic = {}
        if hasattr(dato, '__dict__'):
            dic = dato.__dict__
        if campo is None or campo not in dic:
            return dato
        else:
            return dic[campo]
        
    def insertar(lista, dato, campo=None):
        nodo = nodoLista()
        nodo.info = dato
        if lista.inicio is None or Lista.criterio(lista.inicio.info, campo) > Lista.criterio(dato, campo):
            nodo.sig = lista.inicio
            lista.inicio = nodo
        else:
            anterior = lista.inicio
            actual = lista.inicio.sig
            while actual is not None and Lista.criterio(actual.info, campo) < Lista.criterio(dato, campo):
                anterior = anterior.sig
                actual = actual.sig
            nodo.sig = actual
            anterior.sig = nodo
        lista.size += 1

    def buscar(lista, buscado, campo=None):
        aux = lista.inicio
        while aux is not None and Lista.criterio(aux.info, campo) != buscado:
            aux = aux.sig
        return aux
    

    def barrido(lista):
        aux = lista.inicio
        while aux is not None:
            print(aux.info)
            aux = aux.sig


#Generar lista

lista = Lista()

#Insertar

lista.insertar(1)
lista.insertar(2)
lista.insertar(3)
lista.insertar(4)

#Eliminar

print(lista.eliminar(1))
print(lista.eliminar(2))
print(lista.eliminar(3))

#Buscar

print(lista.buscar(4))

#Barrido

lista.barrido()

