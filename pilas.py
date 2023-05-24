class nodoPila(object):
    info, sig = None, None

class Pila(object):
    def __init__(self):
        self.cima = None
        self.size = 0

    def apilar(pila, dato):
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = pila.cima
        pila.cima = nodo
        pila.size += 1

    def desapilar(pila):
        x = pila.cima.info
        pila.cima = pila.cima.sig
        pila.size -= 1
        return x
    
    def pila_vacia(pila):
        return pila.cima is None
    
    def en_cima(pila):
        if pila.cima.info:
            return pila.cima.info
        else:
            return None
        
    def size(pila):
        return pila.size
    
    def barrido(pila):
        paux = Pila()
        while not Pila.pila_vacia(pila):
            dato = Pila.desapilar(pila)
            print(dato)
            Pila.apilar(paux, dato)
        while not paux.pila_vacia():
            dato = Pila.desapilar(paux)
            Pila.apilar(pila, dato)


#Generar pila

pila = Pila()

#Apilar

pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)

#Desapilar

print(pila.desapilar())
print(pila.desapilar())

#Verificar si la pila esta vacia

print(pila.pila_vacia())

#Verificar el elemento en la cima

print(pila.en_cima())

#Verificar el tamaño de la pila

print(pila.size)

#Verificar el elemento en la cima

print(pila.en_cima())

#Barrido de la pila

pila.barrido()

print(pila.pila_vacia())

print(pila.size)

print(pila.barrido()    )