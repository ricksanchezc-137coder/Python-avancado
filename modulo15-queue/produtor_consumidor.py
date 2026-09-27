import queue
import threading
import time

fila = queue.Queue()

def produtor():
    for i in range(5):
        item = f"item-{i}"
        print(f"Produzindo {item}")
        fila.put(item)
        time.sleep(0.5)

def consumidor():
    while True:
        item = fila.get()
        print(f"Consumindo {item}")
        fila.task_done()

t_produtor = threading.Thread(target=produtor)
t_consumidor = threading.Thread(target=consumidor, daemon=True)

t_produtor.start()
t_consumidor.start()

t_produtor.join()
fila.join()
print("Fim")
