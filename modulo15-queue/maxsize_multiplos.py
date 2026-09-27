import queue
import threading
import time

fila = queue.Queue(maxsize=2)

def produtor():
    for i in range(6):
        item = f"item-{i}"
        print(f"Tentando produzir {item}")
        fila.put(item)
        print(f"Produzido {item}")

def consumidor(nome):
    while True:
        item = fila.get()
        print(f"{nome} consumindo {item}")
        time.sleep(1)
        fila.task_done()

t_produtor = threading.Thread(target=produtor)
t_c1 = threading.Thread(target=consumidor, args=("Consumidor-A",), daemon=True)
t_c2 = threading.Thread(target=consumidor, args=("Consumidor-B",), daemon=True)

t_c1.start()
t_c2.start()
t_produtor.start()

t_produtor.join()
fila.join()
print("Fim")

