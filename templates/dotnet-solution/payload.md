# Dotnet Solution Payload

## Proposito

Este documento descreve os arquivos concretos que o CLI deve copiar ou materializar ao aplicar o template `dotnet-solution`.

Ele documenta a carga util do template sem competir com os arquivos reais que viverao em `files/`.

## Regra de Mapeamento

Os arquivos mantidos em `files/` devem ser interpretados como a base tecnica de uma solution `.NET` no repositorio gerado.

Em termos praticos:

- tudo o que estiver em `files/` deve ser aplicado no repositorio consumidor
- a estrutura relativa dentro de `files/` deve ser preservada
- o conteudo deve representar a camada de solution, e nao um projeto de aplicacao especifico
- arquivos com sufixo `.tpl` devem ser renderizados e materializados sem o sufixo no destino
- arquivos sem `.tpl` devem ser copiados literalmente

## Tipos de Arquivo Esperados

Os tipos mais provaveis de artefato neste template sao:

- arquivo `.sln`
- arquivos de configuracao compartilhados pela stack `.NET`
- estrutura base de diretorios como `src/` e `tests/`, quando fizer sentido materializa-la aqui

Esses artefatos devem ser suficientemente genericos para servir como base de mais de um repositorio `.NET`.

## Placeholders

Arquivos em `files/` podem conter placeholders resolvidos pelo CLI a partir dos inputs do archetype.

Exemplos conceituais:

- `{{ solutionName }}`
- `{{ rootNamespace }}`
- `{{ targetFramework }}`

Regra importante:

- placeholders devem depender de inputs publicados pelo archetype
- o CLI deve ser a camada responsavel por resolver substituicoes
- nomes de placeholders devem permanecer previsiveis

## O Que Pode Entrar Aqui

Pode entrar em `files/`:

- arquivo de solution
- configuracoes compartilhadas pela solution
- estrutura base reutilizavel para repositorios `.NET`

## O Que Nao Deve Entrar Aqui

Nao deve entrar em `files/`:

- codigo da API HTTP
- codigo de testes
- Dockerfile ou artefatos de containerizacao
- pipeline de CI
- configuracoes especificas de um unico servico

Se um artefato so faz sentido para uma API ou para testes, ele provavelmente pertence a outro template.

## Relacao com o CLI

O CLI deve tratar `files/` como fonte oficial para a base de solution `.NET`.

Ao aplicar este template, o CLI deve conseguir:

- localizar os artefatos do template
- resolver placeholders de solution e namespace
- materializar a base tecnica do repositorio antes de aplicar templates mais especificos

## Pos-processamento Esperado

Este template, isoladamente, fornece uma solution vazia.

Quando outros templates materializarem projetos reais, o CLI devera executar os passos necessarios para incorporar esses projetos a solution, em vez de depender apenas de copia de arquivos.

## Relacao com IA

Agentes de IA devem poder consultar este template para entender:

- como a plataforma espera que uma solution `.NET` nasca
- quais artefatos pertencem ao nivel da solution
- quais decisoes ainda dependem de templates posteriores

## Regra de Qualidade

Antes de adicionar um novo arquivo em `files/`, a pergunta correta e:

este artefato faz parte da base compartilhada de uma solution `.NET` ou depende de um tipo especifico de projeto?

Se a resposta depender da implementacao da API, dos testes ou do pipeline, ele provavelmente nao pertence a este template.
