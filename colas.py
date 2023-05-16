class nodoCola(object):
    info, sig = None, None

class Cola(object):
    def __init__(self):
        self.frente = None
        self.final = None
        self.size = 0

    def arrive(cola, dato):
        nodo = nodoCola()
        nodo.info = dato
        nodo.sig = None
        if cola.final is None:
            cola.frente = nodo
        else:
            cola.final.sig = nodo
        cola.final = nodo
        cola.size += 1
    
    def atencion(cola):
        dato = cola.frente.info
        cola.frente = cola.frente.sig
        if cola.frente is None:
            cola.final = None
        cola.size -= 1
        return dato
    
    def cola_vacia(cola):
        return cola.frente is None
    
    def primero(cola):
        if cola.frente.info:
            return cola.frente.info
        else:
            return None
        
    def size(cola):
        return cola.size
    
    def mover_al_final(cola):
        dato = Cola.atencion(cola)
        Cola.arrive(cola, dato)
        return dato
    
    def barrido(cola):
        i = 0
        while i < cola.size:
            dato = Cola.mover_al_final(cola)
            print(dato)
            i += 1

# #Generar cola

# cola = Cola()

# #Arrive

# cola.arrive(1)
# cola.arrive(2)
# cola.arrive(3)
# cola.arrive(4)

# #Atencion

# print(cola.atencion())

# #Barrido

# cola.barrido()

# #Mover al final

# print(cola.mover_al_final())

# #Barrido

# cola.barrido()

# #Primero

# print(cola.primero())

# #Size

# print(cola.size)

# #Cola vacia

# print(cola.cola_vacia())
