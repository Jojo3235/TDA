nombre1 = "Chewbacca"
nombre2 = "Han Solo"
nombre3 = "Luke Skywalker"
nombre4 = "Leia Organa"

class Nodo:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.siguiente = None

class TablaHash:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.buckets = [None] * capacidad
        
    def hash_func(self, clave):
        # Función hash básica que devuelve el índice de un bucket
        # basado en la clave, en este caso simplemente el módulo
        # de la longitud de la tabla hash.
        return hash(clave) % self.capacidad
        
    def insertar(self, clave, valor):
        indice = self.hash_func(clave)
        
        if self.buckets[indice] is None:
            self.buckets[indice] = Nodo(clave, valor)
        else:
            actual = self.buckets[indice]
            while actual.siguiente is not None and actual.clave != clave:
                actual = actual.siguiente
            if actual.clave == clave:
                actual.valor = valor
            else:
                actual.siguiente = Nodo(clave, valor)
                
    def buscar(self, clave):
        indice = self.hash_func(clave)
        actual = self.buckets[indice]
        while actual is not None:
            if actual.clave == clave:
                return actual.valor
            actual = actual.siguiente
        raise KeyError('Clave no encontrada')
    
tabla = TablaHash(10)
tabla.insertar('a', 1)
tabla.insertar('b', 2)
tabla.insertar('c', 3)

print(tabla.buscar('a'))  # salida: 1
print(tabla.buscar('b'))  # salida: 2
print(tabla.buscar('c'))  # salida: 3