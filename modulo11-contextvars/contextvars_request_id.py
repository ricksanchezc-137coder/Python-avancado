import asyncio
import contextvars
import uuid

request_id = contextvars.ContextVar("request_id", default=None)

def log(mensagem):
    rid = request_id.get()
    print(f"[req={rid}] {mensagem}")

async def funcao_interna():
    log ("processando etapa interna")
    await asyncio.sleep(0.3)
    log("etapa interna concluida")

async def atender_requisicao(nome_requisicao, delay_inicial):
    request_id.set(f"{nome_requisicao}-{uuid.uuid4().hex[:6]}")
    await asyncio.sleep(delay_inicial)
    log("requisicao iniciada")
    await funcao_interna()
    log("requisicao finalizada")

async def main():
    await asyncio.gather(
        atender_requisicao("A", 0.1),
        atender_requisicao("B", 0.2),
        atender_requisicao("C", 0),
    )

asyncio.run(main())
