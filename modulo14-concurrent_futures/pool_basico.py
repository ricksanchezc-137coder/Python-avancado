import concurrent.futures
import threading

def tarefa(n):
    print(f"{threading.current_thread().name} processando {n}")
    return n ** 2

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8]

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        resultados = list(executor.map(tarefa, numeros))

    print(resultados)
