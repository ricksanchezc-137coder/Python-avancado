import queue

pilha = queue.LifoQueue()

for item in ["a", "b", "c"]:
    pilha.put(item)

print("LifoQueue:")
while not pilha.empty():
    print(pilha.get())

fila_prioridade = queue.PriorityQueue()
for prioridade, tarefa in [(3, "baixa"), (1, "alta"), (2, "media")]:
    fila_prioridade.put((prioridade, tarefa))

print("PriorityQueue:")
while not fila_prioridade.empty():
    print(fila_prioridade.get())
