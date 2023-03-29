from listas_enlazadas import LinkedList

class Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.matrix = []
        for i in range(m):
            row = LinkedList()
            for j in range(n):
                row.insert(None)
            self.matrix.append(row)

    def set_value(self, i, j, value):
        self.matrix[i].set(j, value)

    def get_value(self, i, j):
        return self.matrix[i].get(j)

    def print_matrix(self):
        for i in range(self.m):
            row = ''
            for j in range(self.n):
                row += str(self.get_value(i, j)) + ' '
            print(row)
    
    def strassen_determinante(matrix):
        if matrix.m != matrix.n:
            raise ValueError("La matriz debe ser cuadrada")
        if matrix.m == 1:
            return matrix.get_value(0, 0)
        if matrix.m == 2:
            return matrix.get_value(0, 0) * matrix.get_value(1, 1) - matrix.get_value(0, 1) * matrix.get_value(1, 0)
        if matrix.m == 3:
            return matrix.get_value(0, 0) * matrix.get_value(1, 1) * matrix.get_value(2, 2) + matrix.get_value(0, 1) * matrix.get_value(1, 2) * matrix.get_value(2, 0) + matrix.get_value(0, 2) * matrix.get_value(1, 0) * matrix.get_value(2, 1) - matrix.get_value(0, 2) * matrix.get_value(1, 1) * matrix.get_value(2, 0) - matrix.get_value(0, 0) * matrix.get_value(1, 2) * matrix.get_value(2, 1) - matrix.get_value(0, 1) * matrix.get_value(1, 0) * matrix.get_value(2, 2)
        else:
            a = Matrix(matrix.m // 2, matrix.n // 2)
            b = Matrix(matrix.m // 2, matrix.n // 2)
            c = Matrix(matrix.m // 2, matrix.n // 2)
            d = Matrix(matrix.m // 2, matrix.n // 2)
            for i in range(matrix.m // 2):
                for j in range(matrix.n // 2):
                    a.set_value(i, j, matrix.get_value(i, j))
                    b.set_value(i, j, matrix.get_value(i, j + matrix.n // 2))
                    c.set_value(i, j, matrix.get_value(i + matrix.m // 2, j))
                    d.set_value(i, j, matrix.get_value(i + matrix.m // 2, j + matrix.n // 2))
            p1 = Matrix.strassen_determinante(a)
            p2 = Matrix.strassen_determinante(b)
            p3 = Matrix.strassen_determinante(c)
            p4 = Matrix.strassen_determinante(d)
            return p1 * p4 - p2 * p3
        


matriz = Matrix(3, 3)
matriz.set_value(0, 0, 2)
matriz.set_value(0, 1, 2)
matriz.set_value(0, 2, 2)
matriz.set_value(1, 0, 3)
matriz.set_value(1, 1, 2)
matriz.set_value(1, 2, 2)
matriz.set_value(2, 0, 1)
matriz.set_value(2, 1, 0)
matriz.set_value(2, 2, 2)

matriz.print_matrix()

print(Matrix.strassen_determinante(matriz))

#Crear otra matriz de 8x8 y calcular su determinante con el algoritmo de Strassen

matriz2 = Matrix(8, 8)

import random

matriz2.set_value(0, 0, random.randint(0, 100))
matriz2.set_value(0, 1, random.randint(0, 100))
matriz2.set_value(0, 2, random.randint(0, 100))
matriz2.set_value(0, 3, random.randint(0, 100))
matriz2.set_value(0, 4, random.randint(0, 100))
matriz2.set_value(0, 5, random.randint(0, 100))
matriz2.set_value(0, 6, random.randint(0, 100))
matriz2.set_value(0, 7, random.randint(0, 100))
matriz2.set_value(1, 0, random.randint(0, 100))
matriz2.set_value(1, 1, random.randint(0, 100))
matriz2.set_value(1, 2, random.randint(0, 100))
matriz2.set_value(1, 3, random.randint(0, 100))
matriz2.set_value(1, 4, random.randint(0, 100))
matriz2.set_value(1, 5, random.randint(0, 100))
matriz2.set_value(1, 6, random.randint(0, 100))
matriz2.set_value(1, 7, random.randint(0, 100))
matriz2.set_value(2, 0, random.randint(0, 100))
matriz2.set_value(2, 1, random.randint(0, 100))
matriz2.set_value(2, 2, random.randint(0, 100))
matriz2.set_value(2, 3, random.randint(0, 100))
matriz2.set_value(2, 4, random.randint(0, 100))
matriz2.set_value(2, 5, random.randint(0, 100))
matriz2.set_value(2, 6, random.randint(0, 100))
matriz2.set_value(2, 7, random.randint(0, 100))
matriz2.set_value(3, 0, random.randint(0, 100))
matriz2.set_value(3, 1, random.randint(0, 100))
matriz2.set_value(3, 2, random.randint(0, 100))
matriz2.set_value(3, 3, random.randint(0, 100))
matriz2.set_value(3, 4, random.randint(0, 100))
matriz2.set_value(3, 5, random.randint(0, 100))
matriz2.set_value(3, 6, random.randint(0, 100))
matriz2.set_value(3, 7, random.randint(0, 100))
matriz2.set_value(4, 0, random.randint(0, 100))
matriz2.set_value(4, 1, random.randint(0, 100))
matriz2.set_value(4, 2, random.randint(0, 100))
matriz2.set_value(4, 3, random.randint(0, 100))
matriz2.set_value(4, 4, random.randint(0, 100))
matriz2.set_value(4, 5, random.randint(0, 100))
matriz2.set_value(4, 6, random.randint(0, 100))
matriz2.set_value(4, 7, random.randint(0, 100))
matriz2.set_value(5, 0, random.randint(0, 100))
matriz2.set_value(5, 1, random.randint(0, 100))
matriz2.set_value(5, 2, random.randint(0, 100))
matriz2.set_value(5, 3, random.randint(0, 100))
matriz2.set_value(5, 4, random.randint(0, 100))
matriz2.set_value(5, 5, random.randint(0, 100))
matriz2.set_value(5, 6, random.randint(0, 100))
matriz2.set_value(5, 7, random.randint(0, 100))
matriz2.set_value(6, 0, random.randint(0, 100))
matriz2.set_value(6, 1, random.randint(0, 100))
matriz2.set_value(6, 2, random.randint(0, 100))
matriz2.set_value(6, 3, random.randint(0, 100))
matriz2.set_value(6, 4, random.randint(0, 100))
matriz2.set_value(6, 5, random.randint(0, 100))
matriz2.set_value(6, 6, random.randint(0, 100))
matriz2.set_value(6, 7, random.randint(0, 100))
matriz2.set_value(7, 0, random.randint(0, 100))
matriz2.set_value(7, 1, random.randint(0, 100))
matriz2.set_value(7, 2, random.randint(0, 100))
matriz2.set_value(7, 3, random.randint(0, 100))
matriz2.set_value(7, 4, random.randint(0, 100))
matriz2.set_value(7, 5, random.randint(0, 100))
matriz2.set_value(7, 6, random.randint(0, 100))
matriz2.set_value(7, 7, random.randint(0, 100))

print("Matriz 1")
matriz.print_matrix()
print("Matriz 2")
matriz2.print_matrix()

#determinante matriz

print(matriz2.strassen_determinante())

matriz3 = Matrix(4,4)

