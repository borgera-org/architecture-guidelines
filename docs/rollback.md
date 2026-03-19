# Rollback Same-Day

Esta politica define quando e como reverter mudancas centrais no mesmo dia.

## Pre-requisitos antes do merge
- Toda mudanca central deve indicar unidade de reversao: PR, commit ou release.
- O PR deve nomear responsavel pelo rollback e repositorio piloto validado.
- O plano de rollback deve indicar como revalidar o piloto apos a reversao.
- O canal e a mensagem de comunicacao devem estar preparados antes da propagacao.

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
3. Reverter PR, commit ou release central relacionado.
4. Reexecutar smoke test no piloto.
5. Comunicar status e proximo passo aos consumidores.

## Evidencias obrigatorias
- Link do incidente/issue.
- Link do PR ou commit revertido.
- Repositorio piloto revalidado apos rollback.
- Resultado do smoke test apos rollback.

## Modelo minimo de registro do rollback
```md
## Plano de rollback
- Unidade de reversao:
- Responsavel pela execucao:
- Gatilho para acionar rollback:
- Passo tecnico de reversao:
- Como revalidar o piloto:
- Comunicacao aos consumidores:
```

## Modelo minimo de incidente
```md
## Rollback same-day
- Mudanca central:
- Gatilho:
- Repositorios afetados:
- Decisao inicial em:
- Acao executada:
- Execucao de validacao apos rollback:
- Proxima atualizacao:
```

## Mensagem padrao de incidente
"Rollback same-day iniciado para mudanca central <identificador>. Motivo: <gatilho>. Escopo afetado: <repositorios>. Acao imediata: reversao e reexecucao de smoke test no piloto. Nova atualizacao em ate 30 minutos."
