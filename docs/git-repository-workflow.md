# Git Repository Workflow

## Proposito

Este documento define o fluxo de armazenamento e versionamento em Git para dois contextos diferentes:

- o repositorio central de arquitetura
- os repositorios consumidores gerados ou evoluidos a partir dele

Ele existe para deixar explicito o que deve ser versionado, quando isso deve acontecer e qual deve ser o papel do CLI nesse fluxo.

## Escopo

Este documento trata de:

- o que entra ou nao entra em Git
- como o repositorio central deve evoluir
- como um repositorio consumidor deve nascer
- qual deve ser o comportamento padrao do CLI em relacao a Git

Este documento nao define:

- estrategia de branching detalhada
- politica organizacional completa de PR
- regras de protecao de branch especificas da ferramenta de hospedagem

Para branching, commits, pull requests e release do repositorio central, use
[git-branching-and-release-flow.md](c:/Users/igors/source/repos/architecture-guidelines/docs/git-branching-and-release-flow.md).

## Dois Tipos de Repositorio

### Repositorio central

Este e o proprio repositorio `architecture-guidelines`.

Ele versiona os contratos, templates, schemas, examples e documentos que definem a plataforma.

### Repositorios consumidores

Sao os repositorios criados ou evoluidos a partir dos archetypes publicados neste repositorio.

Eles versionam a instancia concreta do sistema, e nao o contrato generico da plataforma.

## Principios

As regras base para armazenamento em Git sao:

- Git deve guardar fonte de verdade, nao estado temporario da maquina local
- artefatos normativos devem ser versionados
- artefatos efemeros, locais ou regeneraveis nao devem ser versionados
- segredos nao devem ser armazenados em Git
- exemplos materializados so devem ser versionados quando tiverem valor de referencia

## O Que Deve Ser Versionado no Repositorio Central

No repositorio central, devem ser versionados:

- documentacao oficial
- archetypes
- templates
- schemas
- examples de referencia
- scripts de validacao e apoio

No baseline atual, isso inclui explicitamente:

- `docs/`
- `archetypes/`
- `templates/`
- `schemas/`
- `examples/`
- `scripts/`

## O Que Nao Deve Ser Versionado no Repositorio Central

No repositorio central, nao devem ser versionados:

- artefatos de build
- caches locais
- ambientes virtuais
- dependencias restauradas localmente
- logs
- segredos
- configuracoes pessoais de editor nao padronizadas pela plataforma

## O Papel dos Examples no Git

Os examples merecem um comentario separado.

Em geral, artefatos gerados nao deveriam ser versionados.

Mas neste repositorio, examples materializados sao permitidos e desejados quando atuam como:

- snapshot normativo de referencia
- evidencia do resultado esperado do scaffolding
- base de validacao automatizada

Por esse motivo, o snapshot `examples/api-dotnet/minimal-default/billing-api/` deve permanecer versionado.

## Fluxo Esperado do Repositorio Central

O fluxo recomendado para mudancas no repositorio central e:

1. propor a mudanca em branch de trabalho
2. classificar a mudanca segundo [governance.md](c:/Users/igors/source/repos/architecture-guidelines/docs/governance.md)
3. atualizar todos os artefatos afetados pelo contrato
4. validar schemas, examples e scripts relevantes
5. submeter a mudanca para revisao
6. integrar a mudanca na branch principal da plataforma

## Regra de Atualizacao Conjunta

No repositorio central, uma mudanca de contrato nao deve ser mergeada isoladamente quando ela exige artefatos complementares.

Exemplos:

- mudanca em archetype pode exigir atualizacao de schema
- mudanca em template pode exigir atualizacao de example
- mudanca em manifest pode exigir atualizacao de validador

Se o contrato mudou, os artefatos que demonstram ou validam esse contrato devem evoluir junto.

## O Que Deve Ser Versionado em Repositorios Consumidores

Nos repositorios consumidores, devem ser versionados:

- codigo-fonte
- testes automatizados
- configuracoes de runtime nao sensiveis
- artefatos de containerizacao
- documentacao do sistema
- ADRs locais
- arquivos de repositorio e padroes herdados do scaffolding

## O Que Nao Deve Ser Versionado em Repositorios Consumidores

Nos repositorios consumidores, nao devem ser versionados:

- segredos
- configuracoes locais sensiveis
- artefatos de build como `bin/` e `obj/`
- logs
- caches locais
- metadados temporarios de IDE

## Como um Repositorio Consumidor Deve Nascer

O fluxo recomendado para criar um novo repositorio consumidor e:

1. o CLI resolve o archetype e seus inputs
2. o CLI seleciona os templates aplicaveis
3. o CLI materializa os arquivos
4. o CLI executa o pos-processamento necessario
5. o CLI executa validacoes basicas quando disponiveis
6. o repositorio e revisado pelo time responsavel

## Comportamento Padrao do CLI em Relacao a Git

No baseline atual, o comportamento recomendado do CLI e:

- pode inicializar um repositorio Git se isso for explicitamente solicitado
- nao deve fazer `commit` automaticamente por padrao
- nao deve criar remoto automaticamente
- nao deve fazer `push` automaticamente

Motivo:

- commit automatico sem revisao pode esconder problemas de materializacao
- criacao de remoto depende de politica organizacional e credenciais
- push automatico aumenta risco operacional desnecessario no fluxo inicial

## Commit Inicial

O commit inicial do repositorio consumidor deve acontecer apenas depois que:

- a materializacao tiver terminado com sucesso
- o pos-processamento tiver sido concluido
- as validacoes minimas tiverem sido executadas
- o time responsavel revisar o resultado ou optar explicitamente por commit automatico

Recomendacao atual:

- o CLI pode oferecer uma opcao explicita de commit inicial
- o comportamento padrao deve continuar sendo sem commit automatico

## Relacao Entre Repositorio Central e Consumidores

Mudancas no repositorio central nao devem mutar automaticamente repositorios consumidores ja existentes.

O contrato correto e:

- o repositorio central evolui os padroes
- os consumidores adotam essas evolucoes explicitamente
- o CLI pode oferecer fluxos de upgrade no futuro

Isso evita que a plataforma trate repositorios consumidores como copias vivas acopladas diretamente ao estado atual dos templates.

## Atualizacao de Baseline em Consumidores

Quando o baseline central evoluir, o fluxo recomendado para consumidores e:

1. identificar a mudanca relevante no repositorio central
2. avaliar impacto no consumidor
3. aplicar a evolucao em branch propria
4. revisar e validar localmente
5. integrar a mudanca segundo o fluxo normal do time

## Armazenamento de Templates no Git

No repositorio central, templates devem ser armazenados como codigo-fonte do scaffolding.

No baseline atual:

- arquivos `.tpl` representam payload renderizavel
- arquivos sem `.tpl` representam payload estatico

Esses artefatos devem ser versionados porque sao parte da fonte de verdade da plataforma.

## Branch Principal

Este documento assume que existe uma branch principal estavel da plataforma, independentemente do nome adotado pela organizacao.

Exemplos de nome possivel:

- `main`
- `master`
- `trunk`
- `develop`, se esse for o padrao organizacional

O ponto importante nao e o nome da branch, e sim o papel:

- ela deve representar o estado estavel e consumivel do repositorio central

## Tags e Versionamento

No estado atual, o repositorio ainda nao formalizou uma estrategia de release tagging para contratos da plataforma.

Mesmo assim, a direcao recomendada e:

- contratos importantes devem evoluir com versionamento explicito
- no futuro, o CLI deve poder consumir versoes identificaveis dos padroes centrais

## Regra Pratica

Se um artefato precisa ser preservado para explicar, validar ou reproduzir o comportamento oficial da plataforma, ele deve ser versionado.

Se ele existe apenas por causa do ambiente local, da execucao temporaria ou de um estado regeneravel, ele nao deve ser versionado.
