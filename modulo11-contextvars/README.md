# Módulo 11 — contextvars

## O que foi feito

Prática isolada (fora do sistema-bancario), com 6 exercícios progressivos:

1. API básica do `ContextVar` (`set`, `get`, `reset` com `Token`).
2. Isolamento entre corrotinas concorrentes rodando via `asyncio.gather`.
3. Contraste com uma variável global comum, demonstrando o vazamento de estado que `contextvars` evita.
4. Comportamento de `asyncio.create_task`, que copia o contexto do chamador em vez de compartilhá-lo.
5. Manipulação direta com `contextvars.copy_context()` e `Context.run()`, o mecanismo por trás das Tasks.
6. Caso de uso aplicado: `request_id` rastreado em três "requisições" concorrentes, com `log()` lendo o contexto sem receber o ID por parâmetro.

## O que foi visto no módulo

- Por que `threading.local()` não resolve o problema de isolamento em código assíncrono (várias corrotinas na mesma thread).
- Como `ContextVar` isola valores por contexto de execução, não por thread.
- O papel do `Token` retornado por `.set()` no `.reset()`.
- Que `Task` do `asyncio` roda numa cópia do contexto de quem a criou — mudanças feitas dentro dela não vazam para fora.
- O uso prático mais comum: rastreamento de `request_id` (ou usuário, tenant, etc.) em frameworks web assíncronos, sem precisar passar o valor por parâmetro em toda a cadeia de chamadas.

## O que foi aprendido

`contextvars` é o mecanismo que garante que estado "por execução" (como um ID de requisição) não vaze entre corrotinas concorrentes que compartilham a mesma thread — algo que uma variável global comum não consegue garantir. Entender que `asyncio.create_task` copia o contexto (em vez de compartilhá-lo) explica por que esse isolamento acontece automaticamente ao usar Tasks, e por que esse padrão é seguro mesmo sob alta concorrência.
