# Governanca de Arquitetura

## Dono dos dominios
- Responsavel principal: Igor.

## Quem decide
- Decisoes de arquitetura do dominio: dono do dominio.
- Decisoes centrais (workflow, seguranca, compliance): dono do dominio com validacao de impacto no piloto.

## Quem revisa
- Alteracoes em .github/ e workflows: code owner obrigatorio.
- Alteracoes com risco alto: requerem justificativa de risco, smoke test e rollback explicito.
- Mudanca central so pode ser mergeada com branch protection e checks obrigatorios ativos na branch principal.

## Como escalar
- Conflito tecnico sem consenso: abrir issue arquitetural com opcoes e trade-offs.
- Mudanca breaking: ADR obrigatoria antes do merge.

## Rito minimo por mudanca central
1. Abrir issue com objetivo, risco e criterio de pronto.
2. Abrir PR com checklist obrigatorio.
3. Executar smoke test no piloto conforme o padrao operacional.
4. Aprovar e comunicar consumidores.
