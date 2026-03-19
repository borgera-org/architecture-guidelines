# API .NET Examples

## Proposito

Este diretorio concentra os examples de referencia para o archetype `api-dotnet`.

Ele existe para mostrar como o contrato, os templates e o comportamento esperado do CLI devem se combinar no resultado final de um repositorio consumidor.

## O Que Este Diretorio Representa

Os examples deste diretorio devem representar cenarios concretos e validos de materializacao do archetype `api-dotnet`.

Eles nao substituem:

- [definition.yaml](c:/Users/igors/source/repos/architecture-guidelines/archetypes/api-dotnet/definition.yaml)
- [README.md](c:/Users/igors/source/repos/architecture-guidelines/archetypes/api-dotnet/README.md)
- os templates em `templates/`
- o contrato do CLI em [cli-contract.md](c:/Users/igors/source/repos/architecture-guidelines/docs/cli-contract.md)

Eles existem para tornar o resultado esperado visivel.

## Cenarios Que Fazem Sentido Aqui

Os cenarios mais naturais para este archetype sao:

- API minima com testes e Docker
- API minima sem testes
- API minima sem Docker

Nem todos esses cenarios precisam existir agora. Eles devem surgir apenas quando agregarem valor real de referencia.

## Primeiro Example Recomendado

O primeiro example recomendado para este archetype e:

- `minimal-default`

Razao:

- representa o caminho padrao mais completo do archetype
- ajuda a validar a interacao entre `repository-files`, `dotnet-solution`, `api-project`, `test-project` e `docker-files`
- reduz ambiguidades antes de examples mais especializados

## O Que Um Example Deve Mostrar

Cada example deste diretorio deve deixar claro:

- quais inputs foram usados
- quais templates foram aplicados
- qual estrutura final foi gerada
- quais pos-processamentos o CLI precisou executar

## Regra de Qualidade

Um novo example de `api-dotnet` so deve ser criado quando:

- representar um cenario valido do archetype
- ajudar a validar uma variacao relevante do contrato
- evitar ambiguidade sobre a saida esperada

Se a variacao nao altera entendimento nem validacao do resultado final, ela provavelmente nao precisa existir como example proprio.

## Proximo Passo

O proximo passo esperado neste diretorio e criar o primeiro cenario `minimal-default`.
