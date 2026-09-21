import asyncio


async def baixar(nome, duracao, falha=False):
    print(f"Iniciando {nome}...")
    await asyncio.sleep(duracao)
    if falha:
        raise ValueError(f"Erro ao baixar {nome}")
    print(f"{nome} concluído!")
    return f"{nome} ({duracao}s)"


async def teste_com_cancelamento_manual():
    print("\n=== c. Cancelando tasks irmãs ao detectar falha ===")

    tasks = [
        asyncio.create_task(baixar("arquivo1", 2)),
        asyncio.create_task(baixar("arquivo2", 1, falha=True)),
        asyncio.create_task(baixar("arquivo3", 3)),
    ]

    # espera até a PRIMEIRA exceção aparecer, sem esperar as outras terminarem
    done, pending = await asyncio.wait(
        tasks, return_when=asyncio.FIRST_EXCEPTION
    )

    # cancela tudo que ainda não terminou
    for task in pending:
        print(f"Cancelando task pendente: {task.get_name()}")
        task.cancel()

    # espera as canceladas realmente encerrarem (evita warnings)
    if pending:
        await asyncio.gather(*pending, return_exceptions=True)

    # checa o que terminou em 'done' — pode ter sucesso ou exceção
    for task in done:
        if task.exception():
            print(f"Task terminou com erro: {task.exception()}")
        else:
            print(f"Task terminou com sucesso: {task.result()}")


async def main():
    await teste_com_cancelamento_manual()


if __name__ == "__main__":
    asyncio.run(main())
