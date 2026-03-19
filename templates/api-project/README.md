# API Project Template

## Proposito

Este template define os artefatos base do projeto de API HTTP em um repositorio `.NET` criado pela plataforma.

Ele existe para padronizar o projeto principal da aplicacao, sem misturar responsabilidades de solution, testes ou containerizacao.

## Papel Deste Template

O papel deste template e materializar o projeto principal da API e sua estrutura inicial.

Em termos praticos, este template tende a ser responsavel por artefatos como:

- projeto `.csproj` da API
- `Program.cs`
- estrutura inicial dentro de `src/`
- arquivos base necessarios para a API compilar e iniciar

## O Que Este Template Resolve

Este template ajuda a resolver problemas como:

- criacao inconsistente do projeto principal da API
- ausencia de baseline tecnico para servicos HTTP em `.NET`
- duplicacao manual de estrutura entre times
- acoplamento da criacao do projeto diretamente ao codigo do CLI

Ele define a base do projeto HTTP que sera hospedado dentro da solution ja criada por `dotnet-solution`.

## O Que Este Template Nao Deve Resolver

Este template nao deve concentrar:

- o arquivo `.sln`
- projeto de testes
- artefatos de Docker
- pipeline de CI
- regras locais de dominio de um servico especifico

Essas responsabilidades pertencem a outros templates ou a evolucoes locais do repositorio consumidor.

## Quando Usar

Este template deve ser usado quando um archetype representar uma API HTTP em `.NET` e precisar gerar o projeto principal da aplicacao.

No estado atual da plataforma, ele faz sentido como parte do `templateSet` do archetype `api-dotnet`.

## Quando Nao Usar

Nao faz sentido usar este template para:

- workers sem interface HTTP
- bibliotecas compartilhadas
- frontends
- representar a estrutura completa do repositorio sozinho

Se o tipo de projeto nao for uma API HTTP, este nao e o template correto.

## Parametros Esperados

Este template tende a depender de parametros como:

- `serviceName`
- `rootNamespace`
- `targetFramework`

Dependendo da modelagem final, outros parametros podem aparecer, mas o template deve permanecer focado no projeto principal da API.

Convencao inicial adotada neste repositorio:

- o nome tecnico do projeto e o caminho inicial em `src/` usam `rootNamespace`
- o `TargetFramework` e herdado de `Directory.Build.props`

Motivo:

- `serviceName` representa melhor a identidade logica do servico
- `rootNamespace` representa melhor a identidade tecnica do projeto `.NET`
- o framework compartilhado deve ser centralizado no nivel da solution

## Estrutura Esperada

A estrutura inicial recomendada para este template e:

```text
templates/
  api-project/
    README.md
    payload.md
    files/
```

O diretorio `files/` deve conter apenas artefatos que fazem sentido para o projeto principal da API.

O arquivo `payload.md` deve documentar as regras operacionais do conteudo em `files/`.

## Relacao com o CLI

O CLI deve usar este template para:

- materializar o projeto principal da API
- resolver placeholders de nome e namespace
- preparar a base de codigo sobre a qual o time evoluira a aplicacao

O CLI nao deveria hardcodar a estrutura do projeto HTTP se ela ja estiver publicada neste template.

## Relacao com IA

Agentes de IA devem conseguir olhar para este template e entender:

- qual e a base oficial de uma API HTTP em `.NET`
- quais artefatos pertencem ao projeto principal
- quais elementos ainda dependem de templates complementares

## Regra de Qualidade

Um arquivo deve entrar neste template apenas se:

- fizer parte do projeto principal da API
- puder ser reutilizado por mais de um repositorio de API em `.NET`
- nao depender fortemente de testes, containerizacao ou CI

Se um artefato existir apenas por causa de testes, Docker ou de um dominio especifico, ele provavelmente deve ficar em outro lugar.

## Proximo Passo

O proximo passo esperado para este template e continuar decidindo, arquivo por arquivo, quais artefatos devem compor a base oficial do projeto de API.
