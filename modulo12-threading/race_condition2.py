import threading
import time

contador = 0
lock = threading.Lock()

def incrementar():
    global contador
    for _ in range(100_000):
        with lock:
            valor_atual = contador
            time.sleep(0)
            contador = valor_atual + 1

threads = [threading.Thread(target=incrementar) for _ in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"Valor esperado: {5 * 100_000}")
print(f"Valor final: {contador}")
