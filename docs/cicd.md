# CI/CD

Os projetos devem consumir workflows reutilizaveis deste repositorio via jobs.<job>.uses.

Exemplo:

```yaml
jobs:
  ci:
    uses: borgera-org/architecture-guidelines/.github/workflows/ci-reusable.yml@main
    with:
      setup-node: '20'
      install-command: npm ci
      lint-command: npm run lint
      test-command: npm test -- --ci
      build-command: npm run build
```

## Regras minimas
- Toda mudanca central deve passar por smoke test no piloto.
- Mudancas de alto risco devem explicitar rollback no PR.
- Checks obrigatorios devem bloquear merge na branch principal.
