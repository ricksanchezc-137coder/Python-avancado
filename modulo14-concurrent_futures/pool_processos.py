import concurrent.futures
import os
import time

def tarefa(n):
    time.sleep(0.1)
    print(f"PID {os.getpid()} processando {n}")
    return n ** 2

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8]

    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        resultados = list(executor.map(tarefa, numeros))

    print(resultados)
