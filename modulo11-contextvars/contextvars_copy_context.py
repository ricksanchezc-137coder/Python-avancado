import contextvars

usuario_atual = contextvars.ContextVar("usuario_atual", default="anônimo")

def definir_e_mostrar(nome):
    usuario_atual.set(nome)
    print(f"[dentro do contexto copiado] usuario_atual.get() = {usuario_atual.get()}")

usuario_atual.set("original")
print(f"[antes] usuario_atual.get() = {usuario_atual.get()}")

ctx = contextvars.copy_context()

ctx.run(definir_e_mostrar, "joao")

print(f"[depois] usuario_atual.get() = {usuario_atual.get()}")
