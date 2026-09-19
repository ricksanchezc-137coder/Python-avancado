# Módulo 4 — `__slots__`

## O que foi feito

Testes práticos em ambiente separado (`modulo4-slots/`), comparando classes com e sem `__slots__`:
- Tentativa de setar atributo não declarado (erro esperado)
- Medição de memória real com `tracemalloc` para 100.000 instâncias (31,3% de economia com slots)
- Herança sem `__slots__` própria vs. com `__slots__ = ()`
- Herança múltipla com layouts de slots conflitantes
- Conflito entre slot e atributo de classe de mesmo nome
- Suporte a `weakref` com `'__weakref__'` declarado

## O que foi visto no módulo

- Como `__slots__` substitui o `__dict__` de instância por um layout fixo baseado em descriptors
- As principais limitações: restrição de atributos, dependência de `__slots__` em toda a cadeia de herança, incompatibilidade entre bases com layouts diferentes, conflito com atributo de classe, perda de `weakref` por padrão

## O que foi aprendido

- O ganho de memória de `__slots__` é real, mas menor do que a intuição sugere, por causa do key-sharing dict (PEP 412) que já otimiza o `__dict__` padrão quando as instâncias compartilham os mesmos nomes de atributo
- `__slots__` compensa mais em cenários de muitas instâncias com atributos fixos e conhecidos de antemão
- Desde o Python 3.10, `@dataclass(slots=True)` gera isso automaticamente
