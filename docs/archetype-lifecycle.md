# Archetype Lifecycle

## Proposito

Este documento define o ciclo de vida oficial dos archetypes publicados neste repositorio.

Ele existe para evitar que estados como `draft`, `active` e `deprecated` sejam usados apenas como rotulo narrativo.

No estado desejado da plataforma, o estado de um archetype deve comunicar maturidade contratual, nivel de recomendacao e expectativa de estabilidade para humanos, IA e CLI.

## Modelo de Estados

O modelo atual de estados e:

- `draft`
- `active`
- `deprecated`

## Significado de Cada Estado

### `draft`

Use `draft` quando o archetype ja existir como proposta executavel, mas ainda estiver amadurecendo.

Nesse estado:

- o contrato ja pode existir em `definition.yaml`
- templates, schemas, examples e validadores ja podem estar presentes
- o archetype ainda nao deve ser tratado como baseline oficialmente estavel
- mudancas podem acontecer com mais frequencia, desde que governadas

### `active`

Use `active` quando o archetype ja tiver contrato suficientemente completo, validado e recomendado como caminho oficial da plataforma para aquele tipo de repositorio.

Nesse estado:

- humanos devem tratá-lo como o caminho preferencial
- IA deve tratá-lo como a recomendacao oficial
- o CLI pode consumi-lo como contrato estavel para o baseline correspondente

### `deprecated`

Use `deprecated` quando o archetype ainda puder existir por compatibilidade ou consulta historica, mas nao for mais o caminho recomendado.

Nesse estado:

- o archetype nao deve ser usado para novos repositorios sem excecao explicita
- deve existir justificativa clara para a obsolescencia
- deve existir substituto ou estrategia de migracao, quando aplicavel

## Criterios Minimos para Promocao de `draft` para `active`

Um archetype so deve ser promovido para `active` quando todos os criterios abaixo estiverem satisfeitos.

### 1. Contrato estrutural completo

Deve existir:

- `definition.yaml` valido contra o schema oficial
- `README.md` explicativo do proprio archetype
- templates referenciados presentes no repositorio
- `postProcessing` declarado quando o resultado final depender dele

### 2. Semantica contratual publicada

Os pontos de comportamento do archetype nao podem depender de interpretacao implícita.

Isso significa que:

- `inputs` precisam estar publicados
- `when` precisa estar dentro do subset oficialmente suportado
- constraints e outputs precisam estar descritos
- orientacao para humanos, IA e CLI precisa estar publicada

### 3. Cobertura de examples suficiente

Deve existir pelo menos:

- um example oficial para o caminho padrao do archetype
- coverage para cada variacao condicional publicada que altere materialmente o resultado

Exemplo:

- se o archetype publica `includeTests` e `includeDocker`, os examples oficiais devem provar essas variacoes quando elas alterarem templates, pos-processamento ou estrutura final

### 4. Validacao automatizada aderente

Deve existir validacao automatizada que comprove pelo menos:

- validade estrutural do archetype
- validade dos manifests de example
- aderencia entre examples materializados e templates aplicados
- aderencia do efeito de `postProcessing` ao resultado final esperado

Essas validacoes devem estar integradas ao fluxo normal do repositorio, preferencialmente em CI.

### 5. Ausencia de lacuna contratual critica

O archetype nao deve exigir que o CLI adivinhe comportamento essencial fora do que ja foi publicado neste repositorio.

Em termos praticos:

- o CLI pode implementar o contrato
- o CLI nao deve precisar inventar regras essenciais para completar o baseline

### 6. Aprovacao explicita dos mantenedores

A promocao para `active` deve ser uma decisao explicita.

Isso exige:

- avaliacao registrada em PR ou documento equivalente
- conclusao de que os criterios acima foram satisfeitos
- atualizacao do `status` e de `lifecycle.currentStateReason`

## O Que Nao E Obrigatorio para `active`

Para manter o criterio pragmático, nao e obrigatorio que:

- o archetype ja tenha sido usado em todos os tipos de projeto possiveis
- exista uma implementacao final e distribuida do produto CLI
- todos os archetypes futuros da plataforma ja estejam definidos

O que importa e a maturidade do contrato publicado para aquele archetype especifico.

## Criterios para Permanecer em `draft`

Um archetype deve permanecer em `draft` quando pelo menos um destes pontos ainda for verdadeiro:

- falta contrato estrutural relevante
- falta example oficial suficiente
- falta validacao automatizada relevante
- ainda existe lacuna contratual que obrigaria o CLI a adivinhar comportamento essencial
- ainda nao houve decisao explicita de promocao

## Criterios para `deprecated`

Um archetype pode ser marcado como `deprecated` quando:

- existir substituto oficial mais adequado
- o caminho atual nao for mais recomendado para novos repositorios
- houver necessidade de transicao controlada sem remocao imediata

Ao marcar como `deprecated`, deve existir:

- justificativa clara
- orientacao de migracao ou substituicao, quando aplicavel
- atualizacao dos documentos que o referenciam como padrao oficial

## Evidencia Minima Esperada em Uma Promocao

Uma PR de promocao para `active` deve deixar claro:

- qual archetype esta sendo promovido
- como cada criterio minimo foi satisfeito
- quais validacoes foram executadas
- qual o impacto para humanos, IA e CLI

## Regra Pratica

`active` nao significa “perfeito”.

`active` significa que o archetype ja e um contrato suficientemente completo, validado e governado para ser tratado como caminho oficial da plataforma.
