import queue

fila = queue.Queue()

for numero in [10, 20, 30, 40, 50]:
    fila.put(numero)

print(f"Tamanho da fila: {fila.qsize()}")

while not fila.empty():
    item = fila.get()
    print(f"Retirado: {item}")

print(f"Tamanho da fila: {fila.qsize()}")
