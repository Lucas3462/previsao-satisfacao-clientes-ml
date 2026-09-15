# Previsão da Satisfação de Clientes utilizando Machine Learning

Projeto de Inteligência Artificial desenvolvido para aplicar técnicas de Machine Learning na previsão da satisfação de clientes a partir de características relacionadas à experiência de atendimento.

## Sobre o projeto

A qualidade do atendimento pode ser influenciada por diferentes fatores, como tempo de espera, resolução do problema, cordialidade e facilidade para solucionar uma demanda.

Este projeto propõe o desenvolvimento de um modelo de Machine Learning capaz de identificar padrões presentes nesses dados e prever se um cliente pertence à categoria de **satisfeito** ou **insatisfeito**.

Além da previsão, o projeto busca identificar características relacionadas à satisfação dos clientes que possam gerar informações úteis para gestores responsáveis pela experiência e pelo atendimento.

## Objetivo

Desenvolver e avaliar modelos de Machine Learning capazes de prever a satisfação de clientes a partir de características relacionadas ao atendimento.

### Objetivos específicos

- Coletar e organizar dados relacionados à experiência dos clientes;
- Realizar análise exploratória dos dados;
- Identificar possíveis relações entre características do atendimento e satisfação;
- Preparar os dados para aplicação dos algoritmos de Machine Learning;
- Desenvolver modelos de classificação para previsão da satisfação;
- Comparar o desempenho dos modelos utilizando métricas de avaliação;
- Identificar características relevantes para a previsão;
- Avaliar a possibilidade de utilização dos resultados como ferramenta de apoio à gestão.

## Problema de pesquisa

> Como técnicas de Machine Learning podem ser utilizadas para prever a satisfação de clientes a partir de características relacionadas ao atendimento?

## Abordagem

O problema é tratado como uma tarefa de **classificação supervisionada**.

A variável de satisfação é criada a partir da nota atribuída ao atendimento:

| Nota | Classificação |
|------|----------------|
| 1 | Insatisfeito |
| 2 | Insatisfeito |
| 3 | Insatisfeito |
| 4 | Satisfeito |
| 5 | Satisfeito |

A variável-alvo utilizada pelos modelos é denominada `Satisfacao`.

A variável original de nota do atendimento não é utilizada como entrada dos modelos após a criação da variável-alvo, evitando que o modelo tenha acesso direto à informação que deve prever.

## Dataset

O dataset foi obtido por meio de uma coleta própria realizada através de questionário, totalizando **207 respostas**.

A base contém informações relacionadas à experiência dos participantes durante situações de atendimento ao cliente.

### Variáveis

| Variável | Descrição | Tipo |
|----------|-----------|------|
| Faixa etária | Faixa de idade do participante | Categórica |
| Canal de atendimento | Canal utilizado no atendimento | Categórica |
| Tempo de espera | Tempo informado até o atendimento | Categórica |
| Problema foi resolvido? | Indica se o problema apresentado foi solucionado | Binária |
| Precisou entrar em contato novamente? | Indica se houve necessidade de novo contato | Binária |
| Atendimento foi cordial? | Avaliação da cordialidade do atendimento | Categórica/Binária |
| Facilidade para resolver o problema | Percepção sobre a facilidade para solucionar a demanda | Ordinal |
| Nota para o atendimento | Nota atribuída à experiência de atendimento | Numérica/Ordinal |
| Voltaria a comprar da empresa? | Intenção de realizar nova compra | Binária |

A variável **"Voltaria a comprar da empresa?"** será analisada durante a etapa exploratória como possível indicador relacionado à satisfação, mas não será utilizada como principal variável de entrada do modelo.

## Análise exploratória

A análise exploratória será realizada utilizando Python, buscando compreender as características da base e identificar possíveis relações entre as variáveis.

Entre as análises realizadas estão:

- Distribuição dos participantes por faixa etária;
- Distribuição dos canais de atendimento;
- Distribuição dos tempos de espera;
- Proporção de problemas resolvidos;
- Frequência de necessidade de novo contato;
- Avaliação da cordialidade;
- Distribuição da facilidade de resolução;
- Distribuição das notas atribuídas ao atendimento;
- Proporção de clientes que declararam intenção de voltar a comprar;
- Análises cruzadas entre as características do atendimento e a satisfação.

## Pré-processamento

Antes do treinamento dos modelos, os dados serão preparados para utilização nos algoritmos de Machine Learning.

As etapas incluem:

- Verificação de valores ausentes;
- Identificação e tratamento de inconsistências;
- Transformação de variáveis categóricas;
- Codificação de variáveis binárias;
- Aplicação de One-Hot Encoding quando necessário;
- Criação da variável-alvo `Satisfacao`;
- Divisão dos dados em conjuntos de treinamento e teste.

## Modelos de Machine Learning

Inicialmente, serão avaliados três algoritmos de classificação supervisionada:

### Regressão Logística

Utilizada como modelo de referência para o problema de classificação binária.

### Árvore de Decisão

Utilizada pela possibilidade de representar as decisões realizadas pelo modelo de maneira mais interpretável.

### Random Forest

Utilizada por combinar múltiplas árvores de decisão e apresentar potencial para melhorar a capacidade de generalização do modelo.

## Avaliação

Os modelos serão comparados utilizando diferentes métricas de classificação:

- Acurácia;
- Precisão;
- Recall;
- F1-score;
- Matriz de confusão.

A comparação permitirá identificar qual modelo apresenta melhor desempenho para o dataset utilizado.

A análise não será baseada exclusivamente na acurácia, buscando considerar diferentes aspectos do desempenho dos classificadores.

## Tecnologias utilizadas

- **Python** — processamento e análise dos dados;
- **Pandas** — manipulação e organização do dataset;
- **Matplotlib** — visualização dos dados;
- **Scikit-learn** — preparação dos dados, treinamento e avaliação dos modelos;
- **Jupyter Notebook / Google Colab** — desenvolvimento e documentação das análises;
- **GitHub** — versionamento, armazenamento e documentação do projeto.