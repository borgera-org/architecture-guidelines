# Architecture Guidelines

Repositorio central e fonte oficial de diretrizes de arquitetura, archetypes, templates e esquemas consumidos por desenvolvedores, agentes de IA e pelo CLI interno de scaffolding.

## Proposito

Este repositorio existe para padronizar a criacao e a evolucao de repositorios consumidores.

Ele concentra:

- diretrizes arquiteturais reutilizaveis
- regras de governanca e evolucao dos padroes
- archetypes de repositorio suportados
- templates oficiais usados em scaffolding
- schemas e contratos estruturados para automacao

O objetivo nao e apenas documentar decisoes. O objetivo e transformar padroes arquiteturais em contratos claros e consumiveis por pessoas e ferramentas.

## Consumidores

Este repositorio foi desenhado para atender tres tipos de consumidores:

- Desenvolvedores
  Usam este repositorio para entender padroes, tomar decisoes coerentes e iniciar novos projetos com menor ambiguidade.
- Agentes de IA
  Usam este repositorio como contexto estavel para geracao de codigo, navegacao de padroes e validacao de aderencia arquitetural.
- CLI interno
  Usa este repositorio como backend oficial para scaffolding, validacao e evolucao de repositorios consumidores.

## Estrutura Atual

A estrutura base atual deste repositorio e:

- `.github/`
  Workflows de automacao e validacao do proprio repositorio.
- `borgera_cli/`
  Implementacao de referencia do CLI que consome os contratos publicados aqui.
- `docs/`
  Documentacao explicativa para humanos e IA.
- `archetypes/`
  Definicoes dos tipos de repositorio suportados pelo CLI.
- `templates/`
  Templates oficiais de arquivos, diretorios e ativos reutilizaveis.
- `schemas/`
  Contratos estruturados para validacao e automacao.
- `examples/`
  Exemplos de saida esperada para archetypes e templates.
- `scripts/`
  Validadores e automacoes locais de apoio ao contrato da plataforma.

## Contrato com o CLI

O CLI interno deve poder assumir que este repositorio fornece:

- definicoes versionadas de archetypes
- templates oficiais e previsiveis
- schemas para validacao de configuracao
- convencoes de nomes e estruturas estaveis
- documentacao suficiente para explicar a intencao dos artefatos automatizados

Isso significa que mudancas neste repositorio podem impactar diretamente os repositorios consumidores. Por esse motivo, estrutura, nomes e formatos devem ser tratados como parte do contrato da plataforma.

## Como Usar

### Baseline Atual

Use [baseline-2026-03-19.md](c:/Users/igors/source/repos/architecture-guidelines/docs/baseline-2026-03-19.md) como checkpoint operacional do estado atual da plataforma.

Para regras de maturidade e promocao de archetypes, use
[archetype-lifecycle.md](c:/Users/igors/source/repos/architecture-guidelines/docs/archetype-lifecycle.md).

A avaliacao formal que promoveu o primeiro archetype para `active` esta em
[api-dotnet-active-evaluation-2026-03-19.md](c:/Users/igors/source/repos/architecture-guidelines/docs/api-dotnet-active-evaluation-2026-03-19.md).

Ele consolida:

- decisoes estruturais ja tomadas
- contratos e convencoes ja adotados
- o que ja esta validado
- principais lacunas e proximos passos

### Para desenvolvedores

Use este repositorio para:

- entender padroes e principios adotados
- descobrir archetypes disponiveis
- consultar templates oficiais
- propor evolucao dos padroes centrais

### Para IA

Use este repositorio como:

- fonte primaria de contexto para padroes organizacionais
- referencia para criacao de novos repositorios
- base para validacao de aderencia entre implementacao e arquitetura

### Para o CLI

Use este repositorio como:

- fonte de verdade para scaffolding
- catalogo de archetypes suportados
- origem dos templates e schemas aplicados na criacao de repositorios
- referencia para a implementacao inicial do proprio CLI

O CLI agora tambem pode ser instalado localmente como comando `borgera`,
apontando para este repositorio via `--contracts-root` ou
`BORGERA_CONTRACTS_ROOT`.

## Limites de Escopo

Este repositorio deve conter:

- padroes transversais e reutilizaveis
- decisoes que valem para multiplos times ou produtos
- contratos consumidos por automacao

Este repositorio nao deve substituir:

- documentacao especifica de arquitetura de um sistema
- ADRs locais de um produto isolado
- decisoes contextuais que so fazem sentido em um unico repositorio consumidor

## Governanca

Como este repositorio e parte do backend da plataforma de scaffolding, alteracoes em archetypes, templates e schemas devem ser tratadas com governanca explicita.

Em especial:

- mudancas compativeis devem ser preferidas
- breaking changes devem ser identificadas claramente
- exemplos e documentacao devem evoluir junto com os contratos
- automacao nao deve depender de texto livre quando um artefato estruturado for mais adequado

## Proximos Passos

Os proximos focos de evolucao deste repositorio sao:

1. iniciar o proximo archetype oficial
2. evoluir a experiencia e distribuicao do CLI
3. evoluir a cobertura de validacao conforme novos archetypes surgirem
4. evoluir a estrategia de versionamento dos contratos da plataforma

Use [baseline-2026-03-19.md](c:/Users/igors/source/repos/architecture-guidelines/docs/baseline-2026-03-19.md) como checkpoint operacional mais atualizado.
