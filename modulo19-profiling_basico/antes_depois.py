import math
import timeit

def eh_primo_v1(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def eh_primo_v2(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def contar(eh_primo, limite):
    return sum(1 for n in range(limite) if eh_primo(n))


assert contar(eh_primo_v1, 2000) == contar(eh_primo_v2, 2000)

for nome, funcao in [("v1 (ate n)", eh_primo_v1), ("v2 (ate raiz)", eh_primo_v2)]:
    tempos = timeit.repeat(lambda: contar(funcao, 10000), number=1, repeat=3)
    print(f"{nome:<14} menor: {min(tempos):.4f}s")
