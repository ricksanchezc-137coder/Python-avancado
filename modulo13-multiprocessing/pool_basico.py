import multiprocessing
import os
import time

def quadrado(n):
    pid = os.getpid()
    print(f"[worker PID {pid}] calculando {n}^2")
    time.sleep(0.5)
    return n * n

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8]

    print(f"PID do processo principal: {os.getpid()}")

    with multiprocessing.Pool(processes=3) as pool:
        resultados = pool.map(quadrado, numeros)

    print(f"resultados: {resultados}")
