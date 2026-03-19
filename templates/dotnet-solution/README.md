# Dotnet Solution Template

## Proposito

Este template define os artefatos base relacionados a uma solution .NET em repositorios consumidores criados pela plataforma.

Ele existe para padronizar a espinha dorsal tecnica de repositorios `.NET`, sem ainda entrar no detalhe de um projeto especifico de API, testes ou outros componentes especializados.

## Papel Deste Template

O papel deste template e materializar a camada de solution e organizacao tecnica inicial para repositorios `.NET`.

Em termos praticos, este template tende a ser responsavel por artefatos como:

- arquivo de solution
- estrutura inicial de diretorios associada a solution
- arquivos base de configuracao compartilhados pela stack `.NET`

## O Que Este Template Resolve

Este template ajuda a resolver problemas como:

- solutions nomeadas de formas inconsistentes
- ausencia de uma espinha dorsal previsivel para repositorios `.NET`
- duplicacao manual de estrutura base entre times
- acoplamento de regras de solution diretamente ao CLI

Ele cria a base estrutural sobre a qual outros templates, como `api-project` e `test-project`, poderao atuar.

## O Que Este Template Nao Deve Resolver

Este template nao deve concentrar:

- implementacao da API
- codigo de testes
- regras especificas de containerizacao
- configuracoes exclusivas de CI
- detalhes de dominio de um produto

Essas responsabilidades pertencem a templates mais especificos.

## Quando Usar

Este template deve ser usado quando um archetype representar um repositorio `.NET` que precise nascer com solution explicita e estrutura base previsivel.

No estado atual da plataforma, ele faz sentido como parte do `templateSet` do archetype `api-dotnet`.

## Quando Nao Usar

Nao faz sentido usar este template para:

- repositorios que nao usam `.NET`
- repositorios sem necessidade de solution
- representar sozinho a estrutura completa de uma API

Se a necessidade principal for gerar o codigo da API, este template sozinho nao e suficiente.

## Parametros Esperados

Este template tende a depender de parametros como:

- `solutionName`
- `rootNamespace`
- `targetFramework`

Nem todo parametro precisa ser usado diretamente em todos os arquivos, mas eles fazem parte do contexto minimo esperado para um repositorio `.NET`.

## Estrutura Esperada

A estrutura inicial recomendada para este template e:

```text
templates/
  dotnet-solution/
    README.md
    payload.md
    files/
```

O diretorio `files/` deve conter apenas artefatos que fazem sentido como base compartilhada de uma solution `.NET`.

O arquivo `payload.md` deve documentar as regras operacionais do conteudo em `files/`.

## Relacao com o CLI

O CLI deve usar este template para:

- materializar a solution base
- resolver placeholders associados a solution e namespace
- preparar a estrutura sobre a qual templates de projeto poderao atuar

O CLI nao deveria hardcodar a estrutura da solution se ela ja estiver publicada neste template.

## Relacao com IA

Agentes de IA devem conseguir olhar para este template e entender:

- qual e a base tecnica esperada de um repositorio `.NET`
- quais artefatos pertencem ao nivel da solution
- onde termina a responsabilidade da solution e onde comecam projetos especificos

## Regra de Qualidade

Um arquivo deve entrar neste template apenas se:

- fizer parte da base compartilhada de uma solution `.NET`
- puder ser reutilizado por mais de um archetype ou repositorio `.NET`
- nao depender fortemente da implementacao de uma API especifica

Se um artefato existir apenas por causa do projeto HTTP ou dos testes, ele provavelmente deve ficar em outro template.

## Proximo Passo

O proximo passo esperado para este template e continuar decidindo, arquivo por arquivo, quais artefatos devem compor a base oficial de uma solution `.NET`.
