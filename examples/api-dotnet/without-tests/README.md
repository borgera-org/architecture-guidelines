# API .NET Without Tests

## Proposito

Este example representa o cenario do archetype `api-dotnet` em que a API e
materializada sem o projeto inicial de testes.

Ele existe para provar que a plataforma consegue gerar um repositorio valido
quando `includeTests = false`, sem deixar residuos de template nem
pos-processamento indevido.

## Cenario Representado

Este example assume:

- API HTTP em `.NET`
- projeto principal da API
- artefatos basicos de Docker
- ausencia de projeto inicial de testes
- solution com apenas o projeto principal adicionado pelo CLI

## Inputs de Referencia

Os inputs de referencia deste example sao:

- `repositoryName`: `billing-api`
- `serviceName`: `billing-api`
- `solutionName`: `Billing.Api`
- `rootNamespace`: `Billing.Api`
- `targetFramework`: `net8.0`
- `dotnetImageTag`: `8.0`
- `includeTests`: `false`
- `includeDocker`: `true`

## Templates Aplicados

Os templates esperados neste cenario sao:

- `repository-files`
- `dotnet-solution`
- `api-project`
- `docker-files`

Neste cenario, o template `test-project` nao deve ser aplicado.

## Pos-processamento Esperado

Neste cenario, o CLI deve executar pelo menos o seguinte passo apos
materializar os arquivos:

- adicionar `src/Billing.Api/Billing.Api.csproj` a solution `Billing.Api.sln`

O CLI nao deve tentar adicionar projeto de testes a solution.

## Estrutura Esperada

A estrutura esperada para este example e, no minimo:

```text
without-tests/
  billing-api/
    .dockerignore
    .editorconfig
    .gitattributes
    .gitignore
    README.md
    Billing.Api.sln
    Directory.Build.props
    Dockerfile
    src/
      Billing.Api/
        Billing.Api.csproj
        Program.cs
        appsettings.json
        appsettings.Development.json
        Properties/
          launchSettings.json
```

O diretorio `tests/` nao deve existir neste snapshot.

## O Que Este Example Valida

Este example ajuda a validar:

- selecao condicional de templates com `includeTests = false`
- ausencia de projeto de testes no snapshot materializado
- ausencia de passo de `postProcessing` para projeto de testes
- integridade da solution contendo apenas o projeto principal

O arquivo `manifest.yaml` deste diretorio representa a mesma referencia em
formato legivel por maquina.

No estado atual da plataforma, esse manifesto deve ser validado por
[example-manifest.schema.json](c:/Users/igors/source/repos/architecture-guidelines/schemas/example-manifest.schema.json).

## Proximo Passo

O proximo passo esperado para este example e validar de forma automatizada se o
snapshot materializado continua aderente aos contratos e templates oficiais.
