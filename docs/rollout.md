# Rollout Controlado

Esta politica define como propagar mudancas centrais com baixo risco para repositorios consumidores.

## Principios
- Expandir por ondas pequenas.
- Validar no piloto antes de ampliar alcance.
- Nao propagar mudancas sem evidencias minimas.

## Ordem de rollout recomendada
1. Piloto principal: identity-service.
2. Repositorio de complexidade similar e baixo acoplamento.
3. Repositorio com maior criticidade operacional.

## Checklist de adocao por repositorio
- Workflow central referenciado por tag ou main conforme criticidade.
- CODEOWNERS e PR template habilitados no repositorio consumidor.
- Branch protection com checks obrigatorios ativa.
- Smoke test executado apos adocao.
- Rollback documentado no PR de adocao.

## Criterios para avancar de onda
- Check de CI e seguranca sem regressao relevante.
- Tempo de pipeline dentro do limite esperado.
- Sem falso positivo critico sem mitigacao.
- Sem incidente aberto associado a mudanca central.

## Metricas minimas
- Percentual de projetos consumindo workflow central.
- Percentual de projetos com baseline atualizado.
- Lead time entre mudanca central e adocao.
- Taxa de falha de pipeline apos atualizacao central.

## Responsabilidades
- Dono da mudanca central: prepara changelog, smoke test e plano de rollback.
- Dono do repositorio consumidor: valida adocao local e evidencia impacto.

## Evidencias esperadas
- Link do PR no repositorio central.
- Link do PR de adocao no consumidor.
- Links de execucao dos workflows.