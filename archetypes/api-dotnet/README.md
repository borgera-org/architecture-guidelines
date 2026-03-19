# API .NET Archetype

## Proposito

Este archetype define a forma oficial de iniciar novos repositorios de API HTTP em .NET dentro da plataforma.

Ele existe para reduzir variacao estrutural, tornar o scaffolding previsivel e registrar de forma explicita as decisoes base que uma nova API deve herdar ao nascer.

## Quando Usar

Use este archetype quando o objetivo for:

- criar uma nova API HTTP em .NET
- iniciar um repositorio backend com estrutura padronizada
- gerar uma base que sera consumida e evoluida com apoio do CLI
- seguir o caminho recomendado pela plataforma para APIs

## Quando Nao Usar

Nao use este archetype quando o objetivo for:

- criar um worker sem interface HTTP
- criar uma biblioteca compartilhada
- criar um frontend
- modelar um repositorio altamente especifico que ainda nao possa ser generalizado

Se o tipo de repositorio nao for uma API HTTP em .NET, este archetype provavelmente nao e o contrato correto.

## O Que Este Archetype Decide

Este archetype ja incorpora algumas decisoes estruturais:

- o repositorio representa uma API HTTP
- a plataforma base e .NET
- existe uma solution explicita
- a estrutura esperada inclui `src` e pode incluir `tests`
- o scaffolding pode incluir testes e artefatos de containerizacao

Essas decisoes nao resolvem o design completo do sistema. Elas apenas definem o baseline arquitetural do repositorio.

## Inputs Esperados

### `repositoryName`

Nome do repositorio a ser criado.

Intencao:

- identificar o repositorio no provedor de codigo
- refletir o tipo de servico de forma previsivel

Convencao atual:

- deve usar `kebab-case`

### `serviceName`

Nome logico do servico.

Intencao:

- identificar a API no contexto de negocio ou plataforma
- servir como referencia para documentacao e nomenclatura do servico

### `solutionName`

Nome da solution .NET.

Intencao:

- agrupar projetos relacionados em uma estrutura previsivel
- evitar solutions implicitas ou inconsistentes

### `rootNamespace`

Namespace raiz dos projetos .NET.

Intencao:

- manter consistencia de nomenclatura entre projetos e codigo

Convencao atual:

- deve usar `PascalCase`

### `targetFramework`

Framework alvo da API.

Valor padrao atual:

- `net8.0`

Intencao:

- tornar explicita a base tecnica do archetype
- evitar scaffolding com framework indefinido

### `dotnetImageTag`

Tag base das imagens `.NET` usadas no `Dockerfile`.

Valor padrao atual:

- `8.0`

Intencao:

- alinhar a imagem de build e runtime com a baseline da stack
- evitar que a escolha da imagem Docker fique implicita no CLI

### `includeTests`

Define se o scaffolding deve incluir um projeto inicial de testes.

Valor padrao atual:

- `true`

Intencao:

- incentivar a existencia de estrutura de testes desde o inicio
- controlar a aplicacao do template `test-project`

### `includeDocker`

Define se o scaffolding deve incluir artefatos basicos de containerizacao.

Valor padrao atual:

- `true`

Intencao:

- preparar a base do repositorio para cenarios comuns de empacotamento e execucao
- controlar a aplicacao do template `docker-files`

## Constraints Publicadas

O archetype atualmente publica estas restricoes:

- nome do repositorio em `kebab-case`
- namespace raiz em `PascalCase`
- solution obrigatoria
- escopo restrito a APIs HTTP

Essas constraints existem para impedir que o archetype seja usado como template generico para qualquer backend.

## Resultado Esperado

Ao consumir este archetype, o resultado esperado e um repositorio que tenha:

- tipo de repositorio classificado como API
- plataforma .NET
- diretorio base `src`
- artefatos iniciais coerentes com API HTTP em .NET
- projeto de testes quando `includeTests = true`
- artefatos de Docker quando `includeDocker = true`

## Post-Processing Declarado

No baseline atual, este archetype tambem publica passos explicitos de
pos-processamento.

Hoje isso cobre:

- adicionar o projeto principal da API a solution
- adicionar o projeto de testes a solution quando `includeTests == true`

Isso importa porque o estado final correto do repositorio nao nasce apenas da
copia dos templates. O CLI precisa conectar artefatos que foram materializados
separadamente.

## Estado Atual

Status atual:

- `draft`

Isso significa que:

- o contrato estrutural inicial ja foi definido
- o schema inicial do archetype ja foi formalizado
- os templates iniciais ja foram criados neste repositorio
- ja existe example oficial materializado com validacao automatizada basica
- o pos-processamento necessario ja foi declarado no contrato do archetype
- o archetype continua em draft porque a semantica completa de `when`, a validacao em pipeline e a implementacao estavel do CLI ainda nao foram fechadas

## Relacao com o CLI

O CLI deve usar este archetype para:

- descobrir quais entradas pedir
- validar o contrato do archetype
- selecionar os templates corretos
- avaliar as condicoes `when` publicadas
- gerar a estrutura inicial do repositorio
- executar os passos declarados de `postProcessing`

O CLI nao deveria manter essas regras hardcoded se elas ja estiverem publicadas aqui.

## Relacao com IA

Agentes de IA devem interpretar este archetype como a forma recomendada de iniciar APIs HTTP em .NET.

Na pratica, isso ajuda a IA a:

- sugerir a estrutura correta
- evitar padroes paralelos
- justificar decisoes com base em um contrato central

## Perguntas Que Este Archetype Ainda Nao Resolve

Este archetype ainda nao define:

- a estrutura interna detalhada dos projetos .NET
- o padrao arquitetural interno da aplicacao
- convencoes de observabilidade, seguranca ou CI
- a semantica formal da linguagem de condicoes usada em `templateSet`
- tipos adicionais de pos-processamento alem de `solution-add-project`

Esses pontos devem aparecer nos proximos artefatos da plataforma.
