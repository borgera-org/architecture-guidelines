# Docker Files Template

## Proposito

Este template define os artefatos basicos de containerizacao para repositorios consumidores criados pela plataforma.

Ele existe para padronizar a base minima de empacotamento em Docker sem misturar responsabilidades do projeto principal da API, da solution ou da pipeline de entrega.

## Papel Deste Template

O papel deste template e materializar os arquivos iniciais relacionados a containerizacao.

Em termos praticos, este template tende a ser responsavel por artefatos como:

- `Dockerfile`
- `.dockerignore`
- outros arquivos basicos de empacotamento, quando fizer sentido

## O Que Este Template Resolve

Este template ajuda a resolver problemas como:

- Dockerfiles criados de forma inconsistente entre times
- ausencia de baseline de empacotamento em novos repositorios
- duplicacao manual de configuracoes basicas de containerizacao
- acoplamento da estrategia inicial de containerizacao ao codigo do CLI

Ele fornece a base minima para que o repositorio possa ser empacotado em container de forma previsivel.

## O Que Este Template Nao Deve Resolver

Este template nao deve concentrar:

- o projeto principal da API
- o arquivo `.sln`
- o projeto de testes
- pipeline de CI
- manifests de deploy
- detalhes de infraestrutura de runtime

Essas responsabilidades pertencem a outros templates ou a repositorios de infraestrutura.

## Quando Usar

Este template deve ser usado quando um archetype representar um repositorio que precise nascer com artefatos basicos de containerizacao.

No estado atual da plataforma, ele faz sentido quando o archetype `api-dotnet` for materializado com `includeDocker = true`.

## Quando Nao Usar

Nao faz sentido usar este template para:

- representar sozinho a estrategia completa de deploy
- substituir manifests de orquestracao
- modelar configuracoes especificas de infraestrutura

Ele existe para fornecer baseline de empacotamento, nao plataforma completa de execucao.

## Parametros Esperados

Este template tende a depender de parametros como:

- `rootNamespace`
- `dotnetImageTag`

Dependendo da modelagem final, outros parametros podem surgir, mas o template deve permanecer focado na camada de containerizacao basica.

Convencao inicial adotada neste repositorio:

- o `Dockerfile` usa build multi-stage
- a tag das imagens `.NET` e controlada por `dotnetImageTag`

## Estrutura Esperada

A estrutura inicial recomendada para este template e:

```text
templates/
  docker-files/
    README.md
    payload.md
    files/
```

O diretorio `files/` deve conter apenas artefatos que fazem sentido para a containerizacao basica do repositorio.

O arquivo `payload.md` deve documentar as regras operacionais do conteudo em `files/`.

## Relacao com o CLI

O CLI deve usar este template para:

- materializar os arquivos basicos de containerizacao
- resolver placeholders necessarios
- manter consistencia entre repositorios criados em momentos diferentes

O CLI nao deveria hardcodar Dockerfiles ou ignore rules se esses artefatos ja estiverem publicados neste template.

## Relacao com IA

Agentes de IA devem conseguir olhar para este template e entender:

- qual e o baseline oficial de containerizacao
- quais artefatos pertencem ao empacotamento basico
- onde termina a responsabilidade do template e onde comeca a infraestrutura do ambiente

## Regra de Qualidade

Um arquivo deve entrar neste template apenas se:

- fizer parte do baseline de containerizacao
- puder ser reutilizado por mais de um repositorio de API em `.NET`
- nao depender fortemente de uma plataforma de deploy especifica

Se um artefato existir apenas por causa de Kubernetes, cloud provider ou pipeline de entrega, ele provavelmente nao pertence a este template.

## Proximo Passo

O proximo passo esperado para este template e continuar decidindo, arquivo por arquivo, quais artefatos devem compor a base oficial de containerizacao.
