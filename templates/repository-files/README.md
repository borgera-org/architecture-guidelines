# Repository Files Template

## Proposito

Este template define os arquivos basicos de raiz que devem existir em repositorios consumidores criados pela plataforma.

Ele existe para padronizar a camada mais transversal do repositorio: identidade inicial, higiene tecnica e arquivos-base que quase todo repositorio precisa ter desde o primeiro commit.

## Papel Deste Template

O papel deste template e materializar arquivos de nivel de repositorio, e nao arquivos especificos da aplicacao.

Em termos praticos, este template tende a ser responsavel por artefatos como:

- `README.md`
- `.gitignore`
- `.editorconfig`
- outros arquivos basicos de raiz, quando fizer sentido

## O Que Este Template Resolve

Este template ajuda a resolver problemas como:

- repositorios novos sem documentacao inicial
- inconsistencias em arquivos de configuracao basicos
- times iniciando projetos copiando repositorios antigos
- ausencia de uma base padronizada para CLI e IA

Ele cria uma base comum antes que templates mais especificos, como solution, projeto de API ou testes, sejam aplicados.

## O Que Este Template Nao Deve Resolver

Este template nao deve concentrar:

- estrutura interna da aplicacao
- arquivos especificos de .NET
- configuracoes exclusivas de um archetype muito particular
- regras arquiteturais de alto nivel

Essas responsabilidades pertencem a outros templates ou ao proprio archetype.

## Quando Usar

Este template deve ser usado quando um archetype precisar gerar um novo repositorio com arquivos basicos de raiz padronizados.

No estado atual da plataforma, ele faz sentido como parte do `templateSet` do archetype `api-dotnet`.

## Quando Nao Usar

Nao faz sentido usar este template isoladamente para:

- representar a estrutura completa de um repositorio
- substituir templates de stack ou linguagem
- modelar arquivos altamente especificos de um unico produto

Se um arquivo existe apenas por causa de uma necessidade local de um sistema, ele provavelmente nao deveria nascer aqui.

## Parametros Esperados

Este template deve consumir apenas parametros realmente necessarios para preencher arquivos basicos de raiz.

Exemplos provaveis:

- `repositoryName`
- `serviceName`

Dependendo da evolucao do repositorio, outros parametros podem surgir, mas a regra deve ser manter este template simples e transversal.

## Estrutura Esperada

A estrutura recomendada para este template e:

```text
templates/
  repository-files/
    README.md
    payload.md
    files/
```

O diretorio `files/` deve conter apenas os arquivos-base que precisam ser aplicados na raiz do repositorio consumidor.

O arquivo `payload.md` deve documentar as regras operacionais do conteudo em `files/` sem competir com os arquivos reais que serao materializados no repositorio destino.

## Relacao com o CLI

O CLI deve usar este template para:

- aplicar arquivos iniciais de raiz
- resolver placeholders com base nos inputs do archetype
- manter consistencia entre repositorios criados em momentos diferentes

O CLI nao deveria reconstruir esses arquivos manualmente se eles ja estiverem versionados aqui.

## Relacao com IA

Agentes de IA devem conseguir olhar para este template e entender:

- quais arquivos basicos todo repositorio oficial deve ter
- quais partes sao padronizadas pela plataforma
- quais artefatos ainda dependem de templates mais especificos

Isso reduz a chance de a IA improvisar arquivos de raiz diferentes do padrao oficial.

## Regra de Qualidade

Um arquivo deve entrar neste template apenas se:

- fizer sentido para mais de um repositorio consumidor
- for realmente de nivel de raiz
- nao depender fortemente de detalhes da aplicacao

Se um arquivo for especifico da stack .NET ou da estrutura interna de API, ele provavelmente deve viver em outro template.

## Proximo Passo

O proximo passo esperado para este template e continuar decidindo, arquivo por arquivo, quais artefatos basicos de raiz devem ser oficializados em `files/`.
