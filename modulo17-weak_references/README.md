# Módulo 17 — Weak References

## O que foi feito

Prática isolada do sistema-bancario, com 5 scripts em `modulo17-weak_references/`:

- `basico.py` — `weakref.ref()`: criação de referência fraca, acesso via chamada, comportamento após `del` + `gc.collect()`
- `proxy.py` — `weakref.proxy()`: acesso transparente ao objeto, `ReferenceError` após coleta
- `weak_value_dict.py` — `WeakValueDictionary`: remoção automática de entrada quando o valor perde a última referência forte
- `callback.py` — `weakref.ref(obj, callback)`: função disparada no exato momento da coleta do objeto
- `weak_set.py` — `WeakSet`: remoção automática de item quando perde a última referência forte

## O que foi visto no módulo

- Diferença entre referência forte e referência fraca, e como isso afeta a decisão do garbage collector de destruir ou não um objeto
- `weakref.ref()` vs `weakref.proxy()`: acesso por chamada e retorno `None` vs. acesso direto e `ReferenceError`
- `WeakValueDictionary` e `WeakSet` como estruturas que se autolimpam, sem remoção manual de entradas
- Callback executado no momento exato da coleta de um objeto referenciado fracamente
- Casos de uso reais: cache que se limpa sozinho, padrão Observer sem prender observadores na memória, quebra de ciclos de referência (ex: filho com referência de volta ao pai)

## O que foi aprendido

Toda a bateria de 5 scripts confirmou exatamente o comportamento esperado pela teoria, sem nenhuma surpresa nos resultados: a referência fraca nunca impediu a coleta do objeto, e cada estrutura (`ref`, `proxy`, `WeakValueDictionary`, `WeakSet`, callback) reagiu do jeito documentado assim que a última referência forte foi removida. Fica claro o valor prático de weak references pra evitar memory leaks em estruturas com referências cíclicas ou "de volta" — sem precisar de limpeza manual.
