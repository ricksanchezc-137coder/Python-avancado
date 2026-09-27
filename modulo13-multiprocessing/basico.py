import multiprocessing
import os
import time

def tarefa(nome):
    print(f"[{nome}] rodando no PID {os.getpid()}")
    time.sleep(1)
    print(f"[{nome}] terminou")

if __name__ == "__main__":
    print(f"PID do processo principal: {os.getpid()}")

    p1 = multiprocessing.Process(target=tarefa, args=("processo-1",))
    p1.start()
    p1.join()

    print("------")

    p2 = multiprocessing.Process(target=tarefa, args=("processo-2",))
    p3 = multiprocessing.Process(target=tarefa, args=("processo-3",))

    p2.start()
    p3.start()

    p2.join()
    p3.join()

    print("todos os processos  terminaram")
