# SE IMPORTAN LAS LIBRERÍAS NECESARIAS:
import random
import time

# SE FIJA UNA SEMILLA PARA LA GENERACIÓN DE VALORES ALEATORIOS:
random.seed(42) 

# SE CREA UNA FUNCIÓN PARA GENERAR LA MATRIZ INICIAL:
def generar_matriz(filas, columnas):
    return [[random.randint(0, 9) for _ in range(columnas)] for _ in range(filas)]

# SE CREA UNA FUNCIÓN PARA REALIZAR LA SUMA SENCUENCIAL DE LOS VALORES DE LA MATRIZ:
def suma_secuencial(matriz):
    suma = 0
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[0])):
            suma =  suma + matriz[i][j]
    return suma

# SE DEFINE LA FUNCIÓN PRINCIPAL DONDE SE EJECUTARÁN LAS FUNCIONES:
def main():

    # Se definen los parámetros para crear la matríz:
    filas = 10000
    columnas = 10000            

    # Se crea la matriz con las dimensiones definidas anteriormente:
    matriz = generar_matriz(filas, columnas)

    # Se inicia el conteo del tiempo de ejecución:
    print(f" Se inicia la suma de los elementos de una matriz {filas}x{columnas} \n")
    inicio = time.time()

    # Se calcula la suma de los valores de la matriz de forma secuencial:
    suma_total = suma_secuencial(matriz)

    # Se finaliza el conteo del tiempo de ejecución:
    fin = time.time()

    # Se imprime el resultado de la suma y del tiempo de ejecución:
    print("\nSuma total - Secuencial:", int(suma_total))
    print(f"Tiempo - Secuencial: {fin - inicio:.4f} segundos")

if __name__ == "__main__":
    main()
