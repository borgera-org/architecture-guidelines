# Examples

## Proposito

Este diretorio concentra exemplos de saida esperada para archetypes e templates publicados neste repositorio.

Ele existe para mostrar, de forma concreta, como os contratos da plataforma devem se materializar em um repositorio consumidor.

## Papel dos Examples

Os examples nao sao a fonte primaria de verdade da plataforma.

A fonte primaria continua sendo:

- archetypes
- templates
- schemas
- contrato do CLI

Os examples existem para complementar esses artefatos com uma visao concreta do resultado esperado.

## O Que Este Diretorio Resolve

Este diretorio ajuda a resolver problemas como:

- dificuldade de visualizar o resultado do scaffolding sem executar o CLI
- ambiguidade sobre como os templates se combinam
- dificuldade para revisar se um archetype produz a estrutura desejada
- ausencia de referencia concreta para IA e desenvolvedores

## Relacao com o CLI

Os examples nao devem ser tratados como payload de scaffolding.

Eles servem para:

- documentar o resultado esperado
- apoiar validacao manual
- apoiar validacao automatizada futura
- facilitar testes de aderencia entre contrato e saida materializada

## Relacao com IA

Agentes de IA podem usar este diretorio para:

- entender o formato final esperado de um repositorio consumidor
- comparar sugestoes com um baseline concreto
- detectar diferencas entre contrato e resultado esperado

## Estrutura Esperada

A estrutura inicial recomendada e:

```text
examples/
  README.md
  <archetype-id>/
    README.md
    <example-name>/
```

Onde:

- `<archetype-id>/README.md`
  Explica quais cenarios de exemplo existem para aquele archetype.
- `<example-name>/`
  Contem uma representacao concreta do resultado esperado para um cenario especifico.

## O Que Pode Existir Aqui

Pode existir neste diretorio:

- snapshots de estrutura esperada
- exemplos minimos de saida
- cenarios de referencia para archetypes
- artefatos usados para comparar contrato e materializacao

## O Que Nao Deve Existir Aqui

Nao deve existir neste diretorio:

- templates oficiais
- contratos estruturados primarios
- documentacao que substitua o archetype
- variacoes arbitrarias sem valor de referencia

Se um conteudo e normativo, ele provavelmente pertence a `archetypes/`, `templates/` ou `schemas/`, nao a `examples/`.

## Regra de Qualidade

Um example so deve ser criado quando responder claramente:

- qual archetype ele representa
- qual cenario ele demonstra
- por que esse cenario merece existir como referencia

Se um example nao ajuda a validar ou explicar um contrato da plataforma, ele provavelmente nao precisa existir.

## Proximo Passo

O proximo passo esperado neste diretorio e criar o primeiro conjunto de examples para o archetype `api-dotnet`.
