# Módulo 18 — Pattern matching (match/case)

Currículo 15 — Python avançado

## O que foi feito

Seis exercícios, cada um em um arquivo `.py` isolado nesta pasta:

| Arquivo | Tema |
|---|---|
| `basico.py` | Literais, curinga `_` e OR (`\|`) |
| `sequencial.py` | Padrões de sequência e `*resto` |
| `mapeamento.py` | Padrões de dicionário e `**resto` |
| `classes.py` | Padrões de classe, `@dataclass` e `__match_args__` |
| `guards.py` | Guards (`if`) e `as` |
| `armadilha.py` | Captura de nome solto vs. valor com ponto |

Todos rodaram com a saída esperada.

## O que foi visto no módulo

- O `match` (PEP 634, Python 3.10+) compara um padrão com um valor e pode ligar nomes.
- Os `case` são testados de cima pra baixo; o primeiro que casa executa.
- Padrões: literal, `_`, OR (`|`), sequência (`[a, *resto]`), mapeamento (`{"k": v, **resto}`), classe (`Ponto(x, y)`), tipo (`int()`), guard (`if`) e `as`.
- `str`, `bytes` e `bytearray` não casam com padrões de sequência.
- `@dataclass` gera `__match_args__`; em classe comum, define-se na mão.

## O que foi aprendido

- A ordem dos `case` importa: específicos primeiro, `_` por último.
- Chaves extras não impedem o casamento de um padrão de dicionário.
- `bool` é subclasse de `int`, então `case bool()` precisa vir antes de `case int()`.
- Um nome simples num `case` captura e sobrescreve a variável; pra comparar com constante, usar nome com ponto (`Cor.AZUL`).
- Sem nenhum `case` casando, o `match` não dá erro; a função devolve `None`.
