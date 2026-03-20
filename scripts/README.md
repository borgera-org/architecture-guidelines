# Scripts

## Proposito

Este diretorio concentra scripts auxiliares para validar contratos e artefatos materializados neste repositorio.

Eles nao substituem os schemas e a documentacao. Eles existem para automatizar verificacoes repetiveis.

## Scripts Atuais

### `validate_archetypes.py`

Valida definicoes de archetypes contra
[archetype.schema.json](c:/Users/igors/source/repos/architecture-guidelines/schemas/archetype.schema.json),
contra
[post-processing.schema.json](c:/Users/igors/source/repos/architecture-guidelines/schemas/post-processing.schema.json)
e contra a estrutura local esperada do repositorio.

No estado atual, ele verifica:

- aderencia de `definition.yaml` ao schema do archetype
- aderencia de cada passo de `postProcessing` ao schema proprio
- aderencia semantica de `when` ao subset booleano suportado
- existencia de `README.md` no diretorio do archetype
- consistencia entre `id` do archetype e nome do diretorio
- existencia local dos templates referenciados em `templateSet`
- ausencia de ids de input e template duplicados

Uso:

```text
python scripts/validate_archetypes.py
python scripts/validate_archetypes.py archetypes/api-dotnet/definition.yaml
```

### `validate_example.py`

Valida manifests de examples contra [example-manifest.schema.json](c:/Users/igors/source/repos/architecture-guidelines/schemas/example-manifest.schema.json) e executa verificacoes estruturais sobre o snapshot materializado.

No estado atual, ele verifica:

- aderencia do manifesto ao schema
- existencia dos arquivos declarados em `expectedFiles`
- ausencia dos caminhos declarados em `expectedAbsentPaths`
- existencia dos caminhos referenciados em `postProcessing`
- ausencia de placeholders nao resolvidos em caminhos e conteudo do snapshot
- aderencia do snapshot ao resultado renderizado dos templates aplicados
- correspondencia exata entre os projetos declarados em `postProcessing` e os projetos presentes na solution

Arquivos afetados por pos-processamento, como a `.sln`, nao sao comparados por conteudo bruto com o template original. Nesses casos, o script aplica validacoes especificas de pos-processamento.

Uso:

```text
python scripts/validate_example.py
python scripts/validate_example.py examples/api-dotnet/minimal-default/manifest.yaml
```

### `smoke_test_cli.py`

Executa o CLI de referencia contra os manifests oficiais em `examples/` e valida
o resultado gerado com as mesmas regras estruturais aplicadas aos snapshots de
referencia.

No estado atual, ele verifica:

- que o CLI consegue materializar cada scenario oficial
- que os arquivos esperados existem no resultado gerado
- que os caminhos declarados como ausentes continuam ausentes
- que o resultado gerado respeita templates, placeholders e pos-processamento

Uso:

```text
python scripts/smoke_test_cli.py
python scripts/smoke_test_cli.py examples/api-dotnet/minimal-default/manifest.yaml
```

## Uso em CI

A workflow
[validate-platform.yml](c:/Users/igors/source/repos/architecture-guidelines/.github/workflows/validate-platform.yml)
executa os validadores e o smoke test do CLI em pull requests e em push para
`main`.
