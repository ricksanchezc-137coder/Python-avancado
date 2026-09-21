# Módulo 9 — Async/await — fundamentos

## O que foi feito

Prática isolada do sistema-bancario (mesmo padrão dos módulos 4 a 8), comparando execução síncrona e assíncrona com duas coroutines simuladas (`tarefa_a` e `tarefa_b`), em seis variações sucessivas:

1. Versão síncrona baseline (`time.sleep`)
2. Versão assíncrona com `asyncio.gather()`
3. Coroutine chamada sem `await` (nunca aguardada)
4. `await` sequencial sem `gather`
5. Código bloqueante (`time.sleep`) dentro de uma `async def`
6. Captura de valores de retorno via `gather`

## O que foi visto no módulo

- Coroutines (`async def`) e por que chamá-las não executa nada sem `await`
- O event loop como mecanismo de concorrência cooperativa numa única thread
- `asyncio.run()` como ponto de entrada
- Diferença entre `asyncio.sleep()` (cooperativo) e `time.sleep()` (bloqueante)
- `asyncio.gather()` para rodar coroutines concorrentemente e capturar resultados
- Por que `await` sozinho, sem `gather`/`create_task`, não gera concorrência

## O que foi aprendido

- Concorrência com async/await é cooperativa: cada coroutine só cede o controle quando bate num `await` de verdade (como `asyncio.sleep`)
- Código bloqueante dentro de uma coroutine trava o event loop inteiro, afetando até tarefas que não têm relação com ele
- `gather()` preserva a ordem de entrada nos resultados, independente da ordem real de término das tarefas
- Os testes práticos (com tempos medidos via `time.perf_counter()`) tornaram visível na prática cada um desses comportamentos, em vez de só na teoria
