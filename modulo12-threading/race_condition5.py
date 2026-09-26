import threading
import time

def tarefa_cpu_bound():
    total = 0
    for i in range(20_000_000):
        total += i * i
    return total

def tarefa_io_bound():
    time.sleep(1)  # simula espera de rede/disco

def rodar_sequencial(funcao, vezes):
    inicio = time.perf_counter()
    for _ in range(vezes):
        funcao()
    return time.perf_counter() - inicio

def rodar_com_threads(funcao, vezes):
    inicio = time.perf_counter()
    threads = [threading.Thread(target=funcao) for _ in range(vezes)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return time.perf_counter() - inicio

print("--- CPU-bound ---")
print(f"Sequencial: {rodar_sequencial(tarefa_cpu_bound, 4):.2f}s")
print(f"Com threads: {rodar_com_threads(tarefa_cpu_bound, 4):.2f}s")

print("--- I/O-bound ---")
print(f"Sequencial: {rodar_sequencial(tarefa_io_bound, 4):.2f}s")
print(f"Com threads: {rodar_com_threads(tarefa_io_bound, 4):.2f}s")
