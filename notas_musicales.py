import numpy as np

# Clase para representar una nota musical
class NotaMusical:
    def __init__(self, nombre, frecuencia):
        self.nombre = nombre
        self.frecuencia = frecuencia

    def __str__(self):
        return f"{self.nombre} ({self.frecuencia} Hz)"

# Definimos la matriz de notas musicales con frecuencias (3x3)
notas_matriz = np.array([
    [NotaMusical("Do", 261.63), NotaMusical("Re", 293.66), NotaMusical("Mi", 329.63)],
    [NotaMusical("Fa", 349.23), NotaMusical("Sol", 392.00), NotaMusical("La", 440.00)],
    [NotaMusical("Si", 493.88), NotaMusical("Do", 523.25), NotaMusical("Re", 587.33)]
])

# Definimos un vector de notas adicionales
notas_vector = [
    NotaMusical("Mi", 329.63),
    NotaMusical("Fa", 349.23),
    NotaMusical("Sol", 392.00),
    NotaMusical("La", 440.00),
    NotaMusical("Si", 493.88)
]

# Función para imprimir la matriz y el vector
def imprimir_datos():
    print("Matriz de notas:")
    for fila in notas_matriz:
        print(" | ".join(str(nota) for nota in fila))

    print("\nVector de notas adicionales:")
    for nota in notas_vector:
        print(nota)

# Función de búsqueda en la matriz
def buscar_nota_en_matriz(nombre):
    for i in range(notas_matriz.shape[0]):
        for j in range(notas_matriz.shape[1]):
            if notas_matriz[i][j].nombre == nombre:
                return f"Nota '{nombre}' encontrada en la posición ({i}, {j}) de la matriz."
    return f"Nota '{nombre}' no encontrada en la matriz."

# Función de búsqueda en el vector
def buscar_nota_en_vector(nombre):
    for nota in notas_vector:
        if nota.nombre == nombre:
            return f"Nota '{nombre}' encontrada en el vector con frecuencia {nota.frecuencia} Hz."
    return f"Nota '{nombre}' no encontrada en el vector."

# Algoritmo de ordenamiento burbuja bidireccional (Cocktail Sort) para el vector
def cocktail_sort(lista):
    n = len(lista)
    inicio = 0
    fin = n - 1
    while inicio < fin:
        # Bucle hacia adelante (similar a burbuja)
        for i in range(inicio, fin):
            if lista[i].frecuencia > lista[i + 1].frecuencia:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
        fin -= 1

        # Bucle hacia atrás
        for i in range(fin, inicio, -1):
            if lista[i].frecuencia < lista[i - 1].frecuencia:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
        inicio += 1

# Funciones para agregar y eliminar notas del vector
def agregar_nota_a_vector(nombre, frecuencia):
    notas_vector.append(NotaMusical(nombre, frecuencia))
    print(f"Nota '{nombre}' ({frecuencia} Hz) agregada al vector.")

def eliminar_nota_del_vector(nombre):
    for nota in notas_vector:
        if nota.nombre == nombre:
            notas_vector.remove(nota)
            print(f"Nota '{nombre}' eliminada del vector.")
            return
    print(f"Nota '{nombre}' no encontrada en el vector para eliminar.")

# Funciones de manejo de archivos .txt
def guardar_notas_en_txt():
    with open("notas_musicales.txt", "w") as archivo:
        for nota in notas_vector:
            archivo.write(f"{nota.nombre} ({nota.frecuencia} Hz)\n")
    print("Notas guardadas en 'notas_musicales.txt'.")

def leer_notas_desde_txt():
    try:
        with open("notas_musicales.txt", "r") as archivo:
            lineas = archivo.readlines()
            return [linea.strip() for linea in lineas]
    except FileNotFoundError:
        return "El archivo 'notas_musicales.txt' no se encuentra."

# Imprimir datos iniciales
imprimir_datos()

# Buscar una nota en la matriz y en el vector
nota_a_buscar = "Do"
print(buscar_nota_en_matriz(nota_a_buscar))
print(buscar_nota_en_vector(nota_a_buscar))

# Ordenar el vector con Cocktail Sort
print("\nOrdenando el vector de notas...")
cocktail_sort(notas_vector)
print("Vector de notas ordenado:")
for nota in notas_vector:
    print(nota)

# Agregar y eliminar notas
agregar_nota_a_vector("Do", 261.63)
eliminar_nota_del_vector("Mi")

# Guardar y leer desde archivos .txt
guardar_notas_en_txt()
print("\nNotas leídas desde el archivo .txt:")
print(leer_notas_desde_txt())