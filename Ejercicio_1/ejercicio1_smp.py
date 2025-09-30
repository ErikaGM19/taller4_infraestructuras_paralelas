import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Generador de índices (i0, i1, j0, j1) para partir una matriz n x n en bloques
def bloques_indices(n, bloque):
    for i in range(0, n, bloque):
        for j in range(0, n, bloque):
            yield i, min(i + bloque, n), j, min(j + bloque, n)

# Función que calcula la suma de un bloque
def suma_bloque(matriz, i0, i1, j0, j1):
    return matriz[i0:i1, j0:j1].sum(dtype=np.int64)

def main():
    N = 1000
    BLOQUE = 100
    np.random.seed(0)   # semilla para reproducibilidad

    # 1) Crear la matriz de 1000x1000 con números aleatorios
    matriz = np.random.randint(0, 100, size=(N, N), dtype=np.int64)

    # 2) Dividir la matriz en bloques de 100x100
    bloques = list(bloques_indices(N, BLOQUE))
    print(f"Matriz {N}x{N}, bloques de {BLOQUE}x{BLOQUE}\n")

    inicio = time.time()

    # 3) Procesar cada bloque con hilos
    suma_total = 0
    with ThreadPoolExecutor() as executor:
        # Enviar cada bloque como tarea
        futures = [executor.submit(suma_bloque, matriz, i0, i1, j0, j1) 
                   for (i0, i1, j0, j1) in bloques]

        # Recoger resultados
        for idx, future in enumerate(as_completed(futures), start=1):
            suma_bloque_result = future.result()
            print(f"suma Bloque {idx}: = {suma_bloque_result}")
            suma_total += suma_bloque_result

    fin = time.time()

    print("\nSuma total con hilos:", int(suma_total))
    print(f"Tiempo paralelo: {fin - inicio:.4f} segundos")

if __name__ == "__main__":
    main()
