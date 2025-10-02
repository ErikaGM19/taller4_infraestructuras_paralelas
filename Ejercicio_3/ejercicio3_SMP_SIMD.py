# SE IMPORTAN LAS LIBRERÍAS NECESARIAS:
import random
import time
import numpy
import threading

# SE FIJA UNA SEMILLA PARA LA GENERACIÓN DE VALORES ALEATORIOS:
random.seed(42) 

# SE CREA UNA FUNCIÓN PARA GENERAR LA MATRIZ INICIAL:
def generar_matriz(filas, columnas):
    return [[random.randint(0, 9) for _ in range(columnas)] for _ in range(filas)]

# SE CREA UNA FUNCIÓN PARA REALIZAR LA SUMA SENCUENCIAL DE LOS VALORES DE LA MATRIZ:
def suma_bloque_filas(matriz):
    suma = numpy.sum(matriz, axis=1)
    return suma

# SE CREA UNA FUNCIÓN QUE DIVIDA UNA MATRIZ EN BLOQUES Y LES ASIGNE UN ÍNDICE:
def generar_bloques(matriz, indice, tam_bloque):
    n_columnas = len(matriz[0])
    
    # Calcular cuántos bloques hay en una fila
    bloques_por_fila = n_columnas // tam_bloque
    
    # Calcular fila y columna del bloque
    bloque_fila = indice // bloques_por_fila
    bloque_col = indice % bloques_por_fila
    
    # Límites del bloque en la matriz
    fila_inicio = bloque_fila * tam_bloque
    fila_fin = fila_inicio + tam_bloque
    col_inicio = bloque_col * tam_bloque
    col_fin = col_inicio + tam_bloque
    
    # Extraer bloque
    return [fila[col_inicio:col_fin] for fila in matriz[fila_inicio:fila_fin]]

# SE DEFINE UNA FUNCIÓN PARA PASAR COMO TARGET A LOS HILOS:
def funcion_target(matriz, indice, tam_bloque, vector_sumas):
    bloque = generar_bloques(matriz, indice, tam_bloque)
    suma_bloque =  suma_bloque_filas(bloque)
    vector_sumas.append(suma_bloque)

# SE DEFINE LA FUNCIÓN PRINCIPAL DONDE SE EJECUTARÁN LAS FUNCIONES:
def main():

    # Se definen los parámetros para crear la matríz:
    filas = 10000
    columnas = 10000

    # Se definen los parámetros para crear los bloques:
    tam_bloques = 1000
    num_bloques = 100      

    # Se crea un arreglo para almacenar las sumas parciales:
    sum_parciales = []      

    # Se crea un arreglo para almacenar los hilos:
    hilos = []

    # Se crea la matriz con las dimensiones definidas anteriormente:
    matriz = generar_matriz(filas, columnas)

    # Se inicia el conteo del tiempo de ejecución:
    print(f" Se inicia la suma de los elementos de una matriz {filas}x{columnas} \n")
    inicio = time.time()

    # En esta parte se implementan los hilos para la ejecución del código:
    for i in range(0, num_bloques):
        hilo = threading.Thread(target=funcion_target, args=(matriz, i, tam_bloques, sum_parciales))
        hilos.append(hilo)
        hilo.start()

     # Se espera a que terminen los procesos de los hilos:
    for hilo in hilos:
        hilo.join()

    # Se calcula la suma de los valores de la matriz de forma secuencial:
    suma_total = numpy.sum(sum_parciales)

    # Se finaliza el conteo del tiempo de ejecución:
    fin = time.time()

    # Se imprime el resultado de la suma y del tiempo de ejecución:
    print("\nSuma total - Híbrido (SMP - SIMD):", int(suma_total))
    print(f"Tiempo - Híbrido (SMP - SIMD): {fin - inicio:.4f} segundos")

if __name__ == "__main__":
    main()
