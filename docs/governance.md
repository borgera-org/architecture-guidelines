# Governance

## Proposito

Este documento define como os contratos centrais deste repositorio podem evoluir com controle.

Como este repositorio e consumido por desenvolvedores, agentes de IA e pelo CLI interno, uma mudanca aqui nao afeta apenas documentacao. Ela pode afetar criacao de repositorios, validacao, onboarding e automacao.

Governanca, neste contexto, existe para responder quatro perguntas:

- quem pode propor mudancas
- como avaliar impacto
- quando uma mudanca e compativel
- como tratar breaking changes

## Por Que Governanca E Necessaria

Sem governanca, este repositorio corre o risco de virar:

- um conjunto de padroes inconsistentes
- uma fonte instavel para o CLI
- um contexto ambiguo para IA
- um ponto de quebra para repositorios consumidores

Como este repositorio funciona como backend da plataforma de scaffolding, mudancas em contratos estruturados precisam de mais rigor do que mudancas em texto livre.

## Principios de Governanca

As mudancas neste repositorio devem seguir estes principios:

- clareza antes de velocidade
- compatibilidade antes de conveniencia local
- evolucao incremental antes de refatoracao ampla
- contratos estruturados antes de convencoes implicitas
- exemplos e documentacao atualizados junto com os artefatos

## Tipos de Artefato

Nem todo arquivo neste repositorio tem o mesmo peso de governanca.

### Documentacao explicativa

Exemplos:

- `README.md`
- `docs/*.md`

Esses arquivos orientam humanos e IA. Em geral, podem evoluir com mais liberdade, desde que nao contradigam os contratos estruturados.

### Contratos estruturados

Exemplos:

- `schemas/*`
- definicoes de archetypes
- manifests usados pelo CLI

Esses arquivos sao consumidos por automacao. Mudancas neles devem ser tratadas como mudancas de contrato.

### Templates oficiais

Exemplos:

- arquivos em `templates/*`

Esses arquivos afetam o resultado do scaffolding. Mesmo quando o formato de entrada nao muda, uma alteracao de template pode impactar todos os futuros repositorios consumidores.

### Exemplos de referencia

Exemplos:

- arquivos em `examples/*`

Esses arquivos ajudam a validar a intencao dos contratos e do scaffolding. Eles devem acompanhar mudancas relevantes nos artefatos que representam.

## Classificacao de Mudancas

Toda mudanca proposta deve ser classificada em uma destas categorias.

### 1. Editorial

Mudancas de texto que nao alteram contrato, comportamento esperado nem semantica de automacao.

Exemplos:

- correcao de redacao
- melhoria de explicacao
- organizacao de secoes

Impacto esperado:

- baixo

### 2. Aditiva Compativel

Mudancas que adicionam capacidade sem quebrar consumidores existentes.

Exemplos:

- novo archetype
- novo template opcional
- novo campo opcional em manifest
- novo exemplo de referencia

Impacto esperado:

- medio

### 3. Evolutiva com Impacto Comportamental

Mudancas que mantem compatibilidade formal, mas alteram comportamento padrao, experiencia de scaffolding ou interpretacao operacional.

Exemplos:

- mudanca no conteudo padrao de um template oficial
- alteracao do fluxo sugerido para um archetype existente
- inclusao de validacoes mais estritas sem quebrar entradas validas atuais

Impacto esperado:

- medio a alto

### 4. Breaking Change

Mudancas que removem, renomeiam ou alteram semantica de contratos consumidos por CLI, IA ou processos padronizados.

Exemplos:

- remocao de um archetype suportado
- renomeacao de caminhos esperados pelo CLI
- transformacao de campo opcional em obrigatorio
- alteracao de schema que invalida configuracoes antes aceitas
- mudanca semantica de um contrato sem mecanismo de transicao

Impacto esperado:

- alto

## Regras por Tipo de Mudanca

### Para mudancas editoriais

Deve existir:

- descricao clara da melhoria

### Para mudancas aditivas compativeis

Deve existir:

- descricao do novo comportamento
- justificativa arquitetural
- atualizacao da documentacao relevante
- exemplo quando aplicavel

### Para mudancas evolutivas com impacto comportamental

Deve existir:

- explicacao explicita do impacto
- justificativa para a mudanca
- atualizacao de documentacao e exemplos
- avaliacao de efeito sobre o CLI e sobre novos consumidores

### Para breaking changes

Deve existir:

- identificacao explicita de que a mudanca e breaking
- motivo da quebra
- estrategia de migracao
- atualizacao dos contratos afetados
- atualizacao de documentacao, exemplos e templates relacionados
- avaliacao de impacto no CLI e nos consumidores existentes

## Contrato de Compatibilidade

Os seguintes elementos devem ser tratados como superficie de contrato:

- nomes e localizacao de arquivos estruturados consumidos pelo CLI
- formato dos manifests e definicoes de archetype
- schemas de validacao
- semantica de campos consumidos por automacao
- convencoes publicadas como parte oficial da plataforma

Esses elementos nao devem ser alterados informalmente.

## Politica de Evolucao

A evolucao deste repositorio deve seguir a seguinte ordem de preferencia:

1. adicionar sem quebrar
2. marcar como obsoleto antes de remover
3. documentar migracao antes de exigir nova forma
4. atualizar exemplos junto com o contrato
5. remover apenas quando houver justificativa clara

## Deprecacao

Quando um contrato precisar ser substituido, o caminho preferido e:

1. marcar o artefato antigo como obsoleto
2. introduzir o substituto oficial
3. documentar a migracao esperada
4. remover apenas em uma mudanca futura explicitamente classificada como breaking

Isso reduz risco para o CLI, para a IA e para os times consumidores.

## Impacto Sobre o CLI

Toda mudanca em contratos estruturados deve responder explicitamente:

- o CLI precisa ser alterado para suportar esta mudanca
- a mudanca afeta scaffolding, validacao ou ambos
- existe compatibilidade com definicoes anteriores
- ha necessidade de migracao ou versionamento

Se a resposta for sim para qualquer uma dessas perguntas, a mudanca nao deve ser tratada como simples ajuste documental.

## Impacto Sobre IA

Mudancas neste repositorio tambem afetam o consumo por IA.

Em especial:

- nomes e estruturas precisam ser previsiveis
- conceitos equivalentes nao devem ser duplicados sem necessidade
- documentacao narrativa nao deve contradizer contratos estruturados
- exemplos devem refletir a forma recomendada mais atual

## Aprovacao

Enquanto nao houver um modelo organizacional mais formal, toda mudanca relevante deve ser avaliada pelos mantenedores deste repositorio com base em:

- clareza do problema resolvido
- aderencia ao proposito da plataforma
- impacto sobre consumidores humanos e automatizados
- compatibilidade
- custo de migracao, quando houver

## O Que Sempre Deve Acompanhar Uma Mudanca Relevante

Sempre que uma mudanca afetar contratos, templates ou comportamento esperado, ela deve vir acompanhada de:

- documentacao atualizada
- exemplos coerentes com o novo estado
- classificacao explicita do tipo de mudanca
- explicacao do impacto

## Regra Pratica

Se uma mudanca puder confundir um desenvolvedor, induzir erro em um agente de IA ou quebrar uma automacao do CLI, ela precisa ser tratada como mudanca de governanca, nao como simples ajuste de repositorio.
