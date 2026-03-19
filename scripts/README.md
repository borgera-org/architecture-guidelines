# Scripts

## Proposito

Este diretorio concentra scripts auxiliares para validar contratos e artefatos materializados neste repositorio.

Eles nao substituem os schemas e a documentacao. Eles existem para automatizar verificacoes repetiveis.

## Scripts Atuais

### `validate_example.py`

Valida manifests de examples contra [example-manifest.schema.json](c:/Users/igors/source/repos/architecture-guidelines/schemas/example-manifest.schema.json) e executa verificacoes estruturais sobre o snapshot materializado.

No estado atual, ele verifica:

- aderencia do manifesto ao schema
- existencia dos arquivos declarados em `expectedFiles`
- existencia dos caminhos referenciados em `postProcessing`
- ausencia de placeholders nao resolvidos em caminhos e conteudo do snapshot
- aderencia do snapshot ao resultado renderizado dos templates aplicados
- presenca dos projetos esperados dentro da solution para passos `solution-add-project`

Arquivos afetados por pos-processamento, como a `.sln`, nao sao comparados por conteudo bruto com o template original. Nesses casos, o script aplica validacoes especificas de pos-processamento.

Uso:

```text
python scripts/validate_example.py
python scripts/validate_example.py examples/api-dotnet/minimal-default/manifest.yaml
```
