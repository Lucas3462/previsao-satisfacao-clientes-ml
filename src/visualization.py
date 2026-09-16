# Integrantes: Alan Ribeiro do Carmo (10428496), Jean Pazzini Domingues (10428555) e Wendell Rodrigues da Costa (10420319).
# Docente/orientador: Leandro Zerbinatti (leandro.zerbinatti@mackenzie.br).
# Síntese: gráficos exploratórios da base e relações descritivas com a satisfação.
# Histórico:
# Data | Autor | Alteração
# 2026-09-15 | GitHub Copilot | Restrição do módulo ao escopo N1.

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def _save(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=160, bbox_inches="tight")
    plt.close()


def _bar_counts(series: pd.Series, title: str, path: Path):
    counts = series.value_counts().sort_index()
    ax = counts.plot(kind="bar", figsize=(8, 4), color="#287d7c")
    ax.set_title(title)
    ax.set_ylabel("Quantidade")
    ax.set_xlabel(series.name)
    _save(path)


def plot_exploration(data: pd.DataFrame, output: Path):
    """Gera visualizações descritivas exigidas na etapa N1."""
    output.mkdir(parents=True, exist_ok=True)
    _bar_counts(data["Satisfacao"].map({0: "Nao-Satisfeito", 1: "Satisfeito"}), "Distribuicao da satisfacao derivada", output / "distribuicao_satisfacao.png")
    _bar_counts(data["Nota_para_o_atendimento_1_a_5"], "Distribuicao da nota de atendimento", output / "distribuicao_notas.png")
    _bar_counts(data["Tempo_de_espera_minutos"], "Distribuicao do tempo de espera", output / "distribuicao_tempo_espera.png")
    categorical = [
        "Faixa_etaria", "Canal_de_atendimento", "Problema_foi_resolvido",
        "Precisou_contato_novamente", "Atendimento_foi_cordial",
        "Facilidade_para_resolver_1_a_5", "Voltaria_a_comprar",
    ]
    for column in categorical:
        _bar_counts(data[column], f"Distribuicao de {column}", output / f"distribuicao_{column.lower()}.png")
        table = pd.crosstab(data[column], data["Satisfacao"], normalize="index").rename(columns={0: "Nao-Satisfeito", 1: "Satisfeito"})
        ax = table.plot(kind="bar", figsize=(8, 4), color=["#c95c54", "#287d7c"])
        ax.set_ylabel("Proporcao dentro da categoria")
        ax.set_title(f"Satisfacao por {column}")
        ax.legend(title="Classe")
        _save(output / f"satisfacao_por_{column.lower()}.png")
    plt.figure(figsize=(8, 4))
    data.boxplot(column="Tempo_de_espera_minutos", by="Satisfacao")
    plt.suptitle("")
    plt.title("Tempo de espera por classe de satisfacao")
    plt.xlabel("Satisfacao (0 = nao, 1 = sim)")
    _save(output / "tempo_espera_por_satisfacao.png")
