# Integrantes: Alan Ribeiro do Carmo (10428496), Jean Pazzini Domingues (10428555) e Wendell Rodrigues da Costa (10420319).
# Docente/orientador: Leandro Zerbinatti (leandro.zerbinatti@mackenzie.br).
# Síntese: execução reproduzível da análise exploratória e preparação do N1.
# Histórico:
# Data | Autor | Alteração
# 2026-09-15 | GitHub Copilot | Restrição do executor ao escopo N1.

from pathlib import Path
import pandas as pd
from src.data_loader import load_dataset, validate_and_create_target
from src.visualization import plot_exploration

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "raw" / "dataset_satisfacao_atendimento.csv"
RESULTS = ROOT / "results"


def main():
    """Executa somente inspeção, preparação e EDA do primeiro bimestre."""
    data = load_dataset(DATA)
    prepared, quality = validate_and_create_target(data)
    RESULTS.joinpath("metrics").mkdir(parents=True, exist_ok=True)
    RESULTS.joinpath("figures").mkdir(parents=True, exist_ok=True)
    pd.DataFrame({"valor": pd.Series(quality)}).to_csv(RESULTS / "metrics" / "quality_report.csv")
    prepared.to_csv(RESULTS / "metrics" / "dataset_preparado_n1.csv", index=False)
    plot_exploration(prepared, RESULTS / "figures")
    print("Execucao N1 concluida: carga, qualidade, target derivado, preparacao e EDA.")
    print(f"Dimensao: {prepared.shape[0]} linhas x {prepared.shape[1]} colunas")
    print(f"Inconsistencias entre target original e nota: {quality['target_inconsistencies']}")
    print("Distribuicao do target derivado:")
    print(prepared["Satisfacao"].value_counts().sort_index().to_string())


if __name__ == "__main__":
    main()
