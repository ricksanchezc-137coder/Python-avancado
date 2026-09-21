import asyncio
import time

async def tarefa_a():
    print("Tarefa A: comecou")
    await asyncio.sleep(2)
    print("Tarefa A: terminou")
    return "resultado A"

async def tarefa_b():
    print("Tarefa B: comecou")
    await asyncio.sleep(1)
    print("Tarefa B: terminou")
    return "resultado B"

async def main():
    inicio = time.perf_counter()

    resultado = await asyncio.gather(tarefa_a(), tarefa_b())

    fim = time.perf_counter()
    print(f"Resultados: {resultado}")
    print(f"Tempo total: {fim - inicio:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
