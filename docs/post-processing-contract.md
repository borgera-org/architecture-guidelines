# Post-Processing Contract

## Proposito

Este documento define o contrato de pos-processamento da plataforma.

Ele existe para tornar explicito um ponto que ja apareceu na pratica: copiar e renderizar templates nao e suficiente para produzir o estado final esperado de um repositorio consumidor.

Depois da materializacao dos arquivos, o CLI ainda pode precisar executar passos estruturais adicionais para que o resultado final fique aderente ao contrato do archetype.

## Problema Que Este Contrato Resolve

Sem um contrato explicito de pos-processamento, o CLI tende a:

- embutir comportamento importante em codigo hardcoded
- executar passos relevantes sem visibilidade para humanos e IA
- dificultar validacao automatizada da saida esperada
- criar dependencia excessiva do historico de implementacao do CLI

Este documento existe para evitar isso.

## O Que E Pos-processamento

Pos-processamento e qualquer acao executada pelo CLI depois que os templates ja foram:

- selecionados
- renderizados
- materializados no repositorio destino

Em termos simples:

- templates produzem arquivos
- pos-processamento conecta, ajusta ou completa o estado final esperado

## Exemplo Real Ja Existente

No baseline atual do archetype `api-dotnet`, o exemplo mais claro de pos-processamento e:

- adicionar o projeto principal da API a solution
- adicionar o projeto de testes a solution, quando `includeTests == true`

O template `dotnet-solution` fornece uma solution vazia.

Os templates `api-project` e `test-project` fornecem projetos.

O estado final correto depende de o CLI conectar essas partes.

## Principios do Contrato

O pos-processamento da plataforma deve seguir estes principios:

- explicito antes de implicito
- declarativo antes de hardcoded
- deterministico antes de contextual
- local ao repositorio antes de depender de servicos externos
- validavel antes de ficar escondido na implementacao

## O Que Deve Ser Considerado Pos-processamento

Em geral, entram nesta categoria:

- ajustes em solution
- conexoes entre artefatos ja materializados
- comandos estruturais necessarios para concluir o baseline do repositorio

## O Que Nao Deve Ser Considerado Pos-processamento Basico

Em geral, nao devem entrar aqui, pelo menos no baseline atual:

- criacao automatica de remoto Git
- push para servidor remoto
- publicacao de pacote
- deploy
- provisionamento de infraestrutura
- chamadas para servicos externos nao essenciais ao estado local do repositorio

Esses pontos pertencem a outras camadas da plataforma.

## Momento de Execucao

A ordem correta no estado atual da plataforma e:

1. resolver inputs
2. selecionar templates
3. renderizar e materializar arquivos
4. executar pos-processamento
5. executar validacoes

Pos-processamento nao deve acontecer antes da materializacao dos arquivos de que ele depende.

## Relacao com Archetypes

O archetype deve ser a fonte de verdade para o comportamento esperado do repositorio final.

Por isso, a direcao correta da plataforma e:

- archetypes devem declarar quais pos-processamentos sao necessarios
- o CLI deve executar esses pos-processamentos
- examples e manifests devem refletir o resultado final apos essas acoes

No baseline atual, essa relacao ja foi formalizada no archetype `api-dotnet`
e passou a ser validada por schema como parte do contrato do archetype.

## Estado Atual do Contrato

No estado atual da plataforma:

- `postProcessing` ja faz parte do contrato validado de archetypes
- o primeiro tipo oficial suportado e `solution-add-project`
- a acao pode ser condicional com `when`, assim como `templateSet`
- examples registram os passos executados e o resultado final esperado

## Tipo de Acao Ja Identificado

O primeiro tipo de pos-processamento que ja existe de fato no baseline atual e:

- `solution-add-project`

Semantica:

- uma solution existente deve passar a referenciar um projeto existente

## Contrato Minimo de `solution-add-project`

No estado atual, uma acao `solution-add-project` precisa responder pelo menos:

- em que condicao ela deve rodar, quando for condicional
- qual solution sera alterada
- qual projeto sera adicionado

Exemplo conceitual:

- solution: `Billing.Api.sln`
- project: `src/Billing.Api/Billing.Api.csproj`
- when: `includeTests == true`, quando o passo depender de input

## Requisitos de Execucao

Uma acao de pos-processamento deve ser executada de forma segura.

No baseline atual, isso implica:

- falhar se a solution nao existir
- falhar se o projeto nao existir
- falhar se o tipo de acao nao for suportado
- evitar assumir caminhos que nao estejam publicados no contrato

## Idempotencia

Sempre que possivel, o pos-processamento deve ser idempotente.

No caso de `solution-add-project`, isso significa que o CLI deve evitar adicionar a mesma referencia duas vezes.

Essa propriedade e importante porque:

- reduz efeitos colaterais em reexecucao
- facilita automacao
- melhora confiabilidade do fluxo

## Relacao com Examples

Examples devem representar o estado final apos o pos-processamento.

Isso significa que:

- o snapshot materializado deve mostrar a solution ja ajustada
- o manifest deve registrar os passos de pos-processamento esperados
- o validador deve conseguir verificar pelo menos o efeito estrutural dessas acoes

## Relacao com Validacao

O contrato de pos-processamento so e util se puder ser validado.

No baseline atual, a validacao ja consegue verificar:

- se os caminhos declarados existem
- se a solution final referencia os projetos esperados

No futuro, a validacao deve evoluir para comparar o contrato declarado no archetype com o estado final do snapshot.

## Direcao de Evolucao

A direcao recomendada para a plataforma e:

1. ampliar a lista oficial de tipos de acao suportados
2. alinhar validacao de archetypes, examples e CI com o contrato publicado
3. definir como novas acoes serao versionadas sem quebrar consumidores
4. manter o CLI interpretando esse contrato de forma declarativa

## O Que Ainda Nao Esta Decidido

Os seguintes pontos ainda estao em aberto:

- a lista oficial de tipos de acao suportados
- o limite entre pos-processamento generico e logica especifica do CLI
- como versionar novas acoes sem quebrar consumidores
- se o subset atual de `when` precisara ser ampliado no futuro

## Regra Pratica

Se o estado final correto de um repositorio depender de uma acao executada depois dos templates, essa acao nao deve ficar apenas no codigo do CLI.

Ela deve aparecer explicitamente no contrato da plataforma.
