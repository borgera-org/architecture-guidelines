# Principios de Arquitetura (Nao Negociaveis)

## P1. Seguranca por padrao
Todo componente novo deve nascer com autenticacao, autorizacao e tratamento de segredos fora do codigo.

## P2. Mudanca com rollback
Toda mudanca central deve explicitar criterio de rollback no mesmo dia.

## P3. Evidencia antes de merge
Mudancas com impacto em CI, seguranca ou integracao devem anexar evidencia de smoke test.

## P4. Fonte unica da verdade
Diretrizes arquiteturais devem ser versionadas e auditaveis por PR.

## P5. Nao copiar, referenciar
Workflows e baselines centrais devem ser consumidos por referencia, evitando forks locais.

## P6. Evolucao guiada por risco
Quanto maior o risco da mudanca, maior o nivel de revisao e rastreabilidade.

## P7. Observabilidade minima
Servicos devem emitir logs estruturados suficientes para diagnostico operacional.
