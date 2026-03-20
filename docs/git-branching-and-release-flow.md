# Git Branching and Release Flow

## Proposito

Este documento define o fluxo recomendado de branching, integracao e release
para o repositorio central `architecture-guidelines`.

Ele complementa [git-repository-workflow.md](c:/Users/igors/source/repos/architecture-guidelines/docs/git-repository-workflow.md),
que trata do que deve ser versionado e do papel do Git na plataforma.

Aqui o foco e responder:

- como mudancas devem nascer
- como devem ser integradas
- como devem ser revisadas
- quando devem gerar tag ou release

## Recomendacao Geral

O fluxo recomendado para este repositorio e trunk-based simples com branch
principal protegida.

No estado atual, isso significa:

- `main` como unica branch estavel e consumivel
- branches curtas de trabalho
- integracao por pull request
- `squash merge` como padrao

## Por Que Este Fluxo E O Mais Adequado

Este repositorio publica contratos consumidos por:

- desenvolvedores
- agentes de IA
- o CLI interno

Por isso, o ponto mais importante nao e ter uma arvore complexa de branches.
O ponto mais importante e manter uma branch principal sempre coerente, legivel
e consumivel.

Fluxos como GitFlow classico tendem a adicionar cerimonia demais para o estado
atual da plataforma.

## Branch Principal

A branch principal oficial da plataforma e:

- `main`

Ela deve representar:

- o estado estavel do repositorio
- o contrato atualmente consumivel da plataforma
- a referencia para novos trabalhos

Recomendacao operacional:

- proteger `main`
- evitar push direto
- exigir revisao antes de merge

## Fluxo de Trabalho Recomendado

O fluxo diario recomendado e:

1. atualizar `main`
2. criar uma branch curta de trabalho
3. implementar a mudanca completa
4. atualizar artefatos afetados pelo contrato
5. executar validacoes relevantes
6. abrir pull request
7. integrar em `main` via `squash merge`

## Branches de Trabalho

Branches de trabalho devem ser:

- curtas
- focadas em uma mudanca coerente
- descartaveis depois do merge

Evite:

- branches de longa duracao
- branches guarda-chuva com mudancas sem relacao direta
- acumular multiplas decisoes contratuais na mesma branch

## Padrao de Nome de Branch

O padrao recomendado e:

- `feat/...`
- `fix/...`
- `docs/...`
- `chore/...`
- `refactor/...`

Exemplos:

- `feat/post-processing-contract`
- `fix/example-validator`
- `docs/git-release-flow`
- `chore/root-gitignore`
- `refactor/template-layout`

## Pull Request

Toda mudanca relevante deve entrar por pull request.

O pull request deve deixar claro:

- qual problema esta sendo resolvido
- qual o tipo de mudanca segundo [governance.md](c:/Users/igors/source/repos/architecture-guidelines/docs/governance.md)
- quais contratos foram afetados
- qual o impacto em CLI, IA e futuros consumidores
- quais validacoes foram executadas

## Checklist Minimo de Pull Request

Antes de mergear, o pull request deve responder:

- a mudanca e editorial, aditiva compativel, evolutiva com impacto ou breaking
- archetypes, schemas, templates e examples afetados foram atualizados juntos
- a documentacao narrativa continua coerente com os contratos estruturados
- exemplos e validadores continuam representando o estado esperado
- existe necessidade de migracao ou deprecacao

## Estrategia de Merge

O merge recomendado para este repositorio e:

- `squash merge`

Motivos:

- reduz ruido historico
- preserva um historico mais legivel na branch principal
- ajuda a manter uma relacao mais clara entre PR e commit final

Evite, como padrao:

- merge commit para PRs pequenas e medias
- rebase manual em branches compartilhadas sem necessidade

## Commits

O padrao recomendado e Conventional Commits simplificado.

Formato sugerido:

- `feat(scope): ...`
- `fix(scope): ...`
- `docs(scope): ...`
- `chore(scope): ...`
- `refactor(scope): ...`

Exemplos:

- `feat(archetype): add declarative postProcessing`
- `fix(schema): validate dotnetImageTag as string`
- `docs(git): define branching and release flow`

## Relacao Entre Commit E PR

Durante a branch de trabalho, os commits podem ser mais granulares.

Mas o estado final em `main` deve ficar limpo e coerente. Por isso, `squash
merge` e o padrao preferido.

Em termos simples:

- branch de trabalho pode ter varios commits
- `main` deve preservar uma historia mais sintetica

## Quando Nao Fazer Push Direto em `main`

No fluxo recomendado, push direto em `main` deve ser evitado quase sempre.

Excecoes possiveis:

- manutencao operacional extremamente controlada
- ajuste urgente feito por mantenedor com responsabilidade explicita
- situacao em que o processo de PR esteja indisponivel e o risco de nao agir seja maior

Mesmo nesses casos, a excecao deve ser rara.

## Tags e Releases

No estado atual, a plataforma ainda nao depende formalmente de tags para ser
consumida pelo CLI.

Mesmo assim, a direcao recomendada e preparar esse modelo desde ja.

## Quando Gerar Tag

Uma tag passa a fazer sentido quando houver:

- um baseline claramente consumivel
- mudanca relevante de contrato
- nova capacidade compativel que deva ser referenciada
- breaking change com migracao explicita

## Estrategia de Versionamento Recomendada

Enquanto a plataforma ainda amadurece, o formato recomendado e:

- `v0.x.y`

Interpretacao sugerida:

- `patch` para correcao ou ajuste sem impacto contratual relevante
- `minor` para mudanca compativel ou nova capacidade
- `major` para breaking change

Exemplos:

- `v0.1.0` primeiro baseline formal consumivel
- `v0.2.0` nova capacidade compativel
- `v1.0.0` contrato suficientemente estavel para consumo mais formal

## Relacao com o CLI

Hoje o CLI ainda nao consome uma release versionada deste repositorio como
requisito obrigatorio.

A direcao recomendada e:

- primeiro estabilizar contratos
- depois introduzir tagging e release identificavel
- por fim permitir que o CLI consuma versoes explicitas da plataforma

## O Que Evitar

Evite neste repositorio:

- GitFlow classico sem necessidade real
- branch `develop` como copia permanente de `main`
- merges grandes e pouco revisaveis
- PRs que alteram contratos sem atualizar examples e validacao
- criar tags sem significado contratual claro

## Regra Pratica

Se o fluxo de Git tornar mais dificil entender qual e o estado oficial
consumivel da plataforma, ele esta complexo demais para este repositorio.

O objetivo e manter `main` pequena, estavel e confiavel.
