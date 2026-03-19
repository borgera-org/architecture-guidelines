# Branch Protection e Checks Obrigatorios

Esta politica define a baseline minima de protecao de branch e checks obrigatorios para o repositorio central e para os repositorios consumidores.

## Objetivo
- Impedir merge direto sem revisao.
- Garantir evidencias minimas antes de promover mudancas centrais ou locais.
- Reduzir variacao entre repositorios consumidores.

## Escopo
- Repositorio central `architecture-guidelines`
- Repositorios consumidores que adotam os workflows e baselines deste repositorio

## Baseline para o repositorio central
### Branch alvo
- `main`

### Regras obrigatorias
- Pull request obrigatoria para merge.
- Pelo menos 1 aprovacao.
- Review de code owner obrigatoria para mudancas em `.github/`.
- Dismiss stale approvals quando novos commits entrarem no PR.
- Conversas resolvidas antes do merge.
- Force push bloqueado.
- Delecao da branch protegida bloqueada.

### Checks obrigatorios recomendados
- `governance-baseline / docs-policy`
- `governance-baseline / reusable-workflows`

## Baseline para repositorios consumidores
### Branch alvo
- Branch principal do repositorio consumidor.

### Regras obrigatorias
- Pull request obrigatoria para merge.
- Pelo menos 1 aprovacao.
- CODEOWNERS ativo para `.github/`, seguranca e componentes criticos.
- Dismiss stale approvals quando novos commits entrarem no PR.
- Conversas resolvidas antes do merge.
- Force push bloqueado.
- Delecao da branch protegida bloqueada.

### Checks obrigatorios minimos
- Check principal de CI do repositorio consumidor.
- Check de seguranca do repositorio consumidor.

### Checks adicionais por criticidade
- Build ou empacotamento, quando separado do CI principal.
- Validacao de deploy ou smoke test automatizado, quando existir.

## Convencao de nomes recomendada
- Workflow principal de CI: `ci`
- Workflow principal de seguranca: `security`
- Manter nomes de checks estaveis ao longo do tempo para evitar reconfiguracao frequente de branch protection.

## Excecoes
- Toda excecao deve ser formalmente documentada no PR, issue ou ADR conforme risco.
- Repositorio consumidor nao deve remover check obrigatorio sem justificativa e aprovacao do owner responsavel.

## Implementacao inicial recomendada
1. Configurar a protecao da `main` no repositorio central.
2. Tornar os checks do repositorio central obrigatorios.
3. Replicar a baseline minima para cada novo repositorio consumidor no momento da criacao.
4. Revisar periodicamente se os checks continuam representando o contrato real do repositorio.
