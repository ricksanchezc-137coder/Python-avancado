# Módulo 13 — Multiprocessing

## O que foi feito

- `basico.py`: criação de processos com `multiprocessing.Process` — um processo único e depois dois em paralelo, com `.start()`/`.join()`
- `pool_basico.py`: `multiprocessing.Pool` distribuindo 8 tarefas entre 3 workers via `pool.map()`
- `comparativo_cpu.py`: comparação de tempo sequencial vs. multiprocessing numa tarefa CPU-bound (soma de quadrados)
- `overhead_pequeno.py`: comparação sequencial vs. multiprocessing numa tarefa leve, evidenciando o overhead

## O que foi visto no módulo

- Diferença fundamental entre `Process` (multiprocessing) e `Thread` (threading): cada `Process` roda em PID próprio, com interpretador e memória separados; threads compartilham tudo isso
- `multiprocessing.Pool` reaproveita um número fixo de processos worker em vez de criar um por tarefa, distribuindo o trabalho dinamicamente
- Comparação real de CPU-bound: multiprocessing (8.06s) teve o resultado oposto de threading no Módulo 12 (61.66s) frente ao mesmo sequencial (~30s) — sem GIL compartilhado entre processos, o paralelismo é real
- Overhead de criar processos e serializar dados pode tornar multiprocessing muito mais lento que sequencial quando a tarefa é leve (0.0003s sequencial vs. 0.5138s multiprocessing em 1000 tarefas triviais)

## O que foi aprendido

- Multiprocessing é a ferramenta certa pra CPU-bound pesado, não uma alternativa universal a threading
- `if __name__ == "__main__":` não é estilo, é requisito técnico em qualquer script que use multiprocessing
- Antes de paralelizar, vale considerar o tamanho da tarefa: threading serve pra I/O-bound, multiprocessing pra CPU-bound pesado, e nenhum dos dois compensa quando a tarefa individual é leve demais
