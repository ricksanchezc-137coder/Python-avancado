import asyncio


class ConexaoFake:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco

    async def __aenter__(self):
        print(f"Conectando a '{self.nome_banco}'...")
        await asyncio.sleep(1)
        print("Conectado!")
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        print(f"Desconectando de '{self.nome_banco}'...")
        await asyncio.sleep(0.5)
        if exc_type is not None:
            print(f"__aexit__ rodou mesmo com exceção: {exc_type.__name__}: {exc_value}")
        else:
            print("Desconectado sem erros.")
        # return False (ou None) deixa a exceção propagar normalmente
        return False

    async def query(self, sql):
        print(f"Executando: {sql}")
        await asyncio.sleep(0.5)
        return f"Resultado de '{sql}'"


async def teste_uso_normal():
    print("\n=== 1. Uso normal, sem erro ===")
    async with ConexaoFake("banco_principal") as conexao:
        resultado = await conexao.query("SELECT * FROM usuarios")
        print(resultado)


async def teste_com_excecao():
    print("\n=== 2. Exceção dentro do bloco ===")
    try:
        async with ConexaoFake("banco_principal") as conexao:
            await conexao.query("SELECT * FROM usuarios")
            raise RuntimeError("Falha simulada durante a query")
    except RuntimeError as e:
        print(f"Exceção capturada fora do bloco: {e}")


async def main():
    await teste_uso_normal()
    await teste_com_excecao()


if __name__ == "__main__":
    asyncio.run(main())
