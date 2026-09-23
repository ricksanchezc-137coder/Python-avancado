import asyncio
import contextvars

usuario_atual = contextvars.ContextVar("usuario_atual", default="anônimo")

async def tarefa_filha():
    usuario_atual.set("joao")
    print(f" [dentro da task] usuario_atual.get() = {usuario_atual.get()}")

async def main():
    print(f"[antes] usuario_atual.get() = {usuario_atual.get()}")

    task = asyncio.create_task(tarefa_filha())
    await task

    print(f"[depois] usuario_atual.get() = {usuario_atual.get()}")

asyncio.run(main())
