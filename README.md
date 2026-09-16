# N1 - Proposta e análise exploratória da satisfação de clientes

## Descrição
Este repositório encontra-se exclusivamente na etapa **N1 (primeiro bimestre)** do projeto da disciplina de Inteligência Artificial da Universidade Presbiteriana Mackenzie. A entrega contém proposta, dataset, análise exploratória e preparação dos dados. O desenvolvimento preditivo pertence ao N2 e está preservado separadamente em [n2](n2).

O relatório da entrega está em [docs/relatorio_projeto_n1.md](docs/relatorio_projeto_n1.md).

## Contexto e problema
O problema de pesquisa é: como técnicas de Machine Learning podem prever a satisfação de clientes a partir de características relacionadas ao atendimento? O dataset anonimizado contém 207 respostas coletadas pelo próprio grupo/empresa, conforme a documentação disponível. Participantes, empresa e informações adicionais não estão identificados neste repositório.

## Objetivo
Propor uma análise de satisfação baseada em dados de atendimento, compreender a qualidade da base, preparar o target conceitualmente e documentar a metodologia que será desenvolvida no N2.

## Opção do projeto
**Opção Framework:** o N2 futuro utilizará scikit-learn para classificação supervisionada. Nesta entrega N1 não há treinamento, métricas ou resultados preditivos.

## Dataset e variáveis
A fonte canônica está em `data/raw/dataset_satisfacao_atendimento.csv`. A descrição detalhada está em [data/dataset_description.md](data/dataset_description.md). O target oficial é derivado de `Nota_para_o_atendimento_1_a_5`: notas 1-3 são classe 0 (`Nao-Satisfeito`) e notas 4-5 são classe 1 (`Satisfeito`). A coluna `Satisfacao` original é auditada, mas não é usada como feature.

Features principais: `Faixa_etaria`, `Canal_de_atendimento`, `Tempo_de_espera_minutos`, `Problema_foi_resolvido`, `Precisou_contato_novamente`, `Atendimento_foi_cordial` e `Facilidade_para_resolver_1_a_5`.

Excluídas: `ID_Resposta`, `Nota_para_o_atendimento_1_a_5`, `Satisfacao` original e `Voltaria_a_comprar`. Esta última é analisada exploratoriamente por poder ser consequência da experiência.

## Metodologia do N1
- Inspeção estrutural, tipos, ausências, duplicatas e inconsistências.
- Carregamento da fonte canônica em `data/raw/`.
- Inspeção estrutural, tipos, ausências, duplicatas e valores válidos.
- Derivação conceitual de `Satisfacao` a partir da nota de atendimento.
- Estatísticas descritivas, distribuições e cruzamentos exploratórios.
- Preparação de `X_n1` e `y_n1` sem treinamento ou avaliação preditiva.

## Qualidade dos dados

Na auditoria da execução atual, a base possui 207 linhas, não possui valores ausentes, não possui linhas duplicadas e não possui IDs duplicados. Foram encontradas 31 divergências entre a coluna `Satisfacao` fornecida no CSV e o target calculado pela regra oficial. Essas divergências são reportadas, mas a coluna original não influencia o treinamento.

## Estrutura

```text
data/raw/                     fonte canônica do dataset
data/dataset_description.md   descrição e dicionário de dados
notebooks/                    notebooks exclusivamente N1
src/                          código da EDA e preparação N1
results/                      gráficos e dados processados N1
docs/                         relatório e metodologia N1
n2/                           material futuro preservado, fora do N1
run_project.py                execução da EDA e preparação N1
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

Os notebooks N1 podem ser executados em ordem: análise exploratória e preparação. O script principal reproduz somente esses artefatos.

### Finalidade dos notebooks

1. `01_analise_exploratoria.ipynb`: inspeção estrutural, qualidade, distribuições e relações com satisfação.
2. `02_preparacao_dados.ipynb`: criação do target, separação de `X` e `y` e auditoria de leakage.
3. O material de modelagem e avaliação foi preservado em `n2/notebooks/` e não integra esta entrega.

## Resultados esperados
O N1 não apresenta desempenho de Machine Learning. Para o N2, espera-se desenvolver modelos de classificação, comparar as abordagens, avaliar métricas e identificar variáveis relacionadas à previsão. Esses resultados ainda não fazem parte desta entrega.

## Limitações e ética
A amostra de 207 registros é pequena e não necessariamente representa toda a população de clientes. Devem ser considerados privacidade, anonimização, segurança de acesso, qualidade dos dados, viés amostral, transparência e risco de interpretação incorreta. O modelo é experimental/acadêmico: suas previsões não são decisões definitivas sobre clientes e qualquer uso requer avaliação humana, revisão metodológica e monitoramento.

## Integrantes
Alan Ribeiro do Carmo (RA 10428496), Jean Pazzini Domingues (RA 10428555) e Wendell Rodrigues da Costa (RA 10420319).

Docente/orientador identificado na documentação original: Leandro Zerbinatti, leandro.zerbinatti@mackenzie.br. O RA dele não é aplicável ou não foi informado como integrante discente.

## Referências
- Documentação acadêmica fornecida: [Doc/trab_IA.docx](Doc/trab_IA.docx).
- Relatório acadêmico completo: [docs/relatorio_projeto_n1.md](docs/relatorio_projeto_n1.md).
- Documentação oficial do pandas, Matplotlib, scikit-learn e Jupyter.
