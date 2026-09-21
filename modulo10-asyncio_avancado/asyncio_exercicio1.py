import asyncio
import time


async def baixar(nome, duracao):
    print(f"Iniciando {nome}...")
    await asyncio.sleep(duracao)
    print(f"{nome} concluído!")
    return f"{nome} ({duracao}s)"


async def forma_sequencial():
    print("\n=== 1. Sequencial (await direto) ===")
    inicio = time.perf_counter()

    r1 = await baixar("arquivo1", 2)
    r2 = await baixar("arquivo2", 1)
    r3 = await baixar("arquivo3", 3)

    fim = time.perf_counter()
    print(f"Resultados: {[r1, r2, r3]}")
    print(f"Tempo total: {fim - inicio:.2f}s")


async def forma_create_task():
    print("\n=== 2. Com create_task ===")
    inicio = time.perf_counter()

    t1 = asyncio.create_task(baixar("arquivo1", 2))
    t2 = asyncio.create_task(baixar("arquivo2", 1))
    t3 = asyncio.create_task(baixar("arquivo3", 3))

    r1 = await t1
    r2 = await t2
    r3 = await t3

    fim = time.perf_counter()
    print(f"Resultados: {[r1, r2, r3]}")
    print(f"Tempo total: {fim - inicio:.2f}s")


async def forma_gather():
    print("\n=== 3. Com gather ===")
    inicio = time.perf_counter()

    resultados = await asyncio.gather(
        baixar("arquivo1", 2),
        baixar("arquivo2", 1),
        baixar("arquivo3", 3),
    )

    fim = time.perf_counter()
    print(f"Resultados: {resultados}")
    print(f"Tempo total: {fim - inicio:.2f}s")


async def main():
    await forma_sequencial()
    await forma_create_task()
    await forma_gather()


if __name__ == "__main__":
    asyncio.run(main())
