# Versionamento de Workflows Reutilizaveis

Esta politica define como versionar, publicar e consumir os workflows reutilizaveis deste repositorio.

## Objetivo
- Reduzir risco para repositorios consumidores.
- Permitir rollout e rollback previsiveis.
- Evitar acoplamento direto ao estado corrente da branch principal.

## Artefatos cobertos
- `.github/workflows/ci-reusable.yml`
- `.github/workflows/security-reusable.yml`

## Formato de versao
- Tag imutavel: `vMAJOR.MINOR.PATCH`
- Tag de canal estavel: `vMAJOR`

## Regra de consumo
- Padrao recomendado: consumir por tag estavel de major, por exemplo `@v1`.
- Repositorios com maior criticidade ou janela de mudanca controlada podem consumir por tag imutavel, por exemplo `@v1.0.0`.
- `@main` nao e canal padrao de consumo. Seu uso fica restrito a piloto, validacao antecipada ou experimento controlado com rollback explicito.

## Pre-requisito para onboarding em escala
- O canal estavel de major deve existir antes da criacao em massa de novos repositorios consumidores.
- Enquanto a primeira tag estavel nao for publicada, `@main` deve ser usado apenas em piloto com aprovacao explicita.

## Compatibilidade esperada
- `PATCH`: correcao sem mudanca de contrato esperada para consumidores.
- `MINOR`: evolucao retrocompativel, com novos parametros ou melhorias opcionais.
- `MAJOR`: mudanca potencialmente breaking, com comunicacao explicita e plano de migracao.

## Processo minimo de release
1. Atualizar workflows, documentacao e changelog.
2. Validar a mudanca no piloto com smoke test e evidencias.
3. Publicar a tag imutavel da release, por exemplo `v1.0.0`.
4. Atualizar a tag de canal correspondente, por exemplo `v1`.
5. Comunicar consumidores com impacto, orientacao de adocao e rollback.

## Regras adicionais
- Toda release de workflow central deve ter entrada no changelog.
- Mudanca breaking requer ADR antes do merge.
- Consumidores nao devem depender de forks locais do workflow central.
