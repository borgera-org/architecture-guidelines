# Golden Path para Novos Repositorios Consumidores

Esta politica define o caminho padrao para criar novos repositorios consumidores com a baseline central ja aplicada desde o inicio.

## Escopo atual
- Archetype suportado neste momento: `templates/node-consumer`
- Stack suportada: Node.js
- Canal de consumo recomendado para workflows centrais: `@v1`

## Objetivo
- Reduzir montagem manual na criacao de novos repositorios.
- Garantir consistencia minima de CI, seguranca, CODEOWNERS e PR template.
- Acelerar onboarding sem perder controle de rollout e branch protection.
- Evitar duplicacao de governanca central em templates locais de issue.

## Artefatos entregues pelo archetype
- Manifesto `.arch-guidelines.yml`
- `CODEOWNERS`
- `PULL_REQUEST_TEMPLATE.md`
- Workflow `ci`
- Workflow `security`

## Decisao sobre issue templates
- Novos repositorios consumidores comecam sem `ISSUE_TEMPLATE`.
- O rastreamento de trabalho local pode existir sem template padrao, conforme a necessidade do time.
- Governanca central, rollout e rollback nao devem ser duplicados em issue templates de consumidores.

## Passo a passo de bootstrap
1. Copiar o conteudo de `templates/node-consumer` para o novo repositorio.
2. Preencher os placeholders do `.arch-guidelines.yml` e do `CODEOWNERS`.
3. Ajustar comandos do workflow `ci` caso o repositorio use scripts diferentes do padrao Node sugerido.
4. Publicar o repositorio com os workflows apontando para o canal estavel `@v1`.
5. Configurar branch protection da branch principal com os checks `ci` e `security`.
6. Abrir o primeiro PR de adocao com evidencia de smoke test e rollback documentado.
7. Validar no piloto antes de propagar qualquer customizacao central para outros consumidores.

## Definicao de pronto para um novo consumidor
- Workflows `ci` e `security` ativos no repositorio.
- `CODEOWNERS` preenchido com owner local e owner de plataforma.
- Branch protection ativa com checks obrigatorios minimos.
- Primeiro PR com smoke test e rollback documentados.
- Repositorio inventariado via `.arch-guidelines.yml`.
- Nenhum `ISSUE_TEMPLATE` local criado por padrao.

## Limites atuais
- Ainda nao ha archetype oficial para .NET, Java ou Python.
- O golden path atual depende da publicacao do canal estavel `@v1`.
- Ajustes de branch protection continuam sendo configuracao no GitHub, nao arquivo versionado no repositorio.
