# Metodologia

## Problema e target

O problema é uma classificação binária da satisfação. O target oficial é derivado de `Nota_para_o_atendimento_1_a_5`: notas 1, 2 e 3 recebem classe 0 (`Nao-Satisfeito`) e notas 4 e 5 recebem classe 1 (`Satisfeito`). A coluna `Satisfacao` original é auditada, mas não é usada como entrada. Na execução da base atual foram encontradas 31 divergências entre a coluna original e a regra oficial; portanto, o modelo usa o target derivado.

## Dados e leakage

As features permitidas são faixa etária, canal, tempo de espera, resolução, novo contato, cordialidade e facilidade de resolução. ID, nota usada para derivar o target, satisfação original e intenção de nova compra ficam fora de `X`. `Voltaria_a_comprar` é explorada por seu interesse analítico, mas pode refletir a própria experiência.

A auditoria atual encontrou 207 registros, zero valores ausentes, zero linhas duplicadas e zero IDs duplicados. A coluna `Satisfacao` original diverge do target oficial em 31 registros; ela é mantida apenas para a auditoria de consistência.

## Validação

O conjunto é dividido em treino e teste na proporção 80/20, com `stratify=y` e `random_state=42`. A comparação durante o treino usa `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`. O preprocessing é parte de cada pipeline e é ajustado somente nos dados recebidos pelo fold de treino.

## Preprocessamento e modelos

Variáveis categóricas usam `OneHotEncoder(handle_unknown="ignore")`. O tempo de espera e a facilidade são numéricos; a Regressão Logística usa `StandardScaler`, enquanto Árvore de Decisão e Random Forest mantêm a escala original. Os três modelos obrigatórios são Logistic Regression, Decision Tree e Random Forest. Não foi aplicado oversampling, pois a distribuição das classes foi inspecionada e não houve justificativa automática para alterar a amostra.

## Avaliação e interpretação

São calculados accuracy, precision, recall, F1, matriz de confusão e `classification_report`. A análise combina teste e médias/desvios da validação cruzada. Coeficientes da regressão e importâncias dos modelos de árvore são apresentados com nomes pós-encoding. Associação e importância para previsão não implicam causalidade.

Na execução atual, a Logistic Regression obteve F1 de teste 0,955 e F1 médio de validação cruzada 0,904; a Decision Tree obteve 0,875 e 0,860; e a Random Forest obteve 0,889 e 0,885, respectivamente. Esses valores são descritivos da divisão reproduzível usada e não constituem evidência de desempenho populacional.

## Notebooks e reprodutibilidade

Os notebooks são executáveis em ordem e usam os módulos de `src/`, sem duplicar a lógica principal. Cada célula possui `metadata.id` único e `metadata.language` (`markdown` ou `python`). Os artefatos da execução são salvos em `results/metrics/`, `results/figures/` e `results/models/`. A execução completa pode ser reproduzida com `python run_project.py`.

## Limitações e responsabilidade

São apenas 207 respostas: a amostra é pequena e pode não representar toda a população. O dataset deve permanecer anonimizado. É necessário cuidar de privacidade, controle de acesso, qualidade dos registros e possível viés amostral. O modelo é experimental/acadêmico, não deve definir decisões sobre clientes e requer transparência, avaliação humana e revisão periódica antes de qualquer uso.
