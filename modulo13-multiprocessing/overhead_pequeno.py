
import multiprocessing
import time


def tarefa_leve(n):
    """Trabalho bem pequeno: praticamente não gasta CPU."""
    return n * n


if __name__ == "__main__":
    numeros = list(range(1000))  # 1000 tarefas, cada uma trivial

    # --- sequencial ---
    inicio = time.time()
    resultados_seq = [tarefa_leve(n) for n in numeros]
    tempo_seq = time.time() - inicio
    print(f"sequencial: {tempo_seq:.4f}s")

    # --- multiprocessing ---
    inicio = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        resultados_mp = pool.map(tarefa_leve, numeros)
    tempo_mp = time.time() - inicio
    print(f"multiprocessing: {tempo_mp:.4f}s")

    print(f"resultados batem: {resultados_seq == resultados_mp}")
    print(f"multiprocessing foi mais lento? {tempo_mp > tempo_seq}")
