import time

def tarefa_a():
    print("Tarefa A: comecou")
    time.sleep(2)
    print("Tarefa A: terminou")

def tarefa_b():
    print("Tarefa B: comecou")
    time.sleep(1)
    print("Tarefa B: terminou")

def main():
    inicio = time.perf_counter()

    tarefa_a()
    tarefa_b()

    fim = time.perf_counter()
    print(f"Tempo total: {fim - inicio:.2f}s")

if __name__ == "__main__":
    main()
