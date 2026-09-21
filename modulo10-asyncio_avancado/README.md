# Módulo 10 — asyncio avançado

## O que foi feito

- Comparação de tempo de execução entre chamada sequencial, `asyncio.create_task` e `asyncio.gather` sobre três coroutines simulando downloads.
- Testes de propagação de exceção em `gather`, com e sem `return_exceptions=True`, incluindo a observação de um vazamento real de tasks não canceladas.
- Cancelamento manual de uma Task isolada com `task.cancel()`.
- Reescrita do cenário de exceção usando `asyncio.wait(..., return_when=asyncio.FIRST_EXCEPTION)` para cancelar corretamente as tasks pendentes ao detectar falha.
- Implementação de um async context manager (`ConexaoFake`) com `__aenter__`/`__aexit__`, testado em uso normal e com exceção forçada dentro do bloco.
- Implementação de async generators (`stream_numeros`, `stream_transacoes`), consumidos com `async for` e manualmente com `__anext__()`.

## O que foi visto no módulo

- `asyncio.Task`, `asyncio.create_task`, `asyncio.gather` (uso básico e com `return_exceptions`)
- Cancelamento de tasks (`.cancel()`, `CancelledError`, `.cancelled()`)
- `asyncio.wait` com `return_when=asyncio.FIRST_EXCEPTION`
- Async context managers (`__aenter__`, `__aexit__`, `async with`)
- Async generators (`async def` com `yield`, `async for`, `__anext__()`)

## O que foi aprendido

- `create_task` e `gather` rodam coroutines concorrentemente, mas os resultados voltam na ordem de entrada, não na ordem de conclusão.
- `gather` sem `return_exceptions=True` propaga a primeira exceção, mas **não cancela** as tasks irmãs — elas continuam rodando em segundo plano se nada for feito, causando vazamento.
- `asyncio.wait(..., return_when=asyncio.FIRST_EXCEPTION)` é o padrão correto para detectar falha e cancelar o resto do grupo de tasks de forma controlada.
- Um async context manager garante que `__aexit__` rode mesmo com exceção dentro do bloco, igual a um `finally`.
- Async generators entregam valores conforme ficam prontos (com `await` entre cada `yield`), permitindo consumo gradual — inclusive parcial, sem erro — em vez de esperar tudo pronto de uma vez.
