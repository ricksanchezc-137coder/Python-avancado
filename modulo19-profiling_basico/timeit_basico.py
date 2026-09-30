import timeit

t1 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
t2 = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
t3 = timeit.timeit('"-".join(map(str, range(100)))', number=10000)

print(f"gerador:     {t1:.4f}s")
print(f"list comp:   {t2:.4f}s")
print(f"map:         {t3:.4f}s")
