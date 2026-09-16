# Metodologia do N1

## Escopo

Este documento descreve somente a etapa N1: proposta, dataset, análise exploratória e preparação dos dados. Treinamento, validação e avaliação de modelos estão preservados em `n2/` para etapa posterior.

## Problema e target

O problema proposto é estudar a satisfação de clientes a partir de características do atendimento. A classificação conceitual deriva de `Nota_para_o_atendimento_1_a_5`: notas 1, 2 e 3 recebem classe 0 (`Nao-Satisfeito`) e notas 4 e 5 recebem classe 1 (`Satisfeito`). A coluna `Satisfacao` original é auditada, mas não substitui a regra oficial.

Foram encontradas 31 inconsistências entre a nota e o rótulo original: 28 respostas com nota 4 rotuladas como `Nao-Satisfeito`, 2 com nota 5 rotuladas como `Nao-Satisfeito` e 1 com nota 3 rotulada como `Satisfeito`. O CSV bruto não é alterado; o target é derivado em memória.

## Dataset e qualidade

A fonte canônica é `data/raw/dataset_satisfacao_atendimento.csv`, com 207 respostas e 11 colunas. A auditoria atual encontrou zero valores ausentes, zero linhas duplicadas, zero IDs duplicados e somente notas válidas de 1 a 5. A descrição das colunas e da origem está em `data/dataset_description.md`.

## Análise exploratória

O notebook `notebooks/01_analise_exploratoria.ipynb` apresenta dimensão, tipos, ausências, duplicatas, distribuição da satisfação derivada, distribuição das notas, estatísticas descritivas e distribuições das principais variáveis. Também gera relações descritivas entre satisfação e faixa etária, canal, resolução, novo contato, cordialidade, facilidade, recompra e tempo de espera.

As interpretações utilizam termos como associação e relação observada. Nenhum gráfico é interpretado como evidência de causalidade.

## Preparação do N1

O notebook `notebooks/02_preparacao_dados.ipynb` valida a fonte, deriva o target e apresenta as features previstas para a etapa futura. As colunas que não devem entrar em um futuro modelo são `ID_Resposta`, `Nota_para_o_atendimento_1_a_5`, `Satisfacao` original e `Voltaria_a_comprar`. Não há train/test split, encoding, treinamento, validação cruzada ou métricas no N1.

## Metodologia proposta para o N2

Em etapa posterior, o grupo poderá usar scikit-learn para construir pipelines com Logistic Regression, Decision Tree e Random Forest. A proposta é comparar os modelos com métricas de classificação e analisar variáveis relevantes. Esses resultados são apenas esperados e não foram produzidos ou apresentados como resultados do N1.

## Ética e limitações

O dataset permanece anonimizado e destinado ao uso acadêmico. Devem ser considerados privacidade, segurança, qualidade dos registros, viés de seleção, tamanho reduzido e representatividade limitada da amostra. As relações observadas não demonstram causalidade. Qualquer uso futuro das previsões exigirá transparência, avaliação humana e monitoramento.
