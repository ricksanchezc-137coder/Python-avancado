# Módulo 14 — concurrent.futures

## O que foi feito

- `pool_basico.py`: `ThreadPoolExecutor` + `.map()`, comparando com o `pool_basico.py` do Módulo 13
- `submit_basico.py`: `ThreadPoolExecutor` + `.submit()` + `as_completed()`, testado com `max_workers=3` e `max_workers=5`
- `pool_processos.py`: `ProcessPoolExecutor` + `.map()` + `os.getpid()`, testado com e sem `time.sleep()` na tarefa
- `try_except_no_future.py`: tratamento de exceção dentro de `Future`, com `dict {future: valor}` + `as_completed()`
- `comparacao_cpu_bound.py`: `ThreadPoolExecutor` vs `ProcessPoolExecutor` numa tarefa CPU-bound

## O que foi visto no módulo

- `concurrent.futures` como camada de abstração sobre `threading` e `multiprocessing` (mesma interface, `ThreadPoolExecutor`/`ProcessPoolExecutor`)
- O objeto `Future`: `.result()`, `.done()`, `as_completed()`
- `.map()` preserva ordem original; `as_completed()` segue ordem real de conclusão
- Exceções ficam guardadas no `Future` e só são relançadas em `.result()`
- `ProcessPoolExecutor` inicia processos sob demanda (diferente do `Pool`, que sobe tudo de uma vez)

## O que foi aprendido

- Trocar `ThreadPoolExecutor` por `ProcessPoolExecutor` (e vice-versa) é praticamente só trocar o nome da classe — a interface é a mesma, o que muda é o mecanismo por baixo (thread vs processo)
- A ordem de conclusão no `as_completed()` depende de quando a tarefa *começou de fato*, não só do tempo declarado de execução — com poucos workers e fila de espera, isso pode gerar uma ordem bem diferente da intuitiva
- Nem todo `max_workers` configurado garante que todos os workers serão de fato usados — com tarefas muito rápidas, o `ProcessPoolExecutor` pode processar tudo com um único processo, por causa da inicialização sob demanda
- O comparativo CPU-bound confirmou que o GIL continua sendo a mesma limitação estrutural, não importa a camada de abstração usada por cima
