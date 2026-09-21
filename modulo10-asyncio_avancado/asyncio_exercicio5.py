import asyncio
import random
import time


async def stream_numeros(total):
    for i in range(1, total + 1):
        await asyncio.sleep(0.5)
        yield i


async def stream_transacoes(quantidade):
    tipos = ["deposito", "saque", "transferencia"]
    for i in range(1, quantidade + 1):
        await asyncio.sleep(0.4)
        transacao = {
            "id": i,
            "tipo": random.choice(tipos),
            "valor": round(random.uniform(10, 1000), 2),
        }
        yield transacao


async def teste_async_for():
    print("\n=== 1. Consumindo com async for ===")
    inicio = time.perf_counter()

    async for numero in stream_numeros(5):
        print(f"Recebido: {numero}")

    fim = time.perf_counter()
    print(f"Tempo total: {fim - inicio:.2f}s")


async def teste_anext_manual():
    print("\n=== 2. Consumindo manualmente com __anext__ ===")
    gerador = stream_numeros(5)

    for _ in range(3):
        valor = await gerador.__anext__()
        print(f"Peguei manualmente: {valor}")

    print("Parando aqui, sem consumir os 2 restantes.")


async def teste_stream_transacoes():
    print("\n=== 3. Bônus: stream de transações ===")
    async for transacao in stream_transacoes(4):
        print(f"Transação recebida: {transacao}")


async def main():
    await teste_async_for()
    await teste_anext_manual()
    await teste_stream_transacoes()


if __name__ == "__main__":
    asyncio.run(main())
