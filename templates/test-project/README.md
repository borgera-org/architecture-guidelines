# Test Project Template

## Proposito

Este template define os artefatos base do projeto de testes automatizados em um repositorio `.NET` criado pela plataforma.

Ele existe para padronizar a existencia de uma base minima de testes sem misturar responsabilidades do projeto principal da API, da solution ou de containerizacao.

## Papel Deste Template

O papel deste template e materializar o projeto inicial de testes e sua estrutura basica.

Em termos praticos, este template tende a ser responsavel por artefatos como:

- projeto `.csproj` de testes
- estrutura inicial dentro de `tests/`
- teste basico de smoke ou sanidade
- dependencias minimas para execucao de testes automatizados

## O Que Este Template Resolve

Este template ajuda a resolver problemas como:

- repositorios criados sem estrutura de testes
- variacao excessiva entre stacks de teste para APIs semelhantes
- duplicacao manual de baseline de testes entre times
- acoplamento da criacao do projeto de testes ao codigo do CLI

Ele fornece o primeiro ponto de apoio para validacao automatizada da API, mesmo antes de o dominio estar modelado.

## O Que Este Template Nao Deve Resolver

Este template nao deve concentrar:

- o projeto principal da API
- o arquivo `.sln`
- Dockerfile
- pipeline de CI
- cenarios detalhados de negocio

Essas responsabilidades pertencem a outros templates ou a evolucoes locais do repositorio consumidor.

## Quando Usar

Este template deve ser usado quando um archetype representar um repositorio que precise nascer com projeto inicial de testes.

No estado atual da plataforma, ele faz sentido quando o archetype `api-dotnet` for materializado com `includeTests = true`.

## Quando Nao Usar

Nao faz sentido usar este template para:

- representar sozinho a validacao completa do sistema
- substituir testes de integracao, contrato ou ponta a ponta
- gerar testes altamente especificos de um dominio

Ele existe para fornecer baseline, nao cobertura completa.

## Parametros Esperados

Este template tende a depender de parametros como:

- `rootNamespace`
- `targetFramework`

Dependendo da modelagem final, outros parametros podem surgir, mas o template deve permanecer focado no projeto de testes.

Convencao inicial adotada neste repositorio:

- o nome tecnico do projeto de testes e o caminho inicial em `tests/` usam `{{ rootNamespace }}.Tests`
- o `TargetFramework` e herdado de `Directory.Build.props`
- o framework inicial de testes adotado e `xUnit`
- o projeto de testes referencia o projeto principal da API
- o teste inicial usa `WebApplicationFactory` para validar o endpoint `/health`

## Estrutura Esperada

A estrutura inicial recomendada para este template e:

```text
templates/
  test-project/
    README.md
    payload.md
    files/
```

O diretorio `files/` deve conter apenas artefatos que fazem sentido para o projeto de testes.

O arquivo `payload.md` deve documentar as regras operacionais do conteudo em `files/`.

## Relacao com o CLI

O CLI deve usar este template para:

- materializar o projeto de testes
- resolver placeholders de nome e namespace
- adicionar a base inicial de validacao automatizada ao repositorio

O CLI nao deveria hardcodar a estrutura do projeto de testes se ela ja estiver publicada neste template.

## Relacao com IA

Agentes de IA devem conseguir olhar para este template e entender:

- qual e a base oficial de testes para APIs em `.NET`
- quais artefatos pertencem ao projeto de testes
- onde termina o baseline de testes e onde comecam cenarios especificos do sistema

## Regra de Qualidade

Um arquivo deve entrar neste template apenas se:

- fizer parte do baseline do projeto de testes
- puder ser reutilizado por mais de um repositorio de API em `.NET`
- nao depender fortemente de um dominio especifico

Se um artefato existir apenas para um caso de negocio particular, ele provavelmente nao pertence a este template.

## Proximo Passo

O proximo passo esperado para este template e continuar decidindo, arquivo por arquivo, quais artefatos devem compor a base oficial do projeto de testes.
