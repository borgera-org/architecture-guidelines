## Contexto
Descreva o problema de negocio/tecnico e o objetivo desta mudanca.

## Escopo de Impacto
- [ ] Codigo de aplicacao
- [ ] Pipeline/workflow
- [ ] Seguranca/compliance
- [ ] Documentacao
- [ ] Dependencias

## Tipo de mudanca
- [ ] Documentacao
- [ ] Workflow de CI
- [ ] Seguranca e compliance
- [ ] Breaking change

## Risco
Descreva o risco principal e a mitigacao.

## Compatibilidade
Descreva impacto em consumidores e compatibilidade retroativa.

## Branch protection e checks
- Branch principal impactada:
- Checks obrigatorios afetados:
- Necessita ajuste de branch protection nos consumidores:

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

## Plano de rollback
- Unidade de reversao:
- Responsavel pela execucao:
- Gatilho para acionar rollback:
- Passo tecnico de reversao:
- Como revalidar o piloto:
- Comunicacao aos consumidores:

## Comunicacao para times consumidores
Descreva como e onde a mudanca foi comunicada.

## Gate de aprovacao (referencia de politica inicial)
- [ ] Documentacao: 1 aprovacao
- [ ] Workflow de CI: 1 aprovacao + smoke test
- [ ] Seguranca/compliance: 1 aprovacao + smoke test + rollback explicito
- [ ] Breaking change: ADR obrigatoria antes de merge

## Checklist final
- [ ] Contexto preenchido
- [ ] Escopo de impacto definido
- [ ] Risco e mitigacao descritos
- [ ] Compatibilidade avaliada
- [ ] Baseline de branch protection e checks avaliada
- [ ] Evidencia de smoke test anexada
- [ ] Rollback explicito definido
- [ ] Comunicacao registrada
- [ ] Smoke test segue o padrao de `docs/smoke-test.md`
