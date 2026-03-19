# Smoke Test no Piloto

Esta politica define quando o smoke test e obrigatorio, qual e o escopo minimo esperado e como a evidencia deve ser registrada.

## Objetivo
- Validar a mudanca central em ambiente controlado antes da propagacao.
- Identificar regressao funcional, operacional ou de seguranca cedo.
- Produzir evidencia comparavel entre mudancas e entre repositorios consumidores.

## Quando e obrigatorio
- Mudanca em workflow reutilizavel de CI.
- Mudanca em workflow ou baseline de seguranca/compliance.
- Mudanca breaking ou com impacto em integracao.
- Uso de `@main` em piloto antes da publicacao de tag estavel.
- Release de nova versao de workflow central.

## Quando pode ser dispensado
- Documentacao sem impacto em pipeline, seguranca ou integracao.
- Ajuste editorial sem efeito no contrato de consumo.

Toda dispensa deve ser justificada no PR.

## Repositorio piloto
- O piloto deve representar um consumidor real.
- O piloto deve ter owner identificado e capacidade de validar impacto.
- O piloto deve ser o primeiro alvo antes de qualquer propagacao por ondas.

## Escopo minimo por tipo de mudanca
### Workflow de CI
- Workflow central consumido pelo piloto com a versao candidata.
- Execucao completa do fluxo principal do consumidor.
- Confirmacao de que os passos essenciais do pipeline continuam verdes.
- Avaliacao de regressao relevante de tempo de pipeline.

### Seguranca e compliance
- Execucao do workflow de seguranca no piloto.
- Confirmacao de ausencia de falso positivo critico sem mitigacao.
- Registro de qualquer excecao, supressao ou ajuste manual exigido.

### Breaking change
- Smoke test reforcado no piloto principal.
- Validacao adicional em pelo menos um consumidor representativo antes de ampliar rollout.
- Compatibilidade e plano de migracao explicitados no PR ou ADR.

## Evidencias obrigatorias
- Repositorio piloto validado.
- Tipo de mudanca central.
- Identificador da mudanca central: issue, PR, commit ou tag candidata.
- Links das execucoes de workflow no piloto.
- Resultado observado e criterio de sucesso.
- Impacto relevante percebido, inclusive tempo de pipeline.
- Risco residual conhecido antes da propagacao.

## Modelo de registro no PR
```md
## Evidencia de smoke test
- Repositorio piloto:
- Tipo de mudanca:
- Versao, tag ou ref avaliada:
- Execucoes:
  - CI:
  - Seguranca:
- Resultado:
- Variacao relevante de tempo:
- Risco residual:
```

## Gate para seguir rollout
- Smoke test obrigatorio concluido com evidencia suficiente.
- Sem regressao relevante sem mitigacao aprovada.
- Rollback same-day descrito no PR.
- Comunicacao pronta para consumidores afetados.
