import asyncio

usuario_global = "anônimo"

async def processar(nome, delay):
    global usuario_global
    usuario_global = nome
    await asyncio.sleep(delay)
    print(f"[{nome}] usuario_global = {usuario_global}")


async def main():
    await asyncio.gather(
        processar("joao", 1),
        processar("maria", 0.5),
    )

asyncio.run(main())
