from typing import Protocol, runtime_checkable

@runtime_checkable
class Exportavel(Protocol):
    def exportar(self) -> str: ...

class RelatorioJSON:
    def __init__(self, dados: dict):
        self.dados = dados

    def exportar(self) -> str:
        import json
        return json.dumps(self.dados)

class RelatoriosTexto:
    def __init__(self, titulo: str, conteudo : str):
        self.titulo = titulo
        self.conteudo = conteudo

    def exportar(self) -> str:
        return f"{self.titulo}\n{self.conteudo}"

class Pegadinha:
    def exportar(self, *args, **kwargs):
        pass

@runtime_checkable
class TemTitulo(Protocol):
    titulo: str

def processar_exportacao(item: Exportavel) -> None:
    print(item.exportar())

relatorio1 = RelatorioJSON({"nome": "João", "modulo": 6})
relatorio2 = RelatoriosTexto("Titulo", "Conteudo de teste")

processar_exportacao(relatorio1)
processar_exportacao(relatorio2)

print(isinstance(relatorio1, Exportavel))
print(isinstance(relatorio2, Exportavel))
print(isinstance(42, Exportavel))

print(isinstance(Pegadinha(), Exportavel))

print(isinstance(relatorio2, TemTitulo))
print(isinstance(relatorio1, TemTitulo))
