# Predição da satisfação de clientes a partir de características do atendimento utilizando Machine Learning

## 1. Título

**Predição da satisfação de clientes a partir de características do atendimento utilizando Machine Learning**

## 2. Integrantes

| Integrante | E-mail | RA |
|---|---|---|
| Alan Ribeiro do Carmo | 10428496@mackenzista.com.br | 10428496 |
| Jean Pazzini Domingues | 10428555@mackenzista.com.br | 10428555 |
| Wendell Rodrigues da Costa | 10420319@mackenzista.com.br | 10420319 |

Docente/orientador identificado na documentação original: Leandro Zerbinatti, leandro.zerbinatti@mackenzie.br.

## 3. Resumo

Este projeto propõe analisar a satisfação de clientes a partir de características de atendimento. O N1 utiliza um dataset original coletado por questionário, com 207 respostas anonimizadas, e realiza inspeção, análise exploratória e preparação dos dados. A satisfação é classificada conceitualmente pela nota do atendimento: notas de 1 a 3 correspondem a `Nao-Satisfeito` e notas 4 ou 5 correspondem a `Satisfeito`. Foram encontradas 31 inconsistências entre a coluna de satisfação fornecida e a classificação derivada da nota. O N1 não apresenta treinamento nem desempenho de modelos; esses resultados são esperados para o N2.

## 4. Introdução

### 4.1 Contextualização

A satisfação é um indicador relevante para compreender a experiência de atendimento. Aspectos como canal, tempo de espera, resolução do problema, necessidade de novo contato, cordialidade e facilidade para resolver a demanda podem estar relacionados às avaliações dos clientes. A Inteligência Artificial pode apoiar a identificação de padrões em dados históricos, respeitando os limites da amostra [1].

### 4.2 Justificativa

A análise exploratória permite compreender a qualidade da base, identificar relações descritivas e preparar uma proposta de solução reproduzível. O trabalho é aderente à Opção Framework porque prevê o uso de ferramentas de Machine Learning no desenvolvimento posterior [2].

### 4.3 Objetivo

Realizar a proposta, auditoria, análise exploratória e preparação inicial dos dados de satisfação, deixando documentada a metodologia que poderá ser aplicada no N2.

### 4.4 Opção do projeto

**Opção Framework:** utilização futura de scikit-learn para classificação supervisionada. No N1, a entrega está limitada à análise dos dados e à preparação necessária.

## 5. Descrição do problema

A pergunta de pesquisa é: **como características relacionadas ao atendimento podem ser analisadas para apoiar uma futura previsão da satisfação de clientes?**

A regra conceitual do target é:

- notas 1, 2 e 3: classe 0, `Nao-Satisfeito`;
- notas 4 e 5: classe 1, `Satisfeito`.

Para uma etapa futura, as variáveis previstas são `Faixa_etaria`, `Canal_de_atendimento`, `Tempo_de_espera_minutos`, `Problema_foi_resolvido`, `Precisou_contato_novamente`, `Atendimento_foi_cordial` e `Facilidade_para_resolver_1_a_5`. Não entram como features `ID_Resposta`, `Nota_para_o_atendimento_1_a_5`, `Satisfacao` original e `Voltaria_a_comprar`.

## 6. Aspectos éticos e responsabilidade

O dataset permanece anonimizado e destinado ao uso acadêmico. A variável `ID_Resposta` é apenas técnica e não é usada como entrada. Devem ser considerados privacidade, segurança, qualidade dos registros, viés de seleção, transparência e risco de interpretações incorretas.

A amostra possui 207 respostas e pode não representar toda a população de clientes. As relações observadas na EDA são descritivas e não demonstram causalidade. Qualquer uso futuro de previsões exigirá avaliação humana, transparência, monitoramento e revisão dos possíveis impactos.

## 7. Dataset, análise exploratória e preparação

### 7.1 Origem e conteúdo

O dataset foi coletado pelo próprio grupo/negócio por meio de questionário, conforme a documentação acadêmica original [1]. A fonte canônica é `data/raw/dataset_satisfacao_atendimento.csv`, com 207 registros e 11 colunas. A descrição detalhada está em [data/dataset_description.md](../data/dataset_description.md).

### 7.2 Auditoria de qualidade

A auditoria encontrou zero valores ausentes, zero linhas duplicadas, zero IDs duplicados e somente notas válidas de 1 a 5. Foram identificadas 31 inconsistências entre `Satisfacao` e a regra oficial:

- 28 respostas com nota 4 rotuladas como `Nao-Satisfeito`;
- 2 respostas com nota 5 rotuladas como `Nao-Satisfeito`;
- 1 resposta com nota 3 rotulada como `Satisfeito`.

O CSV bruto não é alterado. A classificação é derivada em memória para a análise.

### 7.3 Análise exploratória

O notebook `01_analise_exploratoria.ipynb` apresenta dimensão, tipos, valores ausentes, duplicatas, distribuição das classes derivadas, distribuição das notas, estatísticas descritivas e distribuições das principais variáveis. Também analisa relações observadas entre satisfação e faixa etária, canal, resolução, novo contato, cordialidade, facilidade, recompra e tempo de espera.

### 7.4 Preparação

O notebook `02_preparacao_dados.ipynb` valida a fonte canônica, cria o target conceitual e confirma as features previstas para o futuro. Não realiza divisão treino/teste, encoding, treinamento, validação cruzada ou cálculo de métricas.

## 8. Metodologia e resultados esperados

No N1, a metodologia inclui carregamento, inspeção, validação, análise exploratória e preparação em Python. O código é modularizado em `src/`, e `run_project.py` executa somente essa etapa.

No N2, espera-se desenvolver modelos de classificação, comparar abordagens, avaliar métricas e identificar variáveis relacionadas à previsão. Esses resultados ainda não foram apresentados nesta entrega e não há conclusão baseada em desempenho de modelos.

## 9. Referências

[1] RIBEIRO DO CARMO, A.; DOMINGUES, J. P.; COSTA, W. R.; ZERBINATTI, L. *Documentação acadêmica do projeto*. Documento fornecido em [Doc/trab_IA.docx](../Doc/trab_IA.docx), 2026.

[2] PEDREGOSA, F. et al. Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research*, v. 12, p. 2825-2830, 2011. Disponível em: https://scikit-learn.org/. Acesso em: 15 set. 2026.

## 10. Bibliografia

- MCKINNEY, W. *Python for Data Analysis*. O'Reilly Media.
- VANDERPLAS, J. *Python Data Science Handbook*. O'Reilly Media.
- Documentação oficial do pandas: https://pandas.pydata.org/docs/.
- Documentação oficial do Matplotlib: https://matplotlib.org/stable/.
- Documentação oficial do scikit-learn: https://scikit-learn.org/stable/.
