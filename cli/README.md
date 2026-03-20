# CLI

## Proposito

Este diretorio contem a primeira implementacao de referencia do CLI que consome os contratos publicados neste repositorio.

Ela existe para exercitar o baseline atual da plataforma com um fluxo real de scaffolding, sem ainda tratar distribuicao, empacotamento ou experiencia final de produto.

## Escopo Atual

No estado atual, o CLI implementa:

- descoberta de archetypes em `archetypes/`
- validacao de `definition.yaml` contra os schemas oficiais
- resolucao de inputs obrigatorios e valores `default`
- selecao de templates com suporte ao subset atual de `when`
- materializacao de payloads estaticos e `.tpl`
- execucao do pos-processamento `solution-add-project`

## Interface Atual

O CLI pode ser executado como modulo Python:

```text
python -m cli list-archetypes
python -m cli scaffold api-dotnet --destination . --set repositoryName=billing-api --set serviceName=billing-api --set solutionName=Billing.Api --set rootNamespace=Billing.Api
```

Tambem e possivel fornecer valores por arquivo YAML:

```text
python -m cli scaffold api-dotnet --destination . --values-file path/to/inputs.yaml
```

## Decisoes da Primeira Versao

- a implementacao foi mantida em Python para reaproveitar o ecossistema de validacao ja existente no repositorio
- o comando `scaffold` cria o repositorio em `--destination/<repositoryName>`
- conflitos de template no mesmo caminho falham explicitamente
- a validacao de constraints continua limitada ao que ja e pragmaticamente verificavel no contrato atual

## O Que Esta Fora do Escopo

Esta primeira implementacao ainda nao cobre:

- distribuicao como ferramenta instalada no ambiente
- interacao guiada por prompts
- criacao de repositorio remoto
- commits Git automaticos
- acoes de pos-processamento alem de `solution-add-project`

## Relacao com os Examples

O script [smoke_test_cli.py](c:/Users/igors/source/repos/architecture-guidelines/scripts/smoke_test_cli.py) usa os manifests oficiais em `examples/` para verificar se o CLI materializa snapshots aderentes ao contrato atual.
