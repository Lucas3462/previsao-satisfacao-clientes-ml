# Predição da satisfação de clientes utilizando Machine Learning

## Descrição
Projeto acadêmico de Inteligência Artificial da Universidade Presbiteriana Mackenzie, seguindo a Opção Framework. O objetivo é estudar a previsão binária de satisfação a partir de características do atendimento, sem transformar o projeto em uma aplicação operacional.

O relatório estruturado para a entrega do primeiro bimestre está em [reports/relatorio_projeto_n1.md](reports/relatorio_projeto_n1.md).

## Contexto e problema
O problema de pesquisa é: como técnicas de Machine Learning podem prever a satisfação de clientes a partir de características relacionadas ao atendimento? O dataset anonimizado contém 207 respostas coletadas pelo próprio grupo/empresa, conforme a documentação disponível. Participantes, empresa e informações adicionais não estão identificados neste repositório.

## Objetivo
Comparar Logistic Regression, Decision Tree e Random Forest, combinando desempenho preditivo, interpretabilidade e avaliação estatística cautelosa.

## Dataset e variáveis
A fonte original está em `Data/dataset_satisfacao_atendimento.csv` e também é disponibilizada em `data/raw/` para a estrutura do projeto. A descrição detalhada está em [data/dataset_description.md](data/dataset_description.md). O target oficial é derivado de `Nota_para_o_atendimento_1_a_5`: notas 1-3 são classe 0 (`Nao-Satisfeito`) e notas 4-5 são classe 1 (`Satisfeito`). A coluna `Satisfacao` original é auditada, mas não é usada como feature.

Features principais: `Faixa_etaria`, `Canal_de_atendimento`, `Tempo_de_espera_minutos`, `Problema_foi_resolvido`, `Precisou_contato_novamente`, `Atendimento_foi_cordial` e `Facilidade_para_resolver_1_a_5`.

Excluídas: `ID_Resposta`, `Nota_para_o_atendimento_1_a_5`, `Satisfacao` original e `Voltaria_a_comprar`. Esta última é analisada exploratoriamente por poder ser consequência da experiência.

## Metodologia
- Inspeção estrutural, tipos, ausências, duplicatas e inconsistências.
- Split 80/20 com `stratify=y` e `random_state=42`.
- `StratifiedKFold` com 5 folds no treino.
- `OneHotEncoder(handle_unknown="ignore")` para categóricas.
- `StandardScaler` apenas no pipeline da regressão logística.
- Sem SMOTE ou oversampling automático.
- Métricas: accuracy, precision, recall, F1, matriz de confusão e classification report.

## Qualidade dos dados

Na auditoria da execução atual, a base possui 207 linhas, não possui valores ausentes, não possui linhas duplicadas e não possui IDs duplicados. Foram encontradas 31 divergências entre a coluna `Satisfacao` fornecida no CSV e o target calculado pela regra oficial. Essas divergências são reportadas, mas a coluna original não influencia o treinamento.

## Estrutura

```text
Data/                         fonte original preservada
 data/raw/                    cópia organizada da fonte
notebooks/                    quatro etapas executáveis
src/                          funções reutilizáveis
results/figures/              gráficos gerados
results/metrics/              métricas, relatórios e importâncias
results/models/               pipelines treinados
 docs/metodologia.md          decisões metodológicas
reports/relatorio_projeto_n1.md relatório da entrega do primeiro bimestre
run_project.py                execução ponta a ponta
```

## Instalação e execução

```bash
python -m pip install -r requirements.txt
python run_project.py
```

Para abrir os notebooks:

```bash
jupyter notebook notebooks/
```

Os notebooks podem ser executados em ordem: análise exploratória, preparação, modelagem e avaliação. O script principal é a forma mais direta de reproduzir todos os artefatos.

### Finalidade dos notebooks

1. `01_analise_exploratoria.ipynb`: inspeção estrutural, qualidade, distribuições e relações com satisfação.
2. `02_preparacao_dados.ipynb`: criação do target, separação de `X` e `y` e auditoria de leakage.
3. `03_modelagem.ipynb`: split estratificado e treinamento dos três pipelines.
4. `04_avaliacao_modelos.ipynb`: validação cruzada, métricas, matrizes de confusão e importâncias.

## Resultados
Os resultados abaixo foram calculados pelo pipeline atual e também estão disponíveis em `results/metrics/comparacao_modelos.csv`:

| Modelo | Accuracy | Precision | Recall | F1 | F1 médio na CV |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0,929 | 0,941 | 0,970 | 0,955 | 0,904 |
| Decision Tree | 0,810 | 0,903 | 0,848 | 0,875 | 0,860 |
| Random Forest | 0,833 | 0,933 | 0,848 | 0,889 | 0,885 |

Esses números dependem do split fixo e não devem ser generalizados para toda a população. A regressão logística apresentou o maior F1 no teste e na média da validação cruzada nesta execução, mas a conclusão deve considerar os desvios, o tamanho da amostra e o objetivo da análise. Consulte também `classification_reports.json`, os CSVs de importância e as figuras geradas.

## Limitações e ética
A amostra de 207 registros é pequena e não necessariamente representa toda a população de clientes. Devem ser considerados privacidade, anonimização, segurança de acesso, qualidade dos dados, viés amostral, transparência e risco de interpretação incorreta. O modelo é experimental/acadêmico: suas previsões não são decisões definitivas sobre clientes e qualquer uso requer avaliação humana, revisão metodológica e monitoramento.

## Integrantes
Alan Ribeiro do Carmo (RA 10428496), Jean Pazzini Domingues (RA 10428555), Wendell Rodrigues da Costa (RA 10420319) e Leandro Zerbinatti (RA não informado no ambiente; professor/orientador na documentação original).

## Referências
- Documentação do projeto: `Doc/Documentação Projeto IA V.1.doc`.
- Relatório acadêmico completo: [reports/relatorio_projeto_n1.md](reports/relatorio_projeto_n1.md).
- Documentação oficial do pandas, Matplotlib, scikit-learn e Jupyter.
