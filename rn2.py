class NodoRN:
    def __init__(self, valor, color):
        self.valor = valor
        self.color = color
        self.izquierda = None
        self.derecha = None
        self.padre = None

class RN:
    def __init__(self):
        self.nil = NodoRN(None, "negro")
        self.raiz = self.nil

    def insertar(self, valor):
        nuevo_nodo = NodoRN(valor, "rojo")
        nuevo_nodo.izquierda = self.nil
        nuevo_nodo.derecha = self.nil

        nodo_actual = self.raiz
        nodo_padre = None

        while nodo_actual != self.nil:
            nodo_padre = nodo_actual
            if valor < nodo_actual.valor:
                nodo_actual = nodo_actual.izquierda
            else:
                nodo_actual = nodo_actual.derecha

        nuevo_nodo.padre = nodo_padre

        if nodo_padre is None:
            self.raiz = nuevo_nodo
        elif valor < nodo_padre.valor:
            nodo_padre.izquierda = nuevo_nodo
        else:
            nodo_padre.derecha = nuevo_nodo

        self._arreglar_insercion(nuevo_nodo)

    def _arreglar_insercion(self, nodo):
        while nodo.padre.color == "rojo":
            if nodo.padre == nodo.padre.padre.izquierda:
                nodo_tio = nodo.padre.padre.derecha
                if nodo_tio.color == "rojo":
                    nodo.padre.color = "negro"
                    nodo_tio.color = "negro"
                    nodo.padre.padre.color = "rojo"
                    nodo = nodo.padre.padre
                else:
                    if nodo == nodo.padre.derecha:
                        nodo = nodo.padre
                        self._rotacion_izquierda(nodo)
                    nodo.padre.color = "negro"
                    nodo.padre.padre.color = "rojo"
                    self._rotacion_derecha(nodo.padre.padre)
            else:
                nodo_tio = nodo.padre.padre.izquierda
                if nodo_tio.color == "rojo":
                    nodo.padre.color = "negro"
                    nodo_tio.color = "negro"
                    nodo.padre.padre.color = "rojo"
                    nodo = nodo.padre.padre
                else:
                    if nodo == nodo.padre.izquierda:
                        nodo = nodo.padre
                        self._rotacion_derecha(nodo)
                    nodo.padre.color = "negro"
                    nodo.padre.padre.color = "rojo"
                    self._rotacion_izquierda(nodo.padre.padre)

        self.raiz.color = "negro"

    def _rotacion_izquierda(self, nodo):
        nodo_derecha = nodo.derecha
        nodo.derecha = nodo_derecha.izquierda
        if nodo_derecha.izquierda != self.nil:
            nodo_derecha.izquierda.padre = nodo
        nodo_derecha.padre = nodo.padre
        if nodo.padre is None:
            self.raiz = nodo_derecha
        elif nodo == nodo.padre.izquierda:
            nodo.padre.izquierda = nodo_derecha
        else:
            nodo.padre.derecha = nodo_derecha
        if nodo.padre is not None:  # add check for parent node
            nodo.padre.altura = 1 + max(self.altura(nodo.padre.izquierda), self.altura(nodo.padre.derecha))
        nodo_derecha.izquierda = nodo
        nodo.padre = nodo_derecha
        nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))
        nodo_derecha.altura = 1 + max(self.altura(nodo_derecha.izquierda), self.altura(nodo_derecha.derecha))

    def _rotacion_derecha(self, nodo):
        nodo_izquierda = nodo.izquierda
        nodo.izquierda = nodo_izquierda.derecha
        if nodo_izquierda.derecha != self.nil:
            nodo_izquierda.derecha.padre = nodo
        nodo_izquierda.padre = nodo.padre
        if nodo.padre is None:
            self.raiz = nodo_izquierda
        elif nodo == nodo.padre.derecha:
            nodo.padre.derecha = nodo_izquierda
        else:
            nodo.padre.izquierda = nodo_izquierda
        if nodo.padre is not None:  # add check for parent node
            nodo.padre.altura = 1 + max(self.altura(nodo.padre.izquierda), self.altura(nodo.padre.derecha))
        nodo_izquierda.derecha = nodo
        nodo.padre = nodo_izquierda
        nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))
        nodo_izquierda.altura = 1 + max(self.altura(nodo_izquierda.izquierda), self.altura(nodo_izquierda.derecha))

    def altura(self, nodo):
        if nodo == self.nil:
            return 0
        return nodo.altura

    def imprimir(self):
        self._imprimir(self.raiz)

    def _imprimir(self, nodo):
        if nodo != self.nil:
            self._imprimir(nodo.izquierda)
            print(nodo.valor, nodo.color)
            self._imprimir(nodo.derecha)

    def _arreglar_insercion(self, nodo):
        while nodo.padre is not None and nodo.padre.color == "rojo":
            if nodo.padre == nodo.padre.padre.izquierda:
                nodo_tio = nodo.padre.padre.derecha
                if nodo_tio.color == "rojo":
                    nodo.padre.color = "negro"
                    nodo_tio.color = "negro"
                    nodo.padre.padre.color = "rojo"
                    nodo = nodo.padre.padre
                else:
                    if nodo == nodo.padre.derecha:
                        nodo = nodo.padre
                        self._rotacion_izquierda(nodo)
                    nodo.padre.color = "negro"
                    nodo.padre.padre.color = "rojo"
                    self._rotacion_derecha(nodo.padre.padre)
            else:
                nodo_tio = nodo.padre.padre.izquierda
                if nodo_tio.color == "rojo":
                    nodo.padre.color = "negro"
                    nodo_tio.color = "negro"
                    nodo.padre.padre.color = "rojo"
                    nodo = nodo.padre.padre
                else:
                    if nodo == nodo.padre.izquierda:
                        nodo = nodo.padre
                        self._rotacion_derecha(nodo)
                    nodo.padre.color = "negro"
                    nodo.padre.padre.color = "rojo"
                    self._rotacion_izquierda(nodo.padre.padre)
    
        self.raiz.color = "negro"


if __name__ == "__main__":
    arbol = RN()
    arbol.insertar(5)
    arbol.insertar(2)
    arbol.insertar(7)
    arbol.insertar(1)
    arbol.insertar(3)
    arbol.insertar(6)
    arbol.insertar(8)
    arbol.insertar(4)
    arbol.imprimir()