# Módulo 12 — Threading

## O que foi feito

- `race_condition.py`: contador global incrementado por 5 threads sem lock (resultado correto por acaso — janela de colisão pequena demais)
- `race_condition1.py`: mesma lógica, com `time.sleep(0)` forçando troca de contexto — race condition manifestada (100000 em vez de 500000)
- `race_condition2.py`: correção com `threading.Lock` protegendo a seção crítica
- `race_condition3.py`: demonstração de deadlock com dois locks adquiridos em ordem oposta por duas threads
- `race_condition4.py`: correção do deadlock com ordenação consistente de locks
- `race_condition5.py`: comparação de tempo CPU-bound vs I/O-bound, sequencial vs com threads

## O que foi visto no módulo

- GIL (Global Interpreter Lock): o que é, por que existe, e por que impede paralelismo real de CPU em threads Python
- `threading.Thread`, `.start()`, `.join()`
- Race conditions: por que `contador += 1` não é atômico, e por que nem sempre é fácil reproduzir o bug
- `threading.Lock` e seção crítica
- Deadlock: espera circular entre duas threads disputando dois locks
- Correção de deadlock via ordenação consistente de aquisição de locks
- Diferença prática de desempenho entre tarefas CPU-bound e I/O-bound usando threads
- Free-threading (PEP 703 / PEP 779): build experimental desde o Python 3.13, oficialmente suportada (build `t`) a partir do Python 3.14

## O que foi aprendido

- Threads em Python não aceleram trabalho CPU-bound por causa do GIL — podem até piorar, pelo overhead de troca de contexto e disputa de cache
- Threads aceleram bastante trabalho I/O-bound, porque o GIL é liberado durante esperas
- Um teste passar não prova ausência de race condition — bugs de concorrência dependem de timing e podem não aparecer em toda execução
- Deadlock é evitável de forma simples e sistemática: manter uma ordem consistente de aquisição de locks em todo o código
