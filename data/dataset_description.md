# Descrição do dataset

## Identificação

- Arquivo: `dataset_satisfacao_atendimento.csv`
- Origem: coleta própria por questionário, conforme a documentação acadêmica do projeto.
- Registros: 207 respostas.
- Anonimização: não há nomes ou identificadores pessoais no conjunto; `ID_Resposta` é apenas um identificador técnico e não é usado como feature prevista.

## Colunas

| Coluna | Papel | Descrição |
|---|---|---|
| `ID_Resposta` | Excluída | Identificador técnico da resposta. |
| `Faixa_etaria` | Feature categórica | Faixa etária informada. |
| `Canal_de_atendimento` | Feature categórica | Canal utilizado no atendimento. |
| `Tempo_de_espera_minutos` | Feature numérica | Tempo de espera informado em minutos. |
| `Problema_foi_resolvido` | Feature categórica | Indica se o problema foi resolvido. |
| `Precisou_contato_novamente` | Feature categórica | Indica necessidade de novo contato. |
| `Atendimento_foi_cordial` | Feature categórica | Avaliação da cordialidade. |
| `Facilidade_para_resolver_1_a_5` | Feature numérica ordinal | Avaliação da facilidade para resolver o problema. |
| `Nota_para_o_atendimento_1_a_5` | Origem do target | Nota de 1 a 5 usada para derivar a classe. |
| `Voltaria_a_comprar` | Exploratória, excluída de futuras features | Intenção de nova compra; pode ser consequência da experiência. |
| `Satisfacao` | Auditoria, excluída de futuras features | Rótulo original fornecido no CSV, validado mas não usado como feature. |

## Regra do target

- Nota 1, 2 ou 3: `Nao-Satisfeito` / classe 0.
- Nota 4 ou 5: `Satisfeito` / classe 1.

A auditoria encontrou 31 divergências entre o rótulo original e a regra oficial. O código do N1 deriva o target em memória e registra a qualidade em `results/metrics/quality_report.csv`.

## Uso responsável

O dataset é destinado à análise acadêmica. A amostra é pequena, pode conter viés de seleção e não representa necessariamente toda a população de clientes. Não usar os resultados para decisões definitivas sem avaliação humana e validação adicional.
