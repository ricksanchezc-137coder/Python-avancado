# Módulo 2 — Metaclasses

## O que foi feito

5 exercícios práticos implementados e testados em `metaclasses.py` / `metaclasses_com_call.py`:

1. `MetaLog` — observação da ordem de execução `__new__`/`__init__` da metaclasse e inspeção do `namespace` da classe.
2. `MetaValidada` — validação estrutural: rejeita a criação de subclasses que não implementam `executar`.
3. `MetaRegistro` — registro automático de subclasses num dict de classe, com instanciação dinâmica por nome.
4. `MetaOrdem` — observação de `__prepare__` rodando antes de `__new__`, preservando a ordem de declaração dos atributos.
5. `MetaSingleton` — Singleton implementado via `__call__` da metaclasse.

## O que foi visto no módulo

- `type` como metaclasse padrão de toda classe em Python, e como construtor dinâmico (`type(nome, bases, namespace)`)
- Pipeline completo de criação de classe: `__prepare__` → `__new__` → `__init__`
- `__call__` da metaclasse controlando a instanciação
- Três casos de uso reais: validação estrutural, registro automático (plugin pattern), Singleton
- Atributos novos de classe no Python 3.13 (`__firstlineno__`, `__static_attributes__`)

## O que foi aprendido

- Metaclasse age na criação da **classe**, não na criação de instâncias — exceto quando se sobrescreve `__call__`, que é o ponto de entrada pra controlar a instanciação também.
- Validação estrutural via metaclasse barra a classe já na definição, antes de qualquer uso — erro aparece cedo.
- Registro automático elimina a necessidade de manter listas/dicts de classes atualizadas manualmente.
- Singleton via metaclasse é didático, mas carrega risco de estado compartilhado indesejado (especialmente em testes) — anotado como ressalva, não como recomendação de uso.
