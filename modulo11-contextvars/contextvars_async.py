import asyncio
import contextvars

usuario_atual = contextvars.ContextVar("usuario_atual", default="anônimo")

async def processar(nome, delay):
    usuario_atual.set(nome)
    await asyncio.sleep(delay)

    print(f"[{nome}] usuario_atual.get() = {usuario_atual.get()}")

async def main():
    await asyncio.gather(
        processar("joao", 1),
        processar("maria", 0.5),
    )

asyncio.run(main())
