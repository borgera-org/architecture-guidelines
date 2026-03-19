# Repository Files Payload

## Proposito

Este documento descreve os arquivos concretos que o CLI deve copiar ou materializar na raiz do repositorio consumidor ao aplicar o template `repository-files`.

Ele documenta a carga util do template sem competir com os arquivos reais que vivem em `files/`.

## Regra de Mapeamento

Os arquivos mantidos em `files/` devem ser interpretados como arquivos de raiz do repositorio gerado.

Em termos praticos:

- tudo o que estiver em `files/` deve ser aplicado no repositorio consumidor
- a estrutura relativa dentro de `files/` deve ser preservada
- este template deve continuar focado em arquivos de nivel de raiz
- arquivos com sufixo `.tpl` devem ser renderizados e materializados sem o sufixo no destino
- arquivos sem `.tpl` devem ser copiados literalmente

## Tipos de Arquivo Esperados

Os tipos mais provaveis de arquivo em `files/` sao:

- `README.md`
- `.gitignore`
- `.editorconfig`
- outros arquivos basicos de inicializacao de repositorio

Esses arquivos devem ser suficientemente genericos para reaproveitamento por multiplos repositorios consumidores.

## Placeholders

Arquivos em `files/` podem conter placeholders resolvidos pelo CLI a partir dos inputs do archetype.

Exemplos conceituais:

- `{{ repositoryName }}`
- `{{ serviceName }}`
- `{{ solutionName }}`

Regra importante:

- placeholders devem depender de inputs publicados pelo archetype
- nomes de placeholders devem ser previsiveis
- o CLI deve ser a camada responsavel por resolver substituicoes

Os arquivos em `files/` nao devem depender de variaveis ocultas ou convencoes nao documentadas.

## O Que Pode Entrar Aqui

Pode entrar em `files/`:

- arquivos de raiz reutilizaveis
- conteudo inicial padronizado
- arquivos que ajudem onboarding, higiene tecnica e consistencia basica do repositorio

## O Que Nao Deve Entrar Aqui

Nao deve entrar em `files/`:

- arquivos especificos de uma stack quando houver template mais apropriado
- estrutura interna de `src/` ou `tests/`
- arquivos que dependam de comportamento especial nao declarado
- artefatos de um unico produto ou time sem potencial real de reuso

## Relacao com o CLI

O CLI deve tratar `files/` como fonte versionada oficial para arquivos-base de raiz.

Ao aplicar este template, o CLI deve conseguir:

- localizar os arquivos deste diretorio
- preservar a estrutura relativa
- resolver placeholders declarados
- escrever os arquivos no destino correto

## Relacao com IA

Agentes de IA devem poder inspecionar este template para entender:

- quais arquivos base a plataforma considera obrigatorios ou recomendados
- quais valores devem ser parametrizados
- onde termina o template de raiz e onde comecam templates mais especificos

## Regra de Qualidade

Antes de adicionar um novo arquivo em `files/`, a pergunta correta e:

este arquivo e parte da base transversal de um repositorio ou pertence a outro template mais especifico?

Se a resposta for que ele depende fortemente de .NET, API HTTP, testes ou pipeline, ele provavelmente nao pertence a este template.
