# Módulo 7 — MRO e super() em herança múltipla

## O que foi feito

- Cenário de diamante (`A`, `B(A)`, `C(A)`, `D(B, C)`) e inspeção do `D.__mro__`
- Comparação entre resolução de método sem `super()` (para na primeira classe que define o método) e com `super()` cooperativo (percorre todo o MRO)
- `__init__` cooperativo com `**kwargs` em todas as classes da cadeia, inicializando `D`, `B`, `C` e `A` na ordem do MRO
- Quebra proposital da cadeia (removendo `super().__init__()` de `C`) para observar o efeito de um elo faltando
- Hierarquia com ordens contraditórias entre duas classes-base (`X, Y` vs `Y, X`), provocando `TypeError: Cannot create a consistent method resolution order`

## O que foi visto no módulo

- MRO (Method Resolution Order) e o algoritmo C3 linearization por trás dele
- `super()` como "próximo passo no MRO da instância", não "chama a classe-pai direta"
- Diferença entre resolução de nome (para no primeiro match) e propagação cooperativa (percorre a cadeia inteira)
- Efeito de uma classe intermediária não repassar `super()` — falha silenciosa, sem erro
- Momento em que o Python calcula o MRO (na definição da classe) e o erro que resulta de um MRO impossível

## O que foi aprendido

- `super()` em herança múltipla depende do MRO da classe concreta sendo instanciada, não da relação estática entre a classe atual e seus pais declarados
- Um `__init__` cooperativo só funciona se **todas** as classes da cadeia chamarem `super().__init__(**kwargs)`, inclusive a última antes de `object`
- Esquecer um `super()` no meio da cadeia não gera erro — só deixa de inicializar as classes seguintes, o que é mais perigoso que um erro explícito
- Um MRO inconsistente é detectado e falha na **definição** da classe, não na instanciação, o que evita que o problema passe despercebido até alguém tentar criar um objeto
