import random 

# Validar los campos
def validar_campos(prompt):
    while True:
        valor = input(prompt)
        try:
            numero_entero = int(valor)
            if numero_entero > 0:
                return numero_entero
            else:
                print("Error: Ingresa un número entero mayor que 0.")
        except ValueError:
            print("Error: Ingresa solo números enteros.")

size = validar_campos("Introduce el tamaño de la matriz: ")

#Creamos la matriz
def crear_matriz(size):
    matriz = []
    suma_filas = []
    suma_columnas = []
    
    for f in range(size):
        fila = []
        for c in range(size):
            n_random = random.randint(0, 9)
            
            if len(suma_filas)-1 < f: suma_filas.append(n_random)
            else: suma_filas[f] = suma_filas[f] + n_random
            
            if f == 0: suma_columnas.append(n_random)
            else: suma_columnas[c] = suma_columnas[c] + n_random
            
            fila.append(n_random)
        matriz.append(fila)
        
    return {
        "matriz": matriz, 
        "suma_filas": suma_filas,
        "suma_columnas": suma_columnas
    }

resultado = crear_matriz(size)
print ("Matriz de numeros:", resultado["matriz"])

# Imprimir las sumas de cada fila
print("Sumas de cada fila:", resultado["suma_filas"])


# Imprimir las sumas de cada columna
print("Sumas de cada columna:", resultado["suma_columnas"])
