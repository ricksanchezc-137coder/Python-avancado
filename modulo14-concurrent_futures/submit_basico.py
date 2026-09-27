import concurrent.futures
import time

def tarefa(n, atraso):
    time.sleep(atraso)
    print(f"tarefa {n} concluida (atraso {atraso}s)")
    return n ** 2

if __name__ == "__main__":
    entradas = [(1, 3), (2, 1), (3, 2), (4, 0.5), (5, 2.5)]
#versao 1 com max_workers=3, versao 2 com max_workers=5
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(tarefa, n, atraso) for n, atraso in entradas]

        for future in concurrent.futures.as_completed(futures):
            resultado = future.result()
            print(f"resultado recebido: {resultado}")

