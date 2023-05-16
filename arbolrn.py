# Definición de la clase Nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.padre = None
        self.izquierda = None
        self.derecha = None
        self.color = "Rojo"  # Todos los nuevos nodos se insertan como rojos por defecto

# Definición de la clase Árbol Rojo-Negro
class ArbolRojoNegro:
    def __init__(self):
        self.NIL = Nodo(None)  # Representa un nodo nulo
        self.NIL.color = "Negro"
        self.raiz = self.NIL

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.padre = None
        nuevo_nodo.izquierda = self.NIL
        nuevo_nodo.derecha = self.NIL
        nuevo_nodo.color = "Rojo"

        nodo_actual = self.raiz
        nodo_padre = None

        while nodo_actual != self.NIL:
            nodo_padre = nodo_actual

            if nuevo_nodo.valor < nodo_actual.valor:
                nodo_actual = nodo_actual.izquierda
            else:
                nodo_actual = nodo_actual.derecha

        nuevo_nodo.padre = nodo_padre

        if nodo_padre is None:
            self.raiz = nuevo_nodo
        elif nuevo_nodo.valor < nodo_padre.valor:
            nodo_padre.izquierda = nuevo_nodo
        else:
            nodo_padre.derecha = nuevo_nodo

        if nuevo_nodo.padre is None:
            nuevo_nodo.color = "Negro"
            return

        if nuevo_nodo.padre.padre is None:
            return

        self.arreglar_desbalance(nuevo_nodo)

    def arreglar_desbalance(self, nodo):
        while nodo.padre is not None and nodo.padre.color == "Rojo":
            if nodo.padre == nodo.padre.padre.izquierda:
                tio = nodo.padre.padre.derecha

                if tio.color == "Rojo":
                    nodo.padre.color = "Negro"
                    tio.color = "Negro"
                    nodo.padre.padre.color = "Rojo"
                    nodo = nodo.padre.padre
                else:
                    if nodo == nodo.padre.derecha:
                        nodo = nodo.padre
                        self.rotar_izquierda(nodo)

                    nodo.padre.color = "Negro"
                    nodo.padre.padre.color = "Rojo"
                    self.rotar_derecha(nodo.padre.padre)
            else:
                tio = nodo.padre.padre.izquierda

                if tio.color == "Rojo":
                    nodo.padre.color = "Negro"
                    tio.color = "Negro"
                    nodo.padre.padre.color = "Rojo"
                    nodo = nodo.padre.padre
                else:
                    if nodo == nodo.padre.izquierda:
                        nodo = nodo.padre
                        self.rotar_derecha(nodo)

                    nodo.padre.color = "Negro"
                    nodo.padre.padre.color = "Rojo"
                    self.rotar_izquierda(nodo.padre.padre)

        self.raiz.color = "Negro"


    def rotar_izquierda(self, nodo):
        nodo_derecha = nodo.derecha
        nodo.derecha = nodo_derecha.izquierda

        if nodo.derecha != None:
            nodo.derecha.padre = nodo

        nodo_derecha.padre = nodo.padre

        if nodo.padre == None:
            self.raiz = nodo_derecha
        elif nodo == nodo.padre.izquierda:
            nodo.padre.izquierda = nodo_derecha
        else:
            nodo.padre.derecha = nodo_derecha

        nodo_derecha.izquierda = nodo
        nodo.padre = nodo_derecha

        # Actualizar el padre del nodo rotado
        if nodo.derecha != self.NIL:
            nodo.derecha.padre = nodo
    
    def mostrar_arbol(self):
        diccionario = self.mostrar_arbol_recursivo(self.raiz)
        print(diccionario)

    def mostrar_arbol_recursivo(self, nodo):
        diccionario = {}

        if nodo != self.NIL:
            diccionario[nodo.valor] = nodo.color
            diccionario.update(self.mostrar_arbol_recursivo(nodo.izquierda))
            diccionario.update(self.mostrar_arbol_recursivo(nodo.derecha))

        return diccionario

arbol = ArbolRojoNegro()
#insertar 27 19 34 7 25 31 65 2 49 98
arbol.insertar(27)
arbol.insertar(19)
arbol.insertar(34)
arbol.insertar(7)
arbol.insertar(25)
arbol.insertar(31)
arbol.insertar(65)
arbol.insertar(2)
arbol.insertar(49)
arbol.insertar(98)

# Para acceder a la raíz del árbol
raiz = arbol.raiz
print(raiz.valor)

arbol.mostrar_arbol()