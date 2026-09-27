# Módulo 15 — queue

## O que foi feito

- `basico.py`: uso básico de `queue.Queue` (`.put()`, `.get()`, `.qsize()`, `.empty()`), confirmando comportamento FIFO
- `produtor_consumidor.py`: padrão produtor-consumidor com thread produtora, thread consumidora daemon, e sincronização via `task_done()`/`.join()`
- `maxsize_multiplos.py`: fila com `maxsize` limitado e múltiplos consumidores, testando bloqueio de `.put()` e distribuição de trabalho
- `lifo_priority.py`: comparação entre `queue.LifoQueue` (pilha) e `queue.PriorityQueue` (ordenação por prioridade)
- `multiprocessing_queue.py`: comunicação entre processos com `multiprocessing.Queue`, usando sentinela `None` para sinalizar fim de produção

## O que foi visto no módulo

- `queue.Queue`, `queue.LifoQueue` e `queue.PriorityQueue`, todas thread-safe por padrão
- Bloqueio automático de `.put()` (fila cheia) e `.get()` (fila vazia)
- Padrão produtor-consumidor com `task_done()`/`.join()` para sincronização
- Distribuição de trabalho entre múltiplos consumidores concorrentes
- Diferença entre `queue.Queue` (threads, mesma memória) e `multiprocessing.Queue` (processos, dados serializados)

## O que foi aprendido

- `queue.Queue` resolve o padrão produtor-consumidor sem precisar de lock manual — o lock já vem embutido nos métodos
- `maxsize` transforma `.put()` num ponto de bloqueio real, não só uma trava lógica — confirmado na prática vendo o produtor esperar por espaço
- A ordem de `print()` entre threads diferentes não é garantia de ordem real das operações internas — só a fila em si tem consistência garantida
- `multiprocessing.Queue` não tem `task_done()`/`.join()` porque lida com serialização entre processos, exigindo um padrão manual (sentinela) para sinalizar fim de produção
