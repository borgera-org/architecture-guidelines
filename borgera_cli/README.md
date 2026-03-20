# CLI

## Proposito

Este diretorio contem a implementacao de referencia do CLI que consome os contratos publicados neste repositorio.

Ele existe para exercitar o baseline atual da plataforma com um fluxo real de scaffolding e, agora, tambem pode ser instalado como comando local `borgera`.

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
python -m borgera_cli list-archetypes
python -m borgera_cli scaffold api-dotnet --destination . --set repositoryName=billing-api --set serviceName=billing-api --set solutionName=Billing.Api --set rootNamespace=Billing.Api
```

Tambem e possivel fornecer valores por arquivo YAML:

```text
python -m borgera_cli scaffold api-dotnet --destination . --values-file path/to/inputs.yaml
```

## Instalacao

Para instalar o CLI no ambiente local a partir deste repositorio:

```text
python -m pip install -e .
```

Depois disso, o comando `borgera` fica disponivel no terminal:

```text
borgera list-archetypes
borgera scaffold api-dotnet --destination . --set repositoryName=billing-api --set serviceName=billing-api --set solutionName=Billing.Api --set rootNamespace=Billing.Api
```

## Contracts Root

O CLI agora aceita um contracts root explicito para funcionar a partir de qualquer workspace:

```text
borgera list-archetypes --contracts-root C:/Users/igors/source/repos/architecture-guidelines
borgera scaffold api-dotnet --contracts-root C:/Users/igors/source/repos/architecture-guidelines --destination C:/Users/igors/source/repos
```

Tambem e possivel definir a variavel de ambiente `BORGERA_CONTRACTS_ROOT`.

Com isso, o CLI pode:

- inferir o contracts root quando instalado de forma editavel a partir deste repo
- apontar para um clone especifico do repositório central
- ser usado em outra instancia do VSCode sem precisar abrir este workspace

## Decisoes da Primeira Versao

- a implementacao foi mantida em Python para reaproveitar o ecossistema de validacao ja existente no repositorio
- o CLI pode ser instalado com `pip` e exposto como comando `borgera`
- o motor do CLI consome um contracts root externo em vez de depender do workspace atual
- o comando `scaffold` cria o repositorio em `--destination/<repositoryName>`
- conflitos de template no mesmo caminho falham explicitamente
- a validacao de constraints continua limitada ao que ja e pragmaticamente verificavel no contrato atual

## O Que Esta Fora do Escopo

Esta primeira implementacao ainda nao cobre:

- interacao guiada por prompts
- criacao de repositorio remoto
- commits Git automaticos
- acoes de pos-processamento alem de `solution-add-project`

## Relacao com os Examples

O script [smoke_test_cli.py](c:/Users/igors/source/repos/architecture-guidelines/scripts/smoke_test_cli.py) usa os manifests oficiais em `examples/` para verificar se o CLI materializa snapshots aderentes ao contrato atual.
