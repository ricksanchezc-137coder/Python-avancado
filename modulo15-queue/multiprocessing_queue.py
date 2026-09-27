import multiprocessing
import time

def trabalhador(fila):
    for i in range(3):
        fila.put(f"processo-item-{i}")
        time.sleep(0.3)
    fila.put(None)

if __name__ == "__main__":
    fila = multiprocessing.Queue()
    processo = multiprocessing.Process(target=trabalhador, args=(fila,))
    processo.start()

    while True:
        item = fila.get()
        if item is None:
            break
        print(f"Recebido no processo principal: {item}")
    processo.join()
    print("Fim")
