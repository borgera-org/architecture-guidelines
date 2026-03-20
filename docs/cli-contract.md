# CLI Contract

## Proposito

Este documento define o contrato operacional entre este repositorio e o CLI interno de scaffolding.

Ele existe porque este repositorio nao e apenas uma base de documentacao. Ele tambem e fonte de verdade para artefatos, regras e comportamentos que o CLI deve interpretar de forma previsivel.

Sem este contrato, o CLI tenderia a depender de conhecimento implicito, comportamento hardcoded e decisoes nao publicadas.

## O Que Este Contrato Resolve

Este contrato existe para responder perguntas como:

- como o CLI descobre um archetype
- como o CLI valida um contrato
- como o CLI seleciona templates
- como o CLI trata arquivos `.tpl`
- quando o CLI deve copiar literalmente um arquivo
- quando o CLI precisa executar pos-processamento
- como o CLI deve falhar em caso de inconsistencias

## Papel do CLI

O CLI nao deve ser a fonte primaria das regras arquiteturais.

O papel do CLI e:

- ler os contratos publicados neste repositorio
- validar entradas e estruturas
- materializar templates
- executar os passos operacionais declarados no contrato
- gerar repositorios consumidores aderentes ao padrao oficial

Em termos simples:

- este repositorio define
- o CLI interpreta e executa

## Fluxo Esperado

O fluxo minimo esperado para o CLI e:

1. localizar o archetype solicitado
2. validar sua definicao estrutural
3. resolver inputs obrigatorios e valores padrao
4. avaliar quais templates devem ser aplicados
5. materializar arquivos e diretorios
6. executar pos-processamento quando necessario
7. retornar um repositorio aderente ao contrato publicado

## Descoberta de Archetypes

O CLI deve descobrir archetypes no diretorio `archetypes/`.

Cada archetype suportado deve possuir pelo menos:

- um diretorio proprio
- um arquivo `definition.yaml`
- um `README.md` explicativo

O identificador do archetype deve ser tratado como chave estavel de descoberta.

## Validacao de Contrato

Antes de materializar um repositorio, o CLI deve validar a estrutura do archetype consumido.

No estado atual da plataforma, isso significa validar o objeto carregado de `definition.yaml` contra [archetype.schema.json](c:/Users/igors/source/repos/architecture-guidelines/schemas/archetype.schema.json).

O CLI nao deve assumir campos opcionais ou formatos que nao estejam publicados no schema.

## Resolucao de Inputs

Ao consumir um archetype, o CLI deve:

- exigir inputs marcados como obrigatorios
- aplicar valores `default` quando publicados
- rejeitar valores claramente invalidos para o contrato esperado

O CLI nao deve introduzir inputs ocultos sem contrato publicado neste repositorio.

## Selecao de Templates

O CLI deve ler `templateSet` como a fonte oficial para selecao de templates.

No estado atual da plataforma, `templateSet.templates` pode conter:

- entradas simples com `id`
- entradas condicionais com `id` e `when`

Exemplo conceitual:

- `repository-files`
- `test-project` quando `includeTests == true`

## Semantica Atual de `when`

No estado atual da plataforma, a linguagem de condicao deve ser tratada como deliberadamente pequena.

O contrato minimo que o CLI deve suportar agora e:

- comparacao booleana simples no formato `<booleanInput> == true|false`
- uso apenas de inputs booleanos declarados no proprio archetype
- falha explicita quando a expressao nao obedecer esse subset

O CLI nao deve inventar uma linguagem mais ampla sem que isso seja formalizado neste repositorio.

## Materializacao de Payload

O CLI deve tratar `files/` como a fonte de payload de cada template.

Regras obrigatorias:

- a estrutura relativa dentro de `files/` deve ser preservada
- diretorios com placeholders devem ser renderizados
- nomes de arquivo com placeholders devem ser renderizados
- conteudo de arquivos `.tpl` deve ser renderizado
- o sufixo `.tpl` deve ser removido no destino
- arquivos sem `.tpl` devem ser copiados literalmente

Exemplos:

- `Dockerfile.tpl` -> `Dockerfile`
- `README.md.tpl` -> `README.md`
- `.gitignore` -> `.gitignore`
- `src/{{ rootNamespace }}/{{ rootNamespace }}.csproj.tpl` -> `src/My.Api/My.Api.csproj`

## Render de Placeholders

O CLI deve renderizar placeholders apenas a partir de inputs e valores resolvidos do contrato atual.

Regras obrigatorias:

- placeholders em caminho devem ser resolvidos antes da escrita no destino
- placeholders em conteudo devem ser resolvidos antes da gravacao final
- placeholders nao resolvidos devem gerar erro

O CLI nao deve ignorar placeholders restantes silenciosamente.

## Pos-processamento

Nem todo comportamento necessario pode ser resolvido apenas por copia de arquivos.

No estado atual da plataforma, o CLI deve ler o bloco `postProcessing` do
archetype e executar pelo menos o tipo de acao ja suportado hoje:

- `solution-add-project`

Esse ponto e importante:

- o template `dotnet-solution` fornece uma solution vazia
- os templates `api-project` e `test-project` fornecem projetos
- o CLI deve conectar essas partes no resultado final

## Ordem de Aplicacao

A ordem de aplicacao dos templates importa.

No estado atual, a ordem recomendada e:

1. `repository-files`
2. `dotnet-solution`
3. `api-project`
4. `test-project`, quando aplicavel
5. `docker-files`, quando aplicavel
6. pos-processamento da solution

O CLI nao deve aplicar templates em ordem arbitraria quando isso puder alterar o resultado final.

## Arquivos Que Nao Sao Payload

O CLI nao deve materializar como payload:

- `README.md` de documentacao interna do template
- `payload.md`
- outros arquivos explicativos fora de `files/`

Esses arquivos existem para humanos e IA, nao para o repositorio consumidor final.

## Erros Que Devem Interromper a Execucao

O CLI deve falhar explicitamente quando encontrar:

- archetype inexistente
- `definition.yaml` invalido
- template referenciado e nao encontrado
- condicao `when` nao suportada
- placeholder nao resolvido
- tentativa de pos-processamento sobre artefato inexistente

Falhas de contrato devem interromper a execucao. O CLI nao deve tentar adivinhar comportamento em silencio.

## O Que Este Contrato Nao Define

Este contrato nao define:

- experiencia de interface do CLI
- formato do comando final usado pelos times
- estrategia de distribuicao do CLI
- detalhes de autenticacao ou integracao com provedores externos

Esses pontos pertencem a implementacao do produto CLI, nao ao contrato arquitetural deste repositorio.

## Estado Atual

Este contrato ja e suficiente para orientar e sustentar uma primeira implementacao funcional do CLI.

No estado atual, essa primeira implementacao de referencia ja existe em
[cli/](c:/Users/igors/source/repos/architecture-guidelines/cli/README.md) e e
exercitada pelos manifests oficiais em `examples/`.

Mesmo assim, ele ainda pode evoluir em pontos como:

- validacao automatizada de examples
- versionamento mais explicito de contratos e templates
- ampliacao do catalogo de acoes de pos-processamento
- ampliacao controlada da linguagem de `when`, se isso se mostrar necessario
- distribuicao e experiencia final de uso do produto CLI

## Regra Pratica

Se o CLI precisar tomar uma decisao relevante e essa decisao nao estiver publicada neste repositorio, existe uma lacuna no contrato e ela deve ser tratada aqui antes de virar regra hardcoded.
