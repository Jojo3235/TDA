class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class AVL:
    def __init__(self):
        self.raiz = None

    def altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def balance(self, nodo):
        if not nodo:
            return 0
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha)

    def rotacion_izquierda(self, nodo):
        nueva_raiz = nodo.derecha
        nodo.derecha = nueva_raiz.izquierda
        nueva_raiz.izquierda = nodo
        nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))
        nueva_raiz.altura = 1 + max(self.altura(nueva_raiz.izquierda), self.altura(nueva_raiz.derecha))
        return nueva_raiz

    def rotacion_derecha(self, nodo):
        nueva_raiz = nodo.izquierda
        nodo.izquierda = nueva_raiz.derecha
        nueva_raiz.derecha = nodo
        nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))
        nueva_raiz.altura = 1 + max(self.altura(nueva_raiz.izquierda), self.altura(nueva_raiz.derecha))
        return nueva_raiz

    def insertar(self, valor):
        def _insertar(nodo, valor):
            if not nodo:
                return NodoAVL(valor)
            elif valor < nodo.valor:
                nodo.izquierda = _insertar(nodo.izquierda, valor)
            else:
                nodo.derecha = _insertar(nodo.derecha, valor)

            nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))
            balance = self.balance(nodo)

            if balance > 1 and valor < nodo.izquierda.valor:
                return self.rotacion_derecha(nodo)

            if balance < -1 and valor > nodo.derecha.valor:
                return self.rotacion_izquierda(nodo)

            if balance > 1 and valor > nodo.izquierda.valor:
                nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
                return self.rotacion_derecha(nodo)

            if balance < -1 and valor < nodo.derecha.valor:
                nodo.derecha = self.rotacion_derecha(nodo.derecha)
                return self.rotacion_izquierda(nodo)

            return nodo

        self.raiz = _insertar(self.raiz, valor)

    def eliminar(self, valor):
        def _eliminar(nodo, valor):
            if not nodo:
                return nodo
            elif valor < nodo.valor:
                nodo.izquierda = _eliminar(nodo.izquierda, valor)
            elif valor > nodo.valor:
                nodo.derecha = _eliminar(nodo.derecha, valor)
            else:
                if not nodo.izquierda:
                    return nodo.derecha
                elif not nodo.derecha:
                    return nodo.izquierda
                else:
                    nodo.valor = self.minimo(nodo.derecha)
                    nodo.derecha = _eliminar(nodo.derecha, nodo.valor)

            nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))
            balance = self.balance(nodo)

            if balance > 1 and self.balance(nodo.izquierda) >= 0:
                return self.rotacion_derecha(nodo)

            if balance < -1 and self.balance(nodo.derecha) <= 0:
                return self.rotacion_izquierda(nodo)

            if balance > 1 and self.balance(nodo.izquierda) < 0:
                nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
                return self.rotacion_derecha(nodo)

            if balance < -1 and self.balance(nodo.derecha) > 0:
                nodo.derecha = self.rotacion_derecha(nodo.derecha)
                return self.rotacion_izquierda(nodo)

            return nodo

        self.raiz = _eliminar(self.raiz, valor)

    def minimo(self, nodo):
        if nodo.izquierda:
            return self.minimo(nodo.izquierda)
        return nodo.valor
    
    def preorden(self):
        def _preorden(nodo):
            if nodo:
                print(nodo.valor, end=' ')
                _preorden(nodo.izquierda)
                _preorden(nodo.derecha)
        _preorden(self.raiz)
        print()

    def inorden(self):
        def _inorden(nodo):
            if nodo:
                _inorden(nodo.izquierda)
                print(nodo.valor, end=' ')
                _inorden(nodo.derecha)
        _inorden(self.raiz)
        print()

    def postorden(self):
        def _postorden(nodo):
            if nodo:
                _postorden(nodo.izquierda)
                _postorden(nodo.derecha)
                print(nodo.valor, end=' ')
        _postorden(self.raiz)
        print()

    def __str__(self):
        def _str(nodo):
            if not nodo:
                return 'None'
            return f'{nodo.valor}({str(_str(nodo.izquierda))}, {str(_str(nodo.derecha))})'
        return _str(self.raiz)

if __name__ == '__main__':
    arbol = AVL()
    arbol.insertar(10)
    arbol.insertar(20)
    arbol.insertar(30)
    arbol.insertar(40)
    arbol.insertar(50)
    arbol.insertar(25)
    arbol.preorden()
    arbol.inorden()
    arbol.postorden()
    arbol.eliminar(30)
    arbol.preorden()
    arbol.inorden()
    arbol.postorden()
    print(arbol)
    arbol.eliminar(40)
    arbol.preorden()
    print(arbol)