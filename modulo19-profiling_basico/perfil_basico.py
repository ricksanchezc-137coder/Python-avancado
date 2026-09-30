import cProfile

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def contar_primos(limite):
    return sum(1 for n in range(limite) if eh_primo(n))

def principal():
    print(contar_primos(10000))

cProfile.run("principal()", sort="cumulative")
