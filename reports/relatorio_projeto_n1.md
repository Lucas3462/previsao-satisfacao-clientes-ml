# Predição da satisfação de clientes a partir de características do atendimento utilizando Machine Learning

## 1. Título

**Predição da satisfação de clientes a partir de características do atendimento utilizando Machine Learning**

## 2. Integrantes

| Integrante | E-mail | RA |
|---|---|---|
| Alan Ribeiro do Carmo | 10428496@mackenzista.com.br | 10428496 |
| Jean Pazzini Domingues | 10428555@mackenzista.com.br | 10428555 |
| Wendell Rodrigues da Costa | 10420319@mackenzista.com.br | 10420319 |
| Leandro Zerbinatti | leandro.zerbinatti@mackenzie.br | Não informado no ambiente; professor/orientador na documentação original |

A composição acima foi transcrita da documentação acadêmica existente no repositório. O grupo discente identificado possui três alunos; a especificação da disciplina exige grupos de no mínimo três e no máximo quatro alunos.

## 3. Resumo

Este projeto aplica técnicas de Machine Learning para estudar a previsão da satisfação de clientes a partir de características de atendimento. O trabalho utiliza um dataset original coletado por questionário, com 207 respostas anonimizadas. O problema é tratado como classificação binária: notas de 1 a 3 representam `Nao-Satisfeito` e notas 4 ou 5 representam `Satisfeito`. São comparados Logistic Regression, Decision Tree e Random Forest, usando pipelines do scikit-learn, divisão estratificada, validação cruzada e métricas de classificação. A coluna de satisfação fornecida no CSV é auditada, mas o target utilizado é obrigatoriamente derivado da nota. Foram encontradas 31 inconsistências entre os dois campos. Os resultados são experimentais e não devem ser generalizados para toda a população de clientes.

## 4. Introdução

### 4.1 Contextualização

A satisfação é um indicador relevante para compreender a experiência de atendimento. Aspectos como canal, tempo de espera, resolução do problema, necessidade de novo contato, cordialidade e facilidade para resolver a demanda podem estar relacionados às avaliações atribuídas pelos clientes. A Inteligência Artificial pode apoiar a identificação de padrões em dados históricos, desde que sejam respeitados os limites do conjunto de dados e da interpretação estatística [1].

### 4.2 Justificativa

A análise de respostas de atendimento pode ser trabalhosa quando realizada somente de forma manual. Um modelo classificatório permite organizar uma análise experimental dos padrões presentes na base e comparar abordagens com diferentes níveis de interpretabilidade. O projeto é aderente à Opção Framework porque emprega scikit-learn para classificação supervisionada [2].

### 4.3 Objetivo

Desenvolver e comparar modelos capazes de prever a classe de satisfação a partir exclusivamente de características relacionadas ao atendimento, evitando o uso de variáveis que revelem diretamente o target ou que representem possíveis consequências da experiência.

### 4.4 Opção do projeto

**Opção Framework:** uso de scikit-learn para preparação, treinamento, avaliação e interpretação de modelos de Machine Learning.

## 5. Descrição do problema

A pergunta de pesquisa é: **como técnicas de Machine Learning podem prever a satisfação de clientes a partir de características relacionadas ao atendimento?**

A variável-alvo oficial é `Satisfacao`, derivada de `Nota_para_o_atendimento_1_a_5`:

- notas 1, 2 e 3: classe 0, `Nao-Satisfeito`;
- notas 4 e 5: classe 1, `Satisfeito`.

O modelo utiliza como preditores `Faixa_etaria`, `Canal_de_atendimento`, `Tempo_de_espera_minutos`, `Problema_foi_resolvido`, `Precisou_contato_novamente`, `Atendimento_foi_cordial` e `Facilidade_para_resolver_1_a_5`. São excluídos `ID_Resposta`, a nota que origina o target, `Satisfacao` original e `Voltaria_a_comprar`.

## 6. Ética e responsabilidade

O dataset deve permanecer anonimizado e ser tratado com controles de acesso compatíveis com sua finalidade acadêmica. A variável `ID_Resposta` não é usada como preditor e nenhum dado pessoal adicional foi incluído no modelo. A qualidade dos dados é uma preocupação central: a coluna `Satisfacao` original possui 31 divergências em relação à regra formal do projeto, por isso o target é recalculado e a inconsistência é reportada.

A amostra pode conter viés de seleção, pois foi obtida por coleta própria e possui apenas 207 respostas. As associações encontradas não demonstram causalidade. O modelo é experimental e acadêmico; suas previsões não devem determinar tratamento, prioridade ou decisão definitiva sobre clientes. Qualquer uso futuro exigiria avaliação humana, transparência sobre as limitações, monitoramento de desempenho e revisão de possíveis impactos discriminatórios.

## 7. Dataset, análise exploratória e preparação

### 7.1 Origem e conteúdo

O dataset foi coletado pelo próprio grupo/negócio por meio de questionário, conforme a documentação acadêmica original [1]. A base presente em `data/raw/dataset_satisfacao_atendimento.csv` contém 207 registros e 11 colunas. A descrição detalhada está em [data/dataset_description.md](../data/dataset_description.md). Não foram inventadas informações sobre empresa, período ou participantes além do que consta na documentação disponível.

### 7.2 Auditoria de qualidade

A execução atual encontrou:

- 207 linhas e 11 colunas;
- zero valores ausentes;
- zero linhas duplicadas;
- zero IDs duplicados;
- 31 divergências entre `Satisfacao` original e o target derivado;
- target derivado com as classes 0 e 1.

### 7.3 Análise exploratória

O notebook `01_analise_exploratoria.ipynb` avalia dimensão, tipos, ausências, duplicatas, distribuição do target, faixa etária, canais, tempo de espera, resolução, novo contato, cordialidade, facilidade, notas e intenção de nova compra. Também gera cruzamentos de satisfação por essas variáveis e o gráfico de tempo de espera por classe. Os gráficos são salvos em `results/figures/`.

### 7.4 Preparação

O notebook `02_preparacao_dados.ipynb` deriva o target, separa `X` e `y` e confirma que nenhuma coluna excluída entra nas features. A divisão entre treino e teste é feita somente depois dessa definição. Variáveis categóricas passam por `OneHotEncoder(handle_unknown="ignore")`; variáveis numéricas permanecem numéricas e recebem `StandardScaler` somente no pipeline da regressão logística.

## 8. Metodologia e resultados esperados

### 8.1 Modelos

1. **Logistic Regression:** baseline e modelo com coeficientes interpretáveis.
2. **Decision Tree:** modelo com representação de decisões e importância de variáveis.
3. **Random Forest:** ensemble de árvores para comparação com o modelo individual.

### 8.2 Avaliação

A base é dividida em 80% para treino e 20% para teste, com `stratify=y` e `random_state=42`. No treinamento é usada validação cruzada estratificada com cinco folds. São calculados accuracy, precision, recall, F1-score, matriz de confusão e `classification_report`. A comparação considera especialmente precision, recall e F1, sem declarar superioridade com base apenas na acurácia.

### 8.3 Resultados observados na execução reproduzível

| Modelo | Accuracy no teste | Precision | Recall | F1 no teste | F1 médio na CV |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0,929 | 0,941 | 0,970 | 0,955 | 0,904 |
| Decision Tree | 0,810 | 0,903 | 0,848 | 0,875 | 0,860 |
| Random Forest | 0,833 | 0,933 | 0,848 | 0,889 | 0,885 |

Esses valores são resultados da divisão fixa e devem ser interpretados com cautela devido ao tamanho da amostra. Nesta execução, a regressão logística apresentou o maior F1 no teste e na média da validação cruzada. Isso é uma descrição do experimento, não uma garantia de desempenho fora da base.

### 8.4 Resultados esperados

Espera-se identificar características associadas à previsão de satisfação, comparar modelos com diferentes níveis de interpretabilidade e produzir uma análise reproduzível. Coeficientes e importâncias serão tratados como contribuições para a previsão, não como relações causais.

## 9. Referências

[1] RIBEIRO DO CARMO, A.; DOMINGUES, J. P.; COSTA, W. R.; ZERBINATTI, L. *Documentação Projeto IA V.1*. Documento acadêmico fornecido no repositório, 2026.

[2] PEDREGOSA, F. et al. Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research*, v. 12, p. 2825-2830, 2011. Disponível em: https://scikit-learn.org/. Acesso em: 15 set. 2026.

## 10. Bibliografia

- MCKINNEY, W. *Python for Data Analysis*. O'Reilly Media.
- VANDERPLAS, J. *Python Data Science Handbook*. O'Reilly Media.
- DOCUMENTAÇÃO oficial do pandas. Disponível em: https://pandas.pydata.org/docs/.
- DOCUMENTAÇÃO oficial do Matplotlib. Disponível em: https://matplotlib.org/stable/.
- DOCUMENTAÇÃO oficial do scikit-learn. Disponível em: https://scikit-learn.org/stable/.
