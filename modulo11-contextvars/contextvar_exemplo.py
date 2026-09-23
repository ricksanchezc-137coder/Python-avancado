import contextvars

usuario_atual = contextvars.ContextVar("Usuario_atual", default="anônimo")

def mostrar_usuario():
    print(f"Usuario atual: {usuario_atual.get()}")

mostrar_usuario()


token = usuario_atual.set("joao")

mostrar_usuario()

usuario_atual.reset(token)
mostrar_usuario()
