# API .NET Minimal Default

## Proposito

Este example representa o cenario padrao e mais completo do archetype `api-dotnet` no estado atual da plataforma.

Ele existe para mostrar a saida esperada quando o archetype e materializado com os valores padrao para inclusao de testes e artefatos de Docker.

## Cenario Representado

Este example assume:

- API HTTP em `.NET`
- projeto principal da API
- projeto inicial de testes
- artefatos basicos de Docker
- solution com os projetos adicionados pelo CLI

## Inputs de Referencia

Os inputs de referencia deste example sao:

- `repositoryName`: `billing-api`
- `serviceName`: `billing-api`
- `solutionName`: `Billing.Api`
- `rootNamespace`: `Billing.Api`
- `targetFramework`: `net8.0`
- `dotnetImageTag`: `8.0`
- `includeTests`: `true`
- `includeDocker`: `true`

## Templates Aplicados

Os templates esperados neste cenario sao:

- `repository-files`
- `dotnet-solution`
- `api-project`
- `test-project`
- `docker-files`

## Pos-processamento Esperado

Neste cenario, o CLI deve executar pelo menos os seguintes passos apos materializar os arquivos:

- adicionar `src/Billing.Api/Billing.Api.csproj` a solution `Billing.Api.sln`
- adicionar `tests/Billing.Api.Tests/Billing.Api.Tests.csproj` a solution `Billing.Api.sln`

Sem esse pos-processamento, a saida final nao representa corretamente o contrato do archetype.

## Estrutura Esperada

A estrutura esperada para este example e, no minimo:

```text
minimal-default/
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
    tests/
      Billing.Api.Tests/
        Billing.Api.Tests.csproj
        HealthEndpointTests.cs
```

## O Que Este Example Valida

Este example ajuda a validar:

- render de placeholders em caminho e conteudo
- remocao correta do sufixo `.tpl`
- selecao de templates condicionais com valores padrao
- montagem da solution com projeto principal e projeto de testes
- combinacao coerente entre repositorio, solution, API, testes e Docker

O arquivo `manifest.yaml` deste diretorio representa a mesma referencia em formato legivel por maquina.

No estado atual da plataforma, esse manifesto deve ser validado por [example-manifest.schema.json](c:/Users/igors/source/repos/architecture-guidelines/schemas/example-manifest.schema.json).

## O Que Este Example Ainda Nao Mostra

Este example ainda nao cobre:

- cenario sem testes
- cenario sem Docker
- evolucao de configuracoes locais de dominio
- validacao automatizada entre snapshot e contratos

## Proximo Passo

O proximo passo esperado para este example e validar de forma automatizada se o snapshot materializado continua aderente aos contratos e templates oficiais.

No estado atual da plataforma, essa validacao pode ser iniciada com [validate_example.py](c:/Users/igors/source/repos/architecture-guidelines/scripts/validate_example.py).
