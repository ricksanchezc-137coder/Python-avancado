# Módulo 19 — Profiling básico

Currículo 15 (Python avançado). Praticado isolado do `sistema-bancario`.

## O que foi feito

- `timeit_basico.py`: comparação de 3 formas de montar `"-".join` (gerador, list comp, map) com `timeit.timeit`.
- `repeat_basico.py`: `timeit.repeat` do trecho com `map`, 5 rodadas.
- `comparacao.py`: as 3 formas medidas com `repeat` + `min` — gerador 0.6355s, list comp 0.5291s, map 0.5194s.
- `perfil_basico.py`: `cProfile.run` em `contar_primos(10000)` — 11237 chamadas em 1.341s, com `eh_primo` respondendo por ~99% do tempo.
- `perfil_otimizado.py`: `eh_primo` com laço até `math.isqrt(n)` — 0.060s sob o profiler.
- `antes_depois.py`: comparação sem profiler — 1.3184s contra 0.0212s (~62x mais rápido), com `assert` garantindo o mesmo resultado.

## O que foi visto no módulo

- `timeit.timeit` (tempo total de `number` execuções) e `timeit.repeat` (lista de rodadas; usar o `min`).
- `cProfile.run` e as colunas da tabela: `ncalls`, `tottime`, `cumtime`, `percall`.
- Diferença entre ordenar por `cumulative` (árvore de chamadas) e por `tottime` (gargalo).
- Overhead do profiler: ele mostra onde está o tempo, mas distorce o valor absoluto.
- Fluxo: perfilar, otimizar só o gargalo, medir o ganho com `timeit`, conferir a correção com `assert`.
- `python -m cProfile` e `pstats` (apenas apresentados).

## O que foi aprendido

- Medir antes de otimizar: quase todo o tempo estava em uma única função.
- Comparar sempre com `repeat` + `min`; uma medição única pode exagerar diferenças pequenas.
- Resultado estranho demais (dois valores idênticos) pede conferência do código: o problema eram dois `print` apontando para `t1`.
- Menos tempo não significa menos chamadas: a versão otimizada fez mais chamadas e ficou bem mais rápida.
- Um `assert` comparando as versões pegou um erro de sintaxe sutil (vírgula antes do `+ 1`) antes de qualquer conclusão de desempenho.
- O ganho medido pelo profiler (~22x) foi menor que o real (~62x) por causa do custo do próprio profiler.
