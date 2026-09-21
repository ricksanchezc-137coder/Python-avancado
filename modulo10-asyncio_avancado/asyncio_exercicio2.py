import asyncio


async def baixar(nome, duracao, falha=False):
    print(f"Iniciando {nome}...")
    await asyncio.sleep(duracao)
    if falha:
        raise ValueError(f"Erro ao baixar {nome}")
    print(f"{nome} concluído!")
    return f"{nome} ({duracao}s)"


async def teste_sem_return_exceptions():
    print("\n=== a1. gather SEM return_exceptions (padrão) ===")
    try:
        resultados = await asyncio.gather(
            baixar("arquivo1", 2),
            baixar("arquivo2", 1, falha=True),
            baixar("arquivo3", 3),
        )
        print(f"Resultados: {resultados}")
    except ValueError as e:
        print(f"gather propagou a exceção: {e}")


async def teste_com_return_exceptions():
    print("\n=== a2. gather COM return_exceptions=True ===")
    resultados = await asyncio.gather(
        baixar("arquivo1", 2),
        baixar("arquivo2", 1, falha=True),
        baixar("arquivo3", 3),
        return_exceptions=True,
    )
    print(f"Resultados: {resultados}")
    for r in resultados:
        if isinstance(r, Exception):
            print(f"  -> Item veio como exceção: {r!r}")


async def teste_cancelamento():
    print("\n=== b. Cancelamento de Task ===")
    task = asyncio.create_task(baixar("arquivo_grande", 10))

    await asyncio.sleep(1)
    print("Cancelando task após 1s...")
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Task cancelada com sucesso")

    print(f"task.cancelled() = {task.cancelled()}")


async def main():
    await teste_sem_return_exceptions()
    await teste_com_return_exceptions()
    await teste_cancelamento()


if __name__ == "__main__":
    asyncio.run(main())
