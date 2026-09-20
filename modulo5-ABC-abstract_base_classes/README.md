# Módulo 5 — ABC (Abstract Base Classes)

## O que foi feito

Praticado isolado (fora do sistema-bancario), com uma hierarquia de formas geométricas:

- `FormaGeometrica(ABC)` com `area` como método abstrato — testada instanciação direta bloqueada.
- `Circulo(FormaGeometrica)` sem implementar `area` — testado bloqueio de instanciação na subclasse.
- `Circulo` e `Quadrado` implementando `area` — testado funcionamento normal e `isinstance`.
- `nome` como property abstrata + `descricao()` como método concreto (Template Method) — testado nas duas subclasses.
- `Triangulo` sem herança, registrado via `FormaGeometrica.register(Triangulo)` — testado `isinstance`/`issubclass` sem contrato real cumprido.

## O que foi visto no módulo

- `abc.ABC` e `@abstractmethod`.
- Bloqueio de instanciação de classe abstrata e de subclasse incompleta (`TypeError`).
- Métodos concretos convivendo com métodos abstratos na mesma classe.
- `@property` abstrata (ordem dos decorators).
- `X.register(Y)` como mecanismo de subclasse virtual, sem herança.

## O que foi aprendido

- O contrato do ABC é checado na **criação do objeto**, não na chamada do método — erro aparece cedo.
- `ABCMeta` é a metaclasse por trás do `ABC`, conectando com o módulo de Metaclasses.
- Template Method: método concreto na base, escrito uma vez, funcionando em qualquer subclasse que cumpra o contrato.
- `register()` é um ponto fraco do ABC: engana `isinstance`/`issubclass` sem exigir implementação real — motivo pelo qual o próximo módulo (`Protocol`) existe.

