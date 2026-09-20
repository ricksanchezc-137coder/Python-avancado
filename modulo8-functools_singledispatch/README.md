# Módulo 8 — functools.singledispatch

## O que foi feito

Prática isolada do sistema-bancario, em dois scripts (`exercicio1.py` e `exercicio2.py`):

- Função genérica `descrever(obj)` com `@singledispatch`, com implementação padrão e implementações registradas para `int`, `str`, `list`, `dict`, `set`, `frozenset`, `bytes` e `bytearray`.
- Teste de dispatch com `bool`, confirmando que ele herda a implementação de `int` por ser subclasse.
- Inspeção do registro com `.registry.keys()` e `.dispatch()`.
- Classe `Formatador` com `singledispatchmethod`, formatando valores de forma diferente por tipo (`int`, `float`, `str`).

## O que foi visto no módulo

- `@singledispatch` para criar funções genéricas por tipo, sem `if isinstance` encadeado
- Registro de implementações via `@func.register` (com inferência por type hint ou tipo explícito)
- Registro de múltiplos tipos para a mesma implementação (stack de decorators ou union `|`, Python 3.11+)
- Comportamento do dispatch respeitando a hierarquia de tipos (MRO), com o caso `bool`/`int`
- Introspecção do dispatch: `.registry` e `.dispatch()`
- `functools.singledispatchmethod` para uso dentro de métodos de instância

## O que foi aprendido

O `singledispatch` resolve de forma elegante um problema comum: uma função que precisa se comportar diferente dependendo do tipo do argumento. A hierarquia de tipos do Python (MRO) é respeitada automaticamente no dispatch, o que exige atenção em casos como `bool`/`int`, onde o comportamento pode não ser o esperado se não houver um registro específico. `singledispatchmethod` é a forma mais próxima de uso real, aplicável a métodos de classes de serviço que processam tipos diferentes de entrada.
