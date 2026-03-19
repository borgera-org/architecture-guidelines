# Test Project Payload

## Proposito

Este documento descreve os arquivos concretos que o CLI deve copiar ou materializar ao aplicar o template `test-project`.

Ele documenta a carga util do template sem competir com os arquivos reais que viverao em `files/`.

## Regra de Mapeamento

Os arquivos mantidos em `files/` devem ser interpretados como o projeto inicial de testes no repositorio gerado.

Em termos praticos:

- tudo o que estiver em `files/` deve ser aplicado no repositorio consumidor
- a estrutura relativa dentro de `files/` deve ser preservada
- o conteudo deve representar o baseline de testes, e nao a API principal, a solution ou a infraestrutura
- arquivos com sufixo `.tpl` devem ser renderizados e materializados sem o sufixo no destino
- arquivos sem `.tpl` devem ser copiados literalmente

## Tipos de Arquivo Esperados

Os tipos mais provaveis de artefato neste template sao:

- arquivo `.csproj` de testes
- estrutura inicial em `tests/`
- teste basico de smoke ou sanidade
- bootstrap minimo para execucao de testes automatizados

Esses artefatos devem ser suficientemente genericos para servir como base oficial de testes para APIs em `.NET`.

## Placeholders

Arquivos em `files/` podem conter placeholders resolvidos pelo CLI a partir dos inputs do archetype.

Exemplos conceituais:

- `{{ rootNamespace }}`
- `{{ targetFramework }}`

Regra importante:

- placeholders devem depender de inputs publicados pelo archetype
- o CLI deve ser a camada responsavel por resolver substituicoes
- nomes de placeholders devem permanecer previsiveis

Convencao inicial adotada:

- o caminho e o nome do projeto de testes usam `{{ rootNamespace }}.Tests`
- o projeto de testes referencia `src/{{ rootNamespace }}/{{ rootNamespace }}.csproj`
- o framework inicial de testes adotado e `xUnit`
- o teste inicial valida `/health` com `WebApplicationFactory`

## O Que Pode Entrar Aqui

Pode entrar em `files/`:

- projeto de testes
- estrutura base reutilizavel dentro de `tests/`
- teste inicial de sanidade

## O Que Nao Deve Entrar Aqui

Nao deve entrar em `files/`:

- arquivo `.sln`
- projeto principal da API
- Dockerfile
- pipeline de CI
- cenarios altamente especificos de negocio

Se um artefato fizer sentido apenas para um contexto de dominio particular, ele provavelmente nao pertence a este template.

## Relacao com o CLI

O CLI deve tratar `files/` como fonte oficial do projeto inicial de testes.

Ao aplicar este template, o CLI deve conseguir:

- localizar os artefatos do template
- resolver placeholders de namespace
- materializar o projeto de testes no caminho esperado

## Relacao com IA

Agentes de IA devem poder consultar este template para entender:

- como a plataforma espera que a base inicial de testes nasca
- quais artefatos pertencem ao projeto de testes
- onde termina o baseline de testes e onde comecam cenarios locais

## Regra de Qualidade

Antes de adicionar um novo arquivo em `files/`, a pergunta correta e:

este artefato faz parte do baseline do projeto de testes ou depende de um cenario especifico do sistema?

Se a resposta depender da API principal, da solution, de infraestrutura ou de regras de dominio especificas, ele provavelmente nao pertence a este template.
