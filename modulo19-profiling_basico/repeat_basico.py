import timeit

resultados = timeit.repeat(
    '"-".join(map(str, range(100)))',
    number=10000,
    repeat=5,
)
for i, t in enumerate(resultados, start=1):
    print(f"rodada {i}: {t:.4f}s")

print(f"menor: {min(resultados):.4f}s")
