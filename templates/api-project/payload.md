# API Project Payload

## Proposito

Este documento descreve os arquivos concretos que o CLI deve copiar ou materializar ao aplicar o template `api-project`.

Ele documenta a carga util do template sem competir com os arquivos reais que viverao em `files/`.

## Regra de Mapeamento

Os arquivos mantidos em `files/` devem ser interpretados como o projeto principal da API HTTP no repositorio gerado.

Em termos praticos:

- tudo o que estiver em `files/` deve ser aplicado no repositorio consumidor
- a estrutura relativa dentro de `files/` deve ser preservada
- o conteudo deve representar o projeto principal da API, e nao testes, solution ou containerizacao
- arquivos com sufixo `.tpl` devem ser renderizados e materializados sem o sufixo no destino
- arquivos sem `.tpl` devem ser copiados literalmente

## Tipos de Arquivo Esperados

Os tipos mais provaveis de artefato neste template sao:

- arquivo `.csproj` do projeto principal
- `Program.cs`
- estrutura inicial em `src/`
- arquivos de configuracao e bootstrap necessarios para a API iniciar

Esses artefatos devem ser suficientemente genericos para servir como base oficial de APIs HTTP em `.NET`.

## Placeholders

Arquivos em `files/` podem conter placeholders resolvidos pelo CLI a partir dos inputs do archetype.

Exemplos conceituais:

- `{{ serviceName }}`
- `{{ rootNamespace }}`
- `{{ targetFramework }}`

Regra importante:

- placeholders devem depender de inputs publicados pelo archetype
- o CLI deve ser a camada responsavel por resolver substituicoes
- nomes de placeholders devem permanecer previsiveis

Convencao inicial adotada:

- o caminho e o nome do projeto principal usam `{{ rootNamespace }}`

## O Que Pode Entrar Aqui

Pode entrar em `files/`:

- projeto principal da API
- bootstrap minimo da aplicacao HTTP
- estrutura base reutilizavel dentro de `src/`

## O Que Nao Deve Entrar Aqui

Nao deve entrar em `files/`:

- arquivo `.sln`
- projeto de testes
- Dockerfile
- pipeline de CI
- codigo fortemente acoplado a um dominio especifico

Se um artefato fizer sentido apenas por causa de testes, Docker ou da organizacao da solution, ele provavelmente pertence a outro template.

## Relacao com o CLI

O CLI deve tratar `files/` como fonte oficial do projeto principal da API.

Ao aplicar este template, o CLI deve conseguir:

- localizar os artefatos do template
- resolver placeholders de nome, namespace e framework
- materializar o projeto HTTP principal no caminho esperado

## Relacao com IA

Agentes de IA devem poder consultar este template para entender:

- como a plataforma espera que um projeto de API HTTP em `.NET` nasca
- quais artefatos pertencem ao projeto principal
- quais decisoes ainda dependem de templates posteriores

## Regra de Qualidade

Antes de adicionar um novo arquivo em `files/`, a pergunta correta e:

este artefato faz parte da base do projeto principal da API ou depende de outra responsabilidade?

Se a resposta depender da solution, dos testes, de Docker ou de um contexto de dominio especifico, ele provavelmente nao pertence a este template.
