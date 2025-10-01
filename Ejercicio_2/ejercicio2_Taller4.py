import numpy as np
import time
import matplotlib.pyplot as plt

# ----------------------------
# 1) Implementación naive (bucle triple en Python puro)
# ----------------------------
def matmul_naive(A, B):
    """Multiplicación de matrices usando bucles triples (Python puro).
       A y B son listas de listas (floats).
    """
    n = len(A)
    # Transponemos B para mejorar el acceso a memoria
    Bt = [list(col) for col in zip(*B)]
    C = [[0.0] * n for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        Ci = C[i]
        for j in range(n):
            s = 0.0
            Bj = Bt[j]
            for k in range(n):
                s += Ai[k] * Bj[k]
            Ci[j] = s
    return C

# ----------------------------
# 2) Función para medir tiempos
# ----------------------------
def medir_numpy(n):
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    t0 = time.perf_counter()
    C = A @ B    # uso de BLAS/LAPACK con SIMD
    t1 = time.perf_counter()
    return C, t1 - t0

def medir_naive(n):
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    A_list = A.tolist()
    B_list = B.tolist()
    t0 = time.perf_counter()
    C = matmul_naive(A_list, B_list)
    t1 = time.perf_counter()
    return np.array(C), t1 - t0

# ----------------------------
# 3) Experimento
# ----------------------------
if __name__ == "__main__":
    # Tamaños que mediremos
    sizes_numpy = [50, 100, 150, 200, 1000]  # NumPy puede con 1000
    sizes_naive = [50, 100, 150]             # Naive solo en tamaños pequeños

    resultados = []

    for n in sizes_numpy:
        print(f"\nProbando NumPy con n={n}...")
        Cnp, tnp = medir_numpy(n)
        resultados.append(("numpy", n, tnp))

        if n in sizes_naive:
            print(f"   Probando naive con n={n}...")
            Cnv, tnv = medir_naive(n)
            # verificar que los resultados coincidan
            ok = np.allclose(Cnp, Cnv, atol=1e-8)
            resultados.append(("naive", n, tnv))
            print(f"   -> Coinciden resultados: {ok}")

    # ----------------------------
    # 4) Mostrar tabla de tiempos
    # ----------------------------
    print("\nResultados:")
    print(f"{'Método':<10} {'n':<6} {'Tiempo (s)':<12}")
    for metodo, n, tiempo in resultados:
        print(f"{metodo:<10} {n:<6} {tiempo:<12.6f}")

    # ----------------------------
    # 5) Graficar resultados
    # ----------------------------
    plt.figure(figsize=(8, 5))
    for metodo in set(r[0] for r in resultados):
        xs = [n for m, n, t in resultados if m == metodo]
        ys = [t for m, n, t in resultados if m == metodo]
        plt.plot(xs, ys, marker="o", label=metodo)

    plt.xlabel("n (matriz n x n)")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparación tiempos: NumPy vs. bucle tradicional")
    plt.legend()
    plt.grid(True)
    plt.show()
