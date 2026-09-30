import timeit

trechos = {
    "gerador": '"-".join(str(n) for n in range(100))',
    "list_comp": '"-".join([str(n) for n in range(100)])',
    "map": '"-".join(map(str, range(100)))',
}

for nome, codigo in trechos.items():
    tempos = timeit.repeat(codigo, number=10000, repeat=5)
    print(f"{nome:<10} menor: {min(tempos):.4f}s")
