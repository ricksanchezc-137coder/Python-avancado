import concurrent.futures

def tarefa(n):
    if n == 3:
        raise ValueError(f"n={n} nao e permitido")
    return n ** 2

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5]

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(tarefa, n) : n for n in numeros}

        for future in concurrent.futures.as_completed(futures):
            n = futures[future]
            try:
                resultado = future.result()
                print(f"n={n} -> resultado {resultado}")
            except ValueError as e:
                print(f"n={n} -> erro capturado: {e}")
