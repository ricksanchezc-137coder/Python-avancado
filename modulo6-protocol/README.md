# Módulo 6 — typing.Protocol

## O que foi feito

Praticado isolado do sistema-bancario (mesmo padrão dos Módulos 4 e 5), em `protocol_exemplo.py`:

- Protocolo `Exportavel` com método `exportar() -> str`, decorado com `@runtime_checkable`
- Classes `RelatorioJSON` e `RelatoriosTexto` satisfazendo o protocolo sem herdar dele
- Função genérica `processar_exportacao()` aceitando qualquer classe que satisfaça o protocolo
- Testes com `isinstance()` confirmando a checagem estrutural em runtime
- Classe `Pegadinha` para expor a limitação do `runtime_checkable` (não confere assinatura)
- Protocolo `TemTitulo` com atributo (não método), testado contra as instâncias existentes

## O que foi visto no módulo

- `typing.Protocol`: interfaces estruturais (duck typing formalizado), sem herança
- Diferença entre interface estrutural (`Protocol`) e nominal (`ABC`)
- `@runtime_checkable` para habilitar `isinstance()`/`issubclass()`
- Protocol também pode exigir atributos, não só métodos

## O que foi aprendido

- `runtime_checkable` checa apenas a existência de nomes (métodos/atributos), nunca assinatura ou tipo de retorno — quem garante isso é o type checker estático, não o `isinstance()`
- Um Protocol de atributo é satisfeito pela instância, então até um atributo adicionado dinamicamente faria o `isinstance()` retornar `True`
- Quando usar `Protocol` em vez de `ABC`: aceitar "qualquer coisa com esse comportamento", inclusive tipos que não controlamos, sem forçar herança
