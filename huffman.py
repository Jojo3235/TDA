class NodoHuffman:
    def __init__(self, caracter=None, frecuencia=0):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

def construir_arbol_huffman(tabla):
    nodos = [NodoHuffman(caracter, frecuencia) for caracter, frecuencia in tabla]
    
    while len(nodos) > 1:
        nodos = sorted(nodos, key=lambda nodo: nodo.frecuencia)
        nuevo_nodo = NodoHuffman()
        nuevo_nodo.izquierda = nodos[0]
        nuevo_nodo.derecha = nodos[1]
        nuevo_nodo.frecuencia = nodos[0].frecuencia + nodos[1].frecuencia
        nodos = nodos[2:]
        nodos.append(nuevo_nodo)
    
    return nodos[0]

def generar_tabla_codigos(raiz, codigo_actual, tabla_codigos):
    if raiz.caracter:
        tabla_codigos[raiz.caracter] = codigo_actual
    else:
        generar_tabla_codigos(raiz.izquierda, codigo_actual + "0", tabla_codigos)
        generar_tabla_codigos(raiz.derecha, codigo_actual + "1", tabla_codigos)

def decodificar_huffman(codigo, tabla_codigos):
    codigo_actual = ""
    texto_decodificado = ""
    
    for bit in codigo:
        codigo_actual += bit
        for caracter, codigo in tabla_codigos.items():
            if codigo_actual == codigo:
                texto_decodificado += caracter
                codigo_actual = ""
                break
    
    return texto_decodificado

# Tabla de caracteres y códigos correspondientes
tabla = [
    ('I', 0.28),
    ('N', 0.16),
    ('T', 0.08),
    ('E', 0.16),
    ('L', 0.08),
    ('G', 0.08),
    ('C', 0.08),
    ('A', 0.08)
]

# Construir el árbol de Huffman
raiz_huffman = construir_arbol_huffman(tabla)

# Generar la tabla de códigos
tabla_codigos = {}
generar_tabla_codigos(raiz_huffman, "", tabla_codigos)

# Código a decodificar
codigo = "10110010011001100000111101111101110"

# Decodificar el código utilizando la tabla de códigos
texto_decodificado = decodificar_huffman(codigo, tabla_codigos)

# Imprimir el resultado
print("Texto decodificado:", texto_decodificado)
