# Módulo 20 — Encerramento (Currículo 15: Python avançado)

Resumo de aula. Data: 01/10/2026.

## O que foi feito

- **Revisão** dos 19 módulos do currículo e **análise do `sistema-bancario`** contra cada um deles, com o critério de só aplicar o que desse ganho real.
- **Profiling** (`bench_saldo.py`, mantido fora do commit): `calcular_saldo`, `depositar` e o extrato medidos em bancos temporários de 10 mil, 51 mil e 205 mil linhas, comparando "como está", "com índices" e "soma em SQL". O custo cresce linearmente com o histórico, o ganho dos índices foi pequeno (~7% no `depositar`) e a soma em SQL foi 5–7x mais rápida. Nada disso foi aplicado.
- **`match/case` aplicado** em `menu()`, `submenu_extratos()` (com `match` aninhado) e `calcular_saldo()` (com guards), no commit `edf9541`. Verificado com uma comparação de saída antes/depois em cópia do projeto.
- **Suíte de testes consertada:** 9 arquivos de teste atualizados para as exceções específicas do Módulo 14 (`excecoes.py`), saindo de 27 falhas para **171 passed e 1 falha proposital** (o XPASS strict do Currículo 9).
- **Bug real corrigido** no `menu()`: `float("abc")` derrubava o programa porque o `except` só capturava `ErroContaBancaria`. Agora é `except (ErroContaBancaria, ValueError)`.
- **`DeprecationWarning`** do adaptador padrão de `date` (Python 3.12+) corrigido com `hoje.isoformat()` em `servico.py`.

## O que foi visto no módulo

- **Modelo de objetos:** descriptors, metaclasses, `__init_subclass__`, `__slots__`, ABC, `Protocol`, MRO/`super()`, `singledispatch`.
- **Concorrência:** async/await, asyncio avançado, `contextvars`, threading (GIL, locks, deadlock), multiprocessing, `concurrent.futures`, `queue`.
- **Tipos, memória e medição:** typing avançado (`TypeVar`, `Generic`, `@overload`), `weakref`, pattern matching e profiling (`timeit`, `cProfile`).
- **Aplicação real:** como decidir o que entra num projeto existente (inventário, hipótese, medição, decisão), a pegadinha do nome solto no `case` (captura em vez de comparação) e como isolar a causa de falhas de teste com `git stash` + `diff`.

## O que foi aprendido

- **Medir antes de otimizar.** O profiling serviu para dizer *não* a duas otimizações; concluir "não vale aqui" com dado é um resultado do módulo.
- **Nem toda técnica avançada cabe no projeto.** Das 19, só `match/case` e profiling se aplicaram; concorrência, `weakref`, `singledispatch` e afins não tinham lugar num CLI síncrono com SQLite.
- **`case NOME:` não compara, captura.** Para comparar com constante é preciso nome pontuado (`dados.TIPO_X`).
- **Não substituir arquivos inteiros a partir de uma leitura incerta.** Uma cópia antiga em cache e a falta de indentação levaram a um arquivo reconstruído errado; a regra passou a ser trocar só os trechos alterados e conferir o `git diff`.
- **Rodar a suíte completa antes de commitar** teria pego as 25 falhas e o bug do `menu()` deixados pelo Módulo 14.
- **Testes ajudam a achar defeitos de produção:** o teste de valor inválido apontou o `except` incompleto do `menu()`.
- **Comparar listas de falhas** (`pytest -rfE | grep | sort` + `diff`) é uma forma segura de provar que uma mudança não quebrou nada.

**Status: Módulo 20 concluído — Currículo 15 (Python avançado) 20/20.**
