import numpy as np
import time

# Genera los límites de cada bloque en la matriz (i0, i1, j0, j1)
def dividir_bloques(n, bloque):
    for i in range(0, n, bloque):
        for j in range(0, n, bloque):
            yield i, min(i + bloque, n), j, min(j + bloque, n)

def main():
    N = 1000            
    BLOQUE = 100        
    np.random.seed(0)   # semilla para generar los mismo numeros aleatorios

    # 1) Crea la matriz de 1000x1000 con números aleatorios
    matriz = np.random.randint(0, 100, size=(N, N), dtype=np.int64)

    # 2) Divide la matriz en los bloques de 100x100
    bloques = list(dividir_bloques(N, BLOQUE))
    print(f"Matriz {N}x{N}, bloques de {BLOQUE}x{BLOQUE}\n")

    
    inicio = time.time()

    # 3) Suma cada bloque de manera secuencial
    suma_total = 0
    for idx, (i0, i1, j0, j1) in enumerate(bloques, start=1):
        suma_bloque = matriz[i0:i1, j0:j1].sum(dtype=np.int64)
        print(f"suma Bloque {idx}: = {suma_bloque}")

        suma_total += suma_bloque 
    fin = time.time()

    print("\nSuma total secuencial:", int(suma_total))
    print(f"Tiempo secuencial: {fin - inicio:.4f} segundos")

if __name__ == "__main__":
    main()
