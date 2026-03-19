# CI/CD

Os projetos devem consumir workflows reutilizaveis deste repositorio via jobs.<job>.uses.

Exemplo:

```yaml
jobs:
  ci:
    uses: borgera-org/architecture-guidelines/.github/workflows/ci-reusable.yml@v1
    with:
      setup-node: '20'
      install-command: npm ci
      lint-command: npm run lint
      test-command: npm test -- --ci
      build-command: npm run build
```

## Canal de consumo
- Padrao para novos repositorios consumidores: tag estavel de major, por exemplo `@v1`.
- Repositorios criticos podem congelar em tag imutavel, por exemplo `@v1.0.0`.
- `@main` fica restrito a piloto ou validacao antecipada, com risco e rollback documentados.
- A adocao em escala deve comecar somente apos a publicacao da primeira tag estavel do canal.

## Regras minimas
- Toda mudanca central deve passar por smoke test no piloto.
- Mudancas de alto risco devem explicitar rollback no PR.
- Checks obrigatorios devem bloquear merge na branch principal.
- O smoke test deve seguir o padrao definido em `docs/smoke-test.md`.
- A baseline de branch protection e checks obrigatorios deve seguir `docs/branch-protection.md`.
- Novos repositorios consumidores devem nascer a partir do `golden path` suportado em `docs/golden-path.md`.
