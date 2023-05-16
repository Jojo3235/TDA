class NodoMatriz(object):
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.sig_fila = None
        self.sig_columna = None


class Matriz(object):
    def __init__(self):
        self.inicio = None
        self.filas = 0
        self.columnas = 0

    def insertar(self, fila, columna, valor):
        nuevo_nodo = NodoMatriz(fila, columna, valor)

        if self.inicio is None:
            self.inicio = nuevo_nodo
            self.filas = max(self.filas, fila + 1)
            self.columnas = max(self.columnas, columna + 1)
            return

        nodo_actual = self.inicio
        nodo_anterior = None

        while nodo_actual is not None:
            if nodo_actual.fila == fila and nodo_actual.columna == columna:
                nodo_actual.valor = valor
                return

            if nodo_actual.fila > fila or (nodo_actual.fila == fila and nodo_actual.columna > columna):
                break

            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.sig_columna

        if nodo_actual is None:
            nodo_anterior.sig_columna = nuevo_nodo
        else:
            nuevo_nodo.sig_columna = nodo_actual
            if nodo_anterior is None:
                self.inicio = nuevo_nodo
            else:
                nodo_anterior.sig_columna = nuevo_nodo

        nodo_actual = self.inicio
        nodo_anterior = None

        while nodo_actual is not None:
            if nodo_actual.fila == fila and nodo_actual.columna == columna:
                nodo_actual.valor = valor
                return

            if nodo_actual.columna > columna or (nodo_actual.columna == columna and nodo_actual.fila > fila):
                break

            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.sig_fila

        if nodo_actual is None:
            nodo_anterior.sig_fila = nuevo_nodo
        else:
            nuevo_nodo.sig_fila = nodo_actual
            if nodo_anterior is None:
                self.inicio = nuevo_nodo
            else:
                nodo_anterior.sig_fila = nuevo_nodo

        self.filas = max(self.filas, fila + 1)
        self.columnas = max(self.columnas, columna + 1)

    def eliminar(self, fila, columna):
        nodo_actual = self.inicio
        nodo_anterior = None

        while nodo_actual is not None:
            if nodo_actual.fila == fila and nodo_actual.columna == columna:
                if nodo_anterior is None:
                    self.inicio = nodo_actual.sig_columna
                else:
                    nodo_anterior.sig_columna = nodo_actual.sig_columna

                nodo_actual = None
                break

            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.sig_columna

        nodo_actual = self.inicio
        nodo_anterior = None

        while nodo_actual is not None:
            if nodo_actual.fila == fila and nodo_actual.columna == columna:
                if nodo_anterior is None:
                    self.inicio = nodo_actual.sig_fila
                else:
                    nodo_anterior.sig_fila = nodo_actual.sig_fila

                nodo_actual = None
                break

            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.sig_fila

    def obtener_valor(self, fila, columna):
        nodo_actual = self.inicio

        while nodo_actual is not None:
            if nodo_actual.fila == fila and nodo_actual.columna == columna:
                return nodo_actual.valor

            nodo_actual = nodo_actual.sig_columna

        return None
    
    def obtener_fila(self, fila):
        nodo_actual = self.inicio
        fila = []

        while nodo_actual is not None:
            if nodo_actual.fila == fila:
                fila.append(nodo_actual.valor)

            nodo_actual = nodo_actual.sig_columna

        return fila
    
    def obtener_columna(self, columna):
        nodo_actual = self.inicio
        columna = []

        while nodo_actual is not None:
            if nodo_actual.columna == columna:
                columna.append(nodo_actual.valor)

            nodo_actual = nodo_actual.sig_fila

        return columna
    
    def obtener_diagonal_principal(self):
        nodo_actual = self.inicio
        diagonal = []

        while nodo_actual is not None:
            if nodo_actual.fila == nodo_actual.columna:
                diagonal.append(nodo_actual.valor)

            nodo_actual = nodo_actual.sig_columna

        return diagonal
    
    def obtener_diagonal_secundaria(self):
        nodo_actual = self.inicio
        diagonal = []

        while nodo_actual is not None:
            if nodo_actual.fila + nodo_actual.columna == self.filas - 1:
                diagonal.append(nodo_actual.valor)

            nodo_actual = nodo_actual.sig_columna

        return diagonal
    
    def obtener_transpuesta(self):
        nodo_actual = self.inicio
        transpuesta = Matriz()

        while nodo_actual is not None:
            transpuesta.insertar(nodo_actual.columna, nodo_actual.fila, nodo_actual.valor)

            nodo_actual = nodo_actual.sig_columna

        return transpuesta
    
    def sumar(self, matriz):
        if self.filas != matriz.filas or self.columnas != matriz.columnas:
            return None

        resultado = Matriz()

        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.insertar(i, j, self.obtener_valor(i, j) + matriz.obtener_valor(i, j))

        return resultado
    
    def restar(self, matriz):
        if self.filas != matriz.filas or self.columnas != matriz.columnas:
            return None

        resultado = Matriz()

        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.insertar(i, j, self.obtener_valor(i, j) - matriz.obtener_valor(i, j))

        return resultado

    #calcular determinante con el metodo de strassen, para ello aumentar a matriz con filas y columnas de potencia de 2
    def determinante_strassen(self):
        if self.filas != self.columnas:
            return None

        #aumentar matriz a potencia de 2
        potencia = 1
        while potencia < self.filas:
            potencia *= 2

        matriz_aumentada = Matriz()

        for i in range(potencia):
            for j in range(potencia):
                if i < self.filas and j < self.columnas:
                    matriz_aumentada.insertar(i, j, self.obtener_valor(i, j))
                else:
                    matriz_aumentada.insertar(i, j, 0)

        return matriz_aumentada.determinante_strassen_aux()
    
    def determinante_strassen_aux(self):
        if self.filas == 1:
            return self.obtener_valor(0, 0)

        a = Matriz()
        b = Matriz()
        c = Matriz()
        d = Matriz()

        for i in range(self.filas):
            for j in range(self.columnas):
                if i < self.filas // 2 and j < self.columnas // 2:
                    a.insertar(i, j, self.obtener_valor(i, j))
                elif i < self.filas // 2 and j >= self.columnas // 2:
                    b.insertar(i, j - self.columnas // 2, self.obtener_valor(i, j))
                elif i >= self.filas // 2 and j < self.columnas // 2:
                    c.insertar(i - self.filas // 2, j, self.obtener_valor(i, j))
                elif i >= self.filas // 2 and j >= self.columnas // 2:
                    d.insertar(i - self.filas // 2, j - self.columnas // 2, self.obtener_valor(i, j))

        m1 = a.determinante_strassen_aux()
        m2 = b.determinante_strassen_aux()
        m3 = c.determinante_strassen_aux()
        m4 = d.determinante_strassen_aux()

        return m1 * m4 - m2 * m3
    
    def __str__(self):
        nodo_actual = self.inicio
        matriz = ''

        #cuando se han insertando n valores, siendo n = numero de columnas, se pasa a la siguiente fila, con \n
        contador = 0

        while nodo_actual is not None:
            if contador == self.columnas:
                matriz += '\n'
                contador = 0

            matriz += str(nodo_actual.valor) + ' '
            contador += 1

            nodo_actual = nodo_actual.sig_columna

        return matriz
    
    
matriz = Matriz()
matriz.insertar(0, 0, 1)
matriz.insertar(0, 1, 2)
matriz.insertar(0, 2, 3)

matriz.insertar(1, 0, 4)
matriz.insertar(1, 1, 5)
matriz.insertar(1, 2, 6)

matriz.insertar(2, 0, 7)
matriz.insertar(2, 1, 8)
matriz.insertar(2, 2, 9)

n = matriz.determinante_strassen()

print(matriz)

print(n)