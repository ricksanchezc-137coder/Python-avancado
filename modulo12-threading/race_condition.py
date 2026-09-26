import threading

contador = 0

def incrementar():
    global contador
    for _ in range(100_000):
        contador += 1
threads = [threading.Thread(target=incrementar) for _ in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"Valor esperado: {5 * 100_000}")
print(f"Valor final: {contador}")
