
# Módulo 1 — Descriptors

## O que foi feito

Exercício standalone em `descriptors_exercicio.py`, com 6 passos progressivos: non-data descriptor e resolução via MRO, shadowing por instância, data descriptor com validação, prioridade do data descriptor sobre `__dict__`, reuso do descriptor com `__set_name__`, e `__delete__`.

## O que foi visto no módulo

- Protocolo `__get__` / `__set__` / `__delete__`
- Diferença entre data descriptor e non-data descriptor, e a prioridade de cada um na resolução de atributos
- Papel de `obj` e `objtype` em `__get__`
- `__set_name__` para descriptors reutilizáveis sem colisão de estado
- Casos de uso reais: `property`, `staticmethod`, `classmethod`, ORMs, bibliotecas de validação

## O que foi aprendido

A prioridade do data descriptor sobre `obj.__dict__` não é um detalhe de implementação — é o mecanismo que garante que a lógica de validação de um `__set__` não pode ser contornada escrevendo direto no `__dict__` da instância. Isso também esclarece por que métodos comuns (non-data descriptors) podem ser sombreados por atributos de instância, enquanto `property` nunca pode.
