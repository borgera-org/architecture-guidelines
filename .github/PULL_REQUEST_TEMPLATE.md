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

## Evidencia de smoke test
Inclua links/prints dos testes de fumaca no piloto.

## Plano de rollback
Descreva como restaurar o estado anterior no mesmo dia.

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
- [ ] Evidencia de smoke test anexada
- [ ] Rollback explicito definido
- [ ] Comunicacao registrada
