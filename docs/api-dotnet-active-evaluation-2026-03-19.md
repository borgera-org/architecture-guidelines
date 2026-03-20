# API .NET Active Evaluation 2026-03-19

## Proposito

Este documento registra a avaliacao formal do archetype `api-dotnet` contra os criterios publicados em [archetype-lifecycle.md](c:/Users/igors/source/repos/architecture-guidelines/docs/archetype-lifecycle.md).

## Escopo

O objetivo desta avaliacao e decidir se o archetype `api-dotnet` ja pode ser promovido de `draft` para `active`.

## Resultado

Resultado da avaliacao:

- aprovado para promocao para `active`

## Avaliacao por Criterio

### 1. Contrato estrutural completo

Status:

- atendido

Evidencias:

- [definition.yaml](c:/Users/igors/source/repos/architecture-guidelines/archetypes/api-dotnet/definition.yaml)
- [README.md](c:/Users/igors/source/repos/architecture-guidelines/archetypes/api-dotnet/README.md)
- templates referenciados em [templates/](c:/Users/igors/source/repos/architecture-guidelines/templates)
- `postProcessing` declarado no proprio archetype

### 2. Semantica contratual publicada

Status:

- atendido

Evidencias:

- `inputs`, `constraints`, `outputs` e `consumerGuidance` publicados em [definition.yaml](c:/Users/igors/source/repos/architecture-guidelines/archetypes/api-dotnet/definition.yaml)
- semantica de `when` publicada em [cli-contract.md](c:/Users/igors/source/repos/architecture-guidelines/docs/cli-contract.md)
- subset de `when` validado por [archetype.schema.json](c:/Users/igors/source/repos/architecture-guidelines/schemas/archetype.schema.json), [post-processing.schema.json](c:/Users/igors/source/repos/architecture-guidelines/schemas/post-processing.schema.json) e [validate_archetypes.py](c:/Users/igors/source/repos/architecture-guidelines/scripts/validate_archetypes.py)

### 3. Cobertura de examples suficiente

Status:

- atendido

Evidencias:

- caminho padrao em [minimal-default](c:/Users/igors/source/repos/architecture-guidelines/examples/api-dotnet/minimal-default/README.md)
- variacao sem testes em [without-tests](c:/Users/igors/source/repos/architecture-guidelines/examples/api-dotnet/without-tests/README.md)
- variacao sem Docker em [without-docker](c:/Users/igors/source/repos/architecture-guidelines/examples/api-dotnet/without-docker/README.md)

### 4. Validacao automatizada aderente

Status:

- atendido

Evidencias:

- [validate_archetypes.py](c:/Users/igors/source/repos/architecture-guidelines/scripts/validate_archetypes.py)
- [validate_example.py](c:/Users/igors/source/repos/architecture-guidelines/scripts/validate_example.py)
- workflow [validate-platform.yml](c:/Users/igors/source/repos/architecture-guidelines/.github/workflows/validate-platform.yml)

Validacoes executadas nesta avaliacao:

- `python scripts/validate_archetypes.py`
- `python scripts/validate_example.py`

### 5. Ausencia de lacuna contratual critica

Status:

- atendido

Justificativa:

- o archetype publica `inputs`, `templateSet`, `when`, `postProcessing`, constraints e outputs
- o subset de `when` agora e pequeno, explicito e validado
- o CLI ja pode implementar o baseline sem precisar inventar comportamento essencial fora do contrato publicado

### 6. Aprovacao explicita dos mantenedores

Status:

- atendido nesta mudanca

Justificativa:

- esta avaliacao registra a decisao
- o `status` do archetype e atualizado junto com esta evidência

## Riscos Residuais

Mesmo com a promocao para `active`, ainda permanecem riscos normais de evolucao:

- o produto CLI ainda precisa exercitar esse contrato em implementacao real
- novos tipos de archetype ainda precisarao amadurecer seus proprios contratos
- a estrategia de versionamento da plataforma ainda pode evoluir

## Decisao Final

O archetype `api-dotnet` atende os criterios minimos publicados para promocao e deve passar a ser tratado como o caminho oficial da plataforma para novas APIs HTTP em `.NET`.
