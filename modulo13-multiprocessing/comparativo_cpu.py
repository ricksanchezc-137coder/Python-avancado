import multiprocessing
import time

def cpu_bound(n):
    """Trabalho pesado de CPU: soma de quadrados ate n."""
    total = 0
    for i in range(n):
        total += i * i
    return total

if __name__ == "__main__":
    N = 20_000_000
    QUANTIDADE = 4
#versao sequencial
    inicio = time.time()
    resultados_seq = [cpu_bound(N) for _ in range(QUANTIDADE)]
    tempo_seq = time.time() - inicio
    print(f"sequencial: {tempo_seq:.2f}s")



#versao multiprocessing.Pool

    inicio = time.time()
    with multiprocessing.Pool(processes=QUANTIDADE) as pool:
        resultados_mp = pool.map(cpu_bound, [N] * QUANTIDADE)
    tempo_mp = time.time() - inicio
    print(f"multiprocessing: {tempo_mp:.2f}s")

    print(f"resultados batem: {resultados_seq == resultados_mp}")
    print(f"speedup: {tempo_seq / tempo_mp:.2f}x")
