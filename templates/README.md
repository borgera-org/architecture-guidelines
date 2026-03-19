# Templates

## Proposito

Este diretorio concentra os templates oficiais usados pela plataforma para materializar archetypes em repositorios reais.

Se o archetype representa a planta do repositorio, o template representa o material aplicado durante o scaffolding.

## O Que E Um Template

Um template e um ativo reutilizavel usado para gerar parte da estrutura final de um repositorio consumidor.

Um template pode representar:

- um arquivo
- um conjunto de arquivos
- uma estrutura de diretorios
- uma configuracao base
- um bloco reutilizavel aplicado em diferentes archetypes

O template nao deve decidir sozinho quando deve ser usado. Essa decisao pertence ao archetype.

## Relacao Entre Archetype e Template

A relacao correta e:

- o archetype define a intencao
- o archetype declara qual `templateSet` deve ser aplicado
- o `templateSet` referencia templates oficiais
- os templates materializam arquivos, diretorios e configuracoes

Isso evita dois erros comuns:

- colocar regra arquitetural dentro do template
- colocar conteudo operacional detalhado diretamente no archetype

## O Que E Um Template Set

Um `templateSet` e um agrupamento logico de templates usado por um archetype.

Ele existe para:

- simplificar a definicao do archetype
- permitir reutilizacao de conjuntos coerentes
- separar a intencao do tipo de repositorio da implementacao dos arquivos

Um `templateSet` tambem pode conter aplicacao condicional de templates quando o comportamento depender de inputs do archetype, como `includeTests` ou `includeDocker`.

Exemplo conceitual:

- archetype `api-dotnet`
- `templateSet` `api-dotnet-base`
- templates `repository-files`, `dotnet-solution`, `api-project`, `test-project`, `docker-files`

## Por Que Este Diretorio Existe

Este diretorio existe para evitar que:

- o CLI precise manter arquivos base embutidos no codigo
- cada time copie repositorios antigos para iniciar um novo projeto
- a organizacao trate scaffolding como processo manual
- a evolucao de estruturas base fique espalhada em varios lugares

Ao centralizar templates aqui, a plataforma ganha:

- reuso
- versionamento
- governanca
- previsibilidade para CLI e IA

## Estrutura Esperada

A estrutura inicial recomendada e:

```text
templates/
  README.md
  <template-id>/
    README.md
    files/
```

Onde:

- `<template-id>/README.md`
  Explica o objetivo do template, quando ele deve ser usado e quais artefatos ele gera.
- `<template-id>/files/`
  Contem os arquivos-base usados pelo scaffolding.

No futuro, a estrutura pode crescer para suportar manifests ou metadados adicionais, mas a base deve continuar previsivel.

## Convencao de Identidade

Cada template deve possuir um identificador estavel.

Recomendacoes:

- usar minusculas
- usar `kebab-case`
- refletir claramente o papel do template
- evitar nomes vagos como `default`, `base` ou `common` quando usados sozinhos

Exemplos melhores:

- `repository-files`
- `dotnet-solution`
- `api-project`
- `test-project`
- `docker-files`

## O Que Um Template Deve Conter

Um template deve conter apenas o necessario para materializar um fragmento reutilizavel do repositorio final.

Exemplos adequados:

- `README` inicial
- `.gitignore`
- `Dockerfile`
- estrutura base de solution
- projeto inicial da API
- projeto inicial de testes

Exemplos inadequados:

- regras de selecao do tipo de repositorio
- decisoes de alto nivel que pertencem ao archetype
- configuracoes altamente especificas de um unico produto

## O Que Deve Ser Parametrizado

Templates tendem a precisar de substituicoes de valores.

Exemplos comuns:

- nome do repositorio
- nome do servico
- namespace raiz
- nome da solution
- framework alvo

A regra importante e:

- o template recebe parametros
- o archetype define quais parametros existem
- o CLI resolve e injeta esses parametros

Isso preserva a separacao de responsabilidades.

## Convencao de Autoria

Para distinguir payload estatico de payload renderizavel, este repositorio adota a seguinte convencao:

- arquivos com sufixo `.tpl` devem ser renderizados pelo CLI e materializados sem o sufixo no destino
- arquivos sem sufixo `.tpl` devem ser copiados literalmente

Exemplos:

- `Dockerfile.tpl` -> `Dockerfile`
- `README.md.tpl` -> `README.md`
- `.gitignore` -> `.gitignore`

## O Que O CLI Deve Poder Fazer com um Template

Ao consumir templates, o CLI deve conseguir:

- localizar templates pelo identificador
- aplicar um conjunto de templates em ordem previsivel
- resolver parametros vindos do archetype
- gerar arquivos e diretorios no repositorio consumidor
- detectar conflitos ou sobreposicoes relevantes

O CLI nao deveria depender de caminhos implicitos ou de conteudo escondido fora deste diretorio.

## O Que A IA Deve Poder Fazer com um Template

Ao consultar templates, agentes de IA devem conseguir:

- entender quais artefatos compoem um archetype
- sugerir modificacoes coerentes com o padrao oficial
- explicar a diferenca entre estrutura recomendada e customizacao local

Para isso, templates precisam ser nomeados e organizados de forma previsivel.

## Regra de Qualidade

Um novo template so deve ser criado quando:

- ele representa um bloco reutilizavel real
- existe chance concreta de reaproveitamento
- o papel dele e claro para humanos, IA e CLI
- ele nao esta duplicando outro template com diferenca irrelevante

Se um arquivo existe apenas para um unico caso altamente especifico, ele provavelmente nao deveria nascer como template oficial.

## Proximo Passo

Os proximos artefatos esperados neste diretorio sao os primeiros templates oficiais referenciados pelo archetype `api-dotnet`.
