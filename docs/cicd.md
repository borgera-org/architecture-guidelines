# CI/CD

Os projetos devem consumir workflows reutilizaveis deste repositorio via jobs.<job>.uses.

Exemplo:

`yaml
jobs:
  ci:
    uses: igorsiq/architecture-guidelines/.github/workflows/ci-reusable.yml@main
    with:
      setup-node: '20'
      install-command: npm ci
      lint-command: npm run lint
      test-command: npm test -- --ci
      build-command: npm run build
`"; Set-Content -Path docs/seguranca.md -Value 
