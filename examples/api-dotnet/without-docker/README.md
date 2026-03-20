# API .NET Without Docker

## Proposito

Este example representa o cenario do archetype `api-dotnet` em que a API e
materializada sem os artefatos basicos de Docker.

Ele existe para provar que a plataforma consegue gerar um repositorio valido
quando `includeDocker = false`, sem deixar residuos do template
`docker-files`.

## Cenario Representado

Este example assume:

- API HTTP em `.NET`
- projeto principal da API
- projeto inicial de testes
- ausencia de artefatos de Docker
- solution com projeto principal e projeto de testes adicionados pelo CLI

## Inputs de Referencia

Os inputs de referencia deste example sao:

- `repositoryName`: `billing-api`
- `serviceName`: `billing-api`
- `solutionName`: `Billing.Api`
- `rootNamespace`: `Billing.Api`
- `targetFramework`: `net8.0`
- `dotnetImageTag`: `8.0`
- `includeTests`: `true`
- `includeDocker`: `false`

## Templates Aplicados

Os templates esperados neste cenario sao:

- `repository-files`
- `dotnet-solution`
- `api-project`
- `test-project`

Neste cenario, o template `docker-files` nao deve ser aplicado.

## Pos-processamento Esperado

Neste cenario, o CLI deve executar pelo menos os seguintes passos apos
materializar os arquivos:

- adicionar `src/Billing.Api/Billing.Api.csproj` a solution `Billing.Api.sln`
- adicionar `tests/Billing.Api.Tests/Billing.Api.Tests.csproj` a solution `Billing.Api.sln`

O comportamento de pos-processamento continua igual ao do cenario padrao, pois
ele depende de `includeTests`, nao de `includeDocker`.

## Estrutura Esperada

A estrutura esperada para este example e, no minimo:

```text
without-docker/
  billing-api/
    .editorconfig
    .gitattributes
    .gitignore
    README.md
    Billing.Api.sln
    Directory.Build.props
    src/
      Billing.Api/
        Billing.Api.csproj
        Program.cs
        appsettings.json
        appsettings.Development.json
        Properties/
          launchSettings.json
    tests/
      Billing.Api.Tests/
        Billing.Api.Tests.csproj
        HealthEndpointTests.cs
```

Os arquivos `Dockerfile` e `.dockerignore` nao devem existir neste snapshot.

## O Que Este Example Valida

Este example ajuda a validar:

- selecao condicional de templates com `includeDocker = false`
- ausencia dos artefatos do template `docker-files`
- permanencia da estrutura de testes e do pos-processamento da solution
- integridade do baseline da API sem containerizacao inicial

O arquivo `manifest.yaml` deste diretorio representa a mesma referencia em
formato legivel por maquina.

No estado atual da plataforma, esse manifesto deve ser validado por
[example-manifest.schema.json](c:/Users/igors/source/repos/architecture-guidelines/schemas/example-manifest.schema.json).

## Proximo Passo

O proximo passo esperado para este example e validar de forma automatizada se o
snapshot materializado continua aderente aos contratos e templates oficiais.
