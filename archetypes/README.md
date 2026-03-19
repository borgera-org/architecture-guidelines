# Archetypes

## Proposito

Este diretorio concentra os archetypes oficiais suportados pela plataforma.

Um archetype representa um tipo de repositorio que pode ser criado e evoluido de forma padronizada pelo CLI interno.

Ele nao e apenas um conjunto de arquivos. Ele e uma definicao declarativa de intencao arquitetural.

## O Que E Um Archetype

Um archetype descreve:

- que tipo de repositorio esta sendo criado
- qual problema esse tipo de repositorio resolve
- quais entradas o CLI precisa receber
- quais templates devem ser aplicados
- quais restricoes e convencoes precisam ser respeitadas
- qual estrutura final e esperada

Em termos simples:

- template e material de construcao
- archetype e a planta

Sem archetypes, o CLI fica preso a copiar arquivos.
Com archetypes, o CLI consegue interpretar intencao, validar entradas e aplicar o conjunto correto de templates e regras.

## Por Que Este Diretorio Existe

Este diretorio existe para evitar tres problemas comuns:

- scaffolding baseado apenas em copia de pastas
- padroes tecnicos escondidos em scripts ou codigo do CLI
- criacao de repositorios sem contrato arquitetural explicito

Ao colocar archetypes neste repositorio, a plataforma ganha:

- padronizacao reutilizavel
- clareza para desenvolvedores
- contexto estavel para IA
- menor acoplamento entre regra e implementacao do CLI

## Relacao Entre Archetypes, Templates, Schemas e Examples

Cada tipo de artefato tem um papel diferente:

- `archetypes/`
  Define o tipo de repositorio, suas entradas e seu comportamento esperado.
- `templates/`
  Contem os arquivos e estruturas reutilizados durante o scaffolding.
- `schemas/`
  Validam a forma dos contratos e das entradas.
- `examples/`
  Mostram o resultado esperado para um archetype ou para um conjunto de templates.

O archetype fica no centro dessa relacao.

Ele aponta para templates, e validado por schemas e deve ser demonstrado por exemplos.

## Estrutura Esperada

A estrutura recomendada para cada archetype e:

```text
archetypes/
  README.md
  <archetype-id>/
    definition.yaml
    README.md
```

Onde:

- `<archetype-id>/definition.yaml`
  E o contrato estruturado principal do archetype.
- `<archetype-id>/README.md`
  Explica o uso humano do archetype, quando aplica-lo e quais decisoes ele incorpora.

Outros arquivos podem existir no futuro, mas a base deve permanecer pequena e previsivel.

## Convencao de Identidade

Cada archetype deve possuir um identificador estavel.

Recomendacoes para o identificador:

- usar minusculas
- usar `kebab-case`
- representar claramente o tipo de repositorio
- evitar nomes vagos como `default`, `service` ou `standard`

Exemplos melhores:

- `api-dotnet`
- `worker-dotnet`
- `frontend-react`
- `library-dotnet`

## Campos Minimos Esperados

Embora o schema formal ainda sera criado, um archetype deve nascer com pelo menos estes elementos conceituais:

- `id`
  Identificador estavel do archetype.
- `name`
  Nome legivel para humanos.
- `description`
  Explicacao curta do caso de uso.
- `version`
  Versao do contrato do archetype.
- `status`
  Estado atual, por exemplo `draft`, `active` ou `deprecated`.
- `inputs`
  Lista de entradas esperadas pelo CLI.
- `templateSet` ou equivalente
  Referencia aos templates que devem ser aplicados, inclusive quando a selecao depender de condicoes.
- `constraints`
  Regras e limitacoes que o consumidor precisa respeitar.

Esses campos ainda serao formalizados por schema. Aqui eles aparecem como contrato conceitual minimo.

## O Que Um Archetype Deve Decidir

Um archetype deve decidir apenas o que for relevante para o tipo de repositorio.

Exemplos de decisoes adequadas:

- stack base
- estrutura inicial do repositorio
- componentes obrigatorios
- convencoes transversais
- integracoes padrao esperadas

Exemplos de decisoes inadequadas:

- detalhes altamente especificos de um time isolado
- customizacoes que so servem para um unico produto
- preferencias de implementacao sem impacto arquitetural

Se uma variacao nao altera o contrato do tipo de repositorio, provavelmente ela nao deveria gerar um novo archetype.

## O Que O CLI Deve Poder Fazer com um Archetype

Ao consumir um archetype, o CLI deve conseguir:

- descobrir o archetype pelo identificador
- validar sua definicao
- solicitar ou receber as entradas necessarias
- selecionar os templates corretos
- aplicar convencoes e restricoes publicadas
- gerar a estrutura inicial prevista

Isso e o que diferencia um archetype de uma simples pasta de exemplo.

## O Que A IA Deve Poder Fazer com um Archetype

Ao consumir um archetype, um agente de IA deve conseguir:

- entender a intencao do tipo de repositorio
- sugerir o archetype correto para um contexto
- validar se uma estrutura proposta esta aderente
- explicar os trade-offs incorporados pelo padrao

Para isso, nomes, descricoes e estrutura precisam ser previsiveis.

## Regra de Qualidade

Um novo archetype so deve ser criado quando responder claramente:

- qual tipo de repositorio ele representa
- qual necessidade organizacional ele cobre
- por que um archetype existente nao resolve o caso
- quais templates e regras ele precisa acionar

Se essas respostas nao estiverem claras, o archetype provavelmente esta sendo criado cedo demais.

## Proximo Passo

O proximo artefato esperado neste diretorio e o primeiro archetype oficial, com seu `definition.yaml` e sua explicacao de uso.
