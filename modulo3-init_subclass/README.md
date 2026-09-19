# Módulo 3 — __init_subclass__ e hooks de criação de classe

## O que foi feito
5 exercícios progressivos: registro automático de subclasses, kwargs
customizados na declaração de classe, validação de contrato com erro na
definição, __set_name__ em descriptor, e síntese combinando os dois hooks.

## O que foi visto no módulo
- __init_subclass__: hook chamado na definição de uma subclasse
- Uso pra registro automático (padrão plugin/registry)
- Recebimento de kwargs extras direto em `class Filha(Base, kw=valor)`
- Validação de contrato disparando erro na definição, não na instanciação
- __set_name__: hook chamado quando um descriptor vira atributo de classe
- Combinação dos dois hooks numa mesma classe base

## O que foi aprendido
__init_subclass__ resolve boa parte dos casos de uso de metaclasse (Módulo 2)
com bem menos complexidade — é a ferramenta certa quando só quero reagir à
criação de subclasses, sem redefinir como classes em geral são construídas.
