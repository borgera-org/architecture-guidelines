# Docker Files Payload

## Proposito

Este documento descreve os arquivos concretos que o CLI deve copiar ou materializar ao aplicar o template `docker-files`.

Ele documenta a carga util do template sem competir com os arquivos reais que viverao em `files/`.

## Regra de Mapeamento

Os arquivos mantidos em `files/` devem ser interpretados como os artefatos basicos de containerizacao do repositorio gerado.

Em termos praticos:

- tudo o que estiver em `files/` deve ser aplicado no repositorio consumidor
- a estrutura relativa dentro de `files/` deve ser preservada
- o conteudo deve representar o baseline de empacotamento, e nao deploy ou pipeline
- arquivos com sufixo `.tpl` devem ser renderizados e materializados sem o sufixo no destino
- arquivos sem `.tpl` devem ser copiados literalmente

## Tipos de Arquivo Esperados

Os tipos mais provaveis de artefato neste template sao:

- `Dockerfile`
- `.dockerignore`
- outros arquivos auxiliares estritamente ligados ao empacotamento

Esses artefatos devem ser suficientemente genericos para servir como base oficial de containerizacao para APIs em `.NET`.

## Placeholders

Arquivos em `files/` podem conter placeholders resolvidos pelo CLI a partir dos inputs do archetype.

Exemplos conceituais:

- `{{ rootNamespace }}`
- `{{ dotnetImageTag }}`

Regra importante:

- placeholders devem depender de inputs publicados pelo archetype
- o CLI deve ser a camada responsavel por resolver substituicoes
- nomes de placeholders devem permanecer previsiveis

Convencao inicial adotada:

- o `Dockerfile` usa imagens `sdk` e `aspnet` com a mesma `dotnetImageTag`

## O Que Pode Entrar Aqui

Pode entrar em `files/`:

- Dockerfile base
- regras de `.dockerignore`
- artefatos reutilizaveis de empacotamento

## O Que Nao Deve Entrar Aqui

Nao deve entrar em `files/`:

- manifests de Kubernetes
- arquivos de pipeline
- configuracoes especificas de cloud provider
- segredos ou configuracoes sensiveis

Se um artefato fizer sentido apenas para deploy ou infraestrutura, ele provavelmente nao pertence a este template.

## Relacao com o CLI

O CLI deve tratar `files/` como fonte oficial dos artefatos basicos de containerizacao.

Ao aplicar este template, o CLI deve conseguir:

- localizar os artefatos do template
- resolver placeholders necessarios
- materializar o baseline de empacotamento no repositorio consumidor

## Relacao com IA

Agentes de IA devem poder consultar este template para entender:

- como a plataforma espera que a base de containerizacao nasca
- quais artefatos pertencem ao empacotamento basico
- onde termina o baseline e onde comeca a infraestrutura do ambiente

## Regra de Qualidade

Antes de adicionar um novo arquivo em `files/`, a pergunta correta e:

este artefato faz parte do baseline de empacotamento ou depende de uma plataforma de deploy especifica?

Se a resposta depender de CI, cloud provider ou orquestracao, ele provavelmente nao pertence a este template.
