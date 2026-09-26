import threading
import time 

lock_conta_a = threading.Lock()
lock_conta_b = threading.Lock()

def transferir_a_para_b():
    with lock_conta_a:
        print("Thread 1: segurou lock A")
        time.sleep(1)
        print("Thread 1: esperando lock B...")
        with lock_conta_b:
            print("Thread 1: conseguiu lock B")

def transferir_b_para_a():
    with lock_conta_b:
        print("Thread 2: segurou lock B")
        time.sleep(1)
        print("Thread 2: esperando lock A")
        with lock_conta_a:
            print("Thread 2: conseguiu lock A")

t1 = threading.Thread(target=transferir_a_para_b)
t2 = threading.Thread(target=transferir_b_para_a)

t1.start()
t2.start()

t1.join()
t2.join()

print("Fim")
