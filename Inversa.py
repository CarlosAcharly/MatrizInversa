def matriz_inversa(matriz):
    n = len(matriz)
    
    # Crear una matriz identidad del mismo tamaño que la matriz original
    identidad = [[float(i == j) for i in range(n)] for j in range(n)]
    
        # Realizar el algoritmo de Gauss-Jordan
    for i in range(n):
        # Asegurarse de que el pivote no sea cero
        if matriz[i][i] == 0:
            for j in range(i + 1, n):
                if matriz[j][i] != 0:
                    # Intercambiar filas
                    matriz[i], matriz[j] = matriz[j], matriz[i]
                    identidad[i], identidad[j] = identidad[j], identidad[i]
                    break
            else:
                raise ValueError("La matriz no es invertible.")
        
        # Normalizar la fila para que el elemento diagonal sea 1
        factor = matriz[i][i]
        for j in range(n):
            matriz[i][j] /= factor
            identidad[i][j] /= factor
        
        # Hacer ceros en la columna actual, excepto en la fila del pivote
        for j in range(n):
            if i != j:
                factor = matriz[j][i]
                for k in range(n):
                    matriz[j][k] -= factor * matriz[i][k]
                    identidad[j][k] -= factor * identidad[i][k]
    
    return identidad

def crear_matriz_desde_teclado(filas, columnas):
    matriz = []
    print(f"Ingrese los elementos de la matriz ({filas}x{columnas}):")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Elemento [{i+1}][{j+1}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

# Solicitar dimensiones de la matriz
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Crear la matriz desde el teclado
matriz = crear_matriz_desde_teclado(filas, columnas)

# Verificar si la matriz es cuadrada para intentar calcular la inversa
if filas != columnas:
    print("La matriz no es cuadrada, por lo tanto, no es invertible.")
else:
    try:
        identidad = [[float(i == j) for i in range(filas)] for j in range(filas)]
        inversa = matriz_inversa([row[:] for row in matriz])  # Crear una copia para no modificar la original

        # Mostrar la matriz original, identidad y la inversa
        print("\nMatriz Original:") 
        for fila in matriz:
            print(fila)
        
        print("\nMatriz Identidad:")
        for fila in identidad:
            print(fila)
        
        print("\nMatriz Inversa:")
        for fila in inversa:
            print(fila)
            
    except ValueError as e:
        print(e)
