# node-consumer

Template inicial para novos repositorios Node que vao consumir os workflows centrais do `architecture-guidelines`.

## Arquivos incluidos
- `.arch-guidelines.yml`
- `.github/CODEOWNERS`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/workflows/ci.yml`
- `.github/workflows/security.yml`

## Arquivos nao incluidos por decisao de baseline
- `.github/ISSUE_TEMPLATE/`

O consumidor nasce sem issue templates locais para evitar duplicacao de governanca central.

## Antes do primeiro merge
1. Substituir placeholders de owner e nome do repositorio.
2. Confirmar que o projeto expoe os scripts `lint`, `test` e `build`.
3. Ajustar a versao do Node ou comandos, se necessario.
4. Configurar branch protection com checks `ci` e `security`.
5. Abrir o primeiro PR com smoke test e rollback documentados.

## Observacoes
- Este template assume consumo do canal estavel `@v1`.
- Se o canal estavel ainda nao existir, o uso de `@main` deve ficar restrito a piloto aprovado.
- Se o repositorio precisar de issue templates no futuro, eles devem ser estritamente locais ao produto.
