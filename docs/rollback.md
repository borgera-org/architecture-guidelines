# Rollback Same-Day

Esta politica define quando e como reverter mudancas centrais no mesmo dia.

## Gatilhos de rollback
- Quebra de pipeline no piloto por mudanca central.
- Regressao relevante de tempo de pipeline.
- Falso positivo critico sem mitigacao imediata.
- Regressao operacional confirmada em repositorio consumidor.

## Responsavel
- Responsavel primario: dono da mudanca central.
- Responsavel de apoio: dono do repositorio piloto afetado.

## SLA
- Decisao inicial: ate 30 minutos apos confirmacao do incidente.
- Reversao ou mitigacao: no mesmo dia.
- Comunicacao aos consumidores: imediatamente apos decisao de rollback.

## Procedimento
1. Confirmar causa e escopo do impacto.
2. Congelar novas propagacoes da mudanca.
3. Reverter PR ou commit central relacionado.
4. Reexecutar smoke test no piloto.
5. Comunicar status e proximo passo aos consumidores.

## Evidencias obrigatorias
- Link do incidente/issue.
- Link do PR ou commit revertido.
- Resultado do smoke test apos rollback.

## Mensagem padrao de incidente
"Rollback same-day iniciado para mudanca central <identificador>. Motivo: <gatilho>. Escopo afetado: <repositorios>. Acao imediata: reversao e reexecucao de smoke test no piloto. Nova atualizacao em ate 30 minutos."