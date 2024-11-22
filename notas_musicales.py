import numpy as np

# Definimos la matriz de notas musicales (3x3)
notas_matriz = np.array([
    ["Do", "Re", "Mi"],
    ["Fa", "Sol", "La"],
    ["Si", "Do", "Re"]
])

# Definimos un vector de notas adicionales
notas_vector = ["Mi", "Fa", "Sol", "La", "Si"]

# Función para imprimir la matriz y el vector
def imprimir_datos():
    print("Matriz de notas:")
    print(notas_matriz)
    print("\nVector de notas adicionales:")
    print(notas_vector)

# Función de búsqueda secuencial en la matriz
def buscar_nota_en_matriz(nota):
    for i in range(notas_matriz.shape[0]):
        for j in range(notas_matriz.shape[1]):
            if notas_matriz[i][j] == nota:
                return f"Nota '{nota}' encontrada en la posición ({i}, {j}) de la matriz."
    return f"Nota '{nota}' no encontrada en la matriz."

# Función de búsqueda en el vector
def buscar_nota_en_vector(nota):
    if nota in notas_vector:
        return f"Nota '{nota}' encontrada en el vector."
    else:
        return f"Nota '{nota}' no encontrada en el vector."

# Algoritmo de ordenamiento burbuja bidireccional (Cocktail Sort) para el vector
def cocktail_sort(lista):
    n = len(lista)
    inicio = 0
    fin = n - 1
    while inicio < fin:
        # Bucle hacia adelante (similar a burbuja)
        for i in range(inicio, fin):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
        fin -= 1

        # Bucle hacia atrás
        for i in range(fin, inicio, -1):
            if lista[i] < lista[i - 1]:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
        inicio += 1

# Funciones para agregar y eliminar notas del vector
def agregar_nota_a_vector(nota):
    notas_vector.append(nota)
    print(f"Nota '{nota}' agregada al vector.")

def eliminar_nota_del_vector(nota):
    if nota in notas_vector:
        notas_vector.remove(nota)
        print(f"Nota '{nota}' eliminada del vector.")
    else:
        print(f"Nota '{nota}' no encontrada en el vector para eliminar.")

# Funciones de manejo de archivos .txt
def guardar_notas_en_txt():
    with open("notas_musicales.txt", "w") as archivo:
        for nota in notas_vector:
            archivo.write(nota + "\n")
    print("Notas guardadas en 'notas_musicales.txt'.")

def leer_notas_desde_txt():
    try:
        with open("notas_musicales.txt", "r") as archivo:
            notas_leidas = archivo.readlines()
            return [nota.strip() for nota in notas_leidas]  # Eliminar saltos de línea
    except FileNotFoundError:
        return "El archivo 'notas_musicales.txt' no se encuentra."

# Imprimir datos iniciales
imprimir_datos()

# Buscar una nota en la matriz y en el vector
nota_a_buscar = "Do"
print(buscar_nota_en_matriz(nota_a_buscar))
print(buscar_nota_en_vector(nota_a_buscar))

# Ordenamos el vector con Cocktail Sort
print("\nOrdenando el vector de notas...")
cocktail_sort(notas_vector)
print("Vector de notas ordenado:")
print(notas_vector)

# Agregar y eliminar notas
agregar_nota_a_vector("Do")
eliminar_nota_del_vector("Mi")

# Guardar y leer desde archivos .txt
guardar_notas_en_txt()
print("\nNotas leídas desde el archivo .txt:")
print(leer_notas_desde_txt())