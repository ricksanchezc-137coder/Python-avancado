import concurrent.futures
import time

def cpu_bound(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    tarefas = [10_000_000] * 4

    inicio = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        list(executor.map(cpu_bound, tarefas))
    print(f"ThreadPoolExecutor: {time.time() - inicio:.2f}s")

    inicio = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        list(executor.map(cpu_bound, tarefas))
    print(f"ProcessPoolExecutor: {time.time() - inicio:.2f}s")
