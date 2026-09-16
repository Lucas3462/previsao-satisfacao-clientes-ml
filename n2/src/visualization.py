# Integrantes: Alan Ribeiro do Carmo (10428496), Jean Pazzini Domingues (10428555) e Wendell Rodrigues da Costa (10420319).
# Docente/orientador: Leandro Zerbinatti (leandro.zerbinatti@mackenzie.br).
# Síntese: gráficos exploratórios, métricas e interpretação dos modelos.
# Histórico:
# Data | Autor | Alteração
# 2026-09-15 | GitHub Copilot | Implementação dos gráficos exploratórios e de avaliação.

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import plot_tree


def _save(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=160, bbox_inches="tight")
    plt.close()


def plot_exploration(data: pd.DataFrame, output: Path):
    output.mkdir(parents=True, exist_ok=True)
    categorical = ["Faixa_etaria", "Canal_de_atendimento", "Problema_foi_resolvido", "Precisou_contato_novamente", "Atendimento_foi_cordial", "Facilidade_para_resolver_1_a_5", "Voltaria_a_comprar"]
    for column in categorical:
        table = pd.crosstab(data[column], data["Satisfacao"], normalize="index").rename(columns={0: "Nao-Satisfeito", 1: "Satisfeito"})
        ax = table.plot(kind="bar", figsize=(8, 4), color=["#c95c54", "#287d7c"])
        ax.set_ylabel("Proporcao")
        ax.set_title(f"Satisfacao por {column}")
        ax.legend(title="Classe")
        _save(output / f"satisfacao_por_{column.lower()}.png")
    plt.figure(figsize=(8, 4))
    data.boxplot(column="Tempo_de_espera_minutos", by="Satisfacao")
    plt.suptitle("")
    plt.title("Tempo de espera por classe de satisfacao")
    plt.xlabel("Satisfacao (0 = nao, 1 = sim)")
    _save(output / "tempo_espera_por_satisfacao.png")


def plot_metrics(metrics: pd.DataFrame, output: Path):
    long = metrics.melt(id_vars="modelo", value_vars=["accuracy", "precision", "recall", "f1"], var_name="metrica", value_name="valor")
    ax = long.pivot(index="modelo", columns="metrica", values="valor").plot(kind="bar", figsize=(9, 5), ylim=(0, 1), color=["#1f6f8b", "#99c24d", "#f4a261", "#e76f51"])
    ax.set_ylabel("Valor")
    ax.set_title("Comparacao das metricas no conjunto de teste")
    ax.legend(title="Metrica")
    _save(output / "comparacao_metricas.png")


def plot_confusion_matrices(reports, output: Path):
    for name, report in reports.items():
        matrix = report["confusion_matrix"]
        plt.figure(figsize=(4, 4))
        plt.imshow(matrix, cmap="Blues")
        plt.colorbar()
        plt.xticks([0, 1], ["Nao", "Sim"])
        plt.yticks([0, 1], ["Nao", "Sim"])
        for row in range(2):
            for col in range(2):
                plt.text(col, row, matrix[row][col], ha="center", va="center")
        plt.xlabel("Predito")
        plt.ylabel("Real")
        plt.title(f"Matriz de confusao - {name}")
        _save(output / f"matriz_{name.lower().replace(' ', '_')}.png")


def plot_tree_model(model, output: Path):
    plt.figure(figsize=(20, 10))
    plot_tree(model.named_steps["classifier"], feature_names=model.named_steps["preprocessor"].get_feature_names_out(), class_names=["Nao-Satisfeito", "Satisfeito"], filled=True, rounded=True, max_depth=3, fontsize=7)
    _save(output / "arvore_decisao.png")
