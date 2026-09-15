# Integrantes: Alan Ribeiro do Carmo (10428496), Jean Pazzini Domingues (10428555), Wendell Rodrigues da Costa (10420319) e Leandro Zerbinatti (RA não informado no ambiente).
# Síntese: execução completa e reproduzível da análise e modelagem.
# Histórico:
# Data | Autor | Alteração
# 2026-09-15 | GitHub Copilot | Execução reprodutível do projeto completo.

from pathlib import Path
import json
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from src.data_loader import load_dataset, validate_and_create_target, split_features_target
from src.models import build_models
from src.evaluation import cross_validate_models, evaluate_models, model_importance, save_json
from src.visualization import plot_exploration, plot_metrics, plot_confusion_matrices, plot_tree_model

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "Data" / "dataset_satisfacao_atendimento.csv"
RESULTS = ROOT / "results"
RANDOM_STATE = 42


def main():
    data = load_dataset(DATA)
    data, quality = validate_and_create_target(data)
    x, y = split_features_target(data)
    RESULTS.joinpath("metrics").mkdir(parents=True, exist_ok=True)
    RESULTS.joinpath("models").mkdir(parents=True, exist_ok=True)
    save_json(quality, RESULTS / "metrics" / "quality_report.json")
    data.to_csv(RESULTS / "metrics" / "dataset_preparado.csv", index=False)
    plot_exploration(data, RESULTS / "figures")
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y, random_state=RANDOM_STATE)
    models = build_models(RANDOM_STATE)
    cv = cross_validate_models(models, x_train, y_train, RANDOM_STATE)
    metrics, fitted, reports = evaluate_models(models, x_train, x_test, y_train, y_test)
    comparison = metrics.merge(cv, on="modelo")
    comparison.to_csv(RESULTS / "metrics" / "comparacao_modelos.csv", index=False)
    save_json(reports, RESULTS / "metrics" / "classification_reports.json")
    plot_metrics(metrics, RESULTS / "figures")
    plot_confusion_matrices(reports, RESULTS / "figures")
    plot_tree_model(fitted["Decision Tree"], RESULTS / "figures")
    for name, model in fitted.items():
        safe_name = name.lower().replace(" ", "_")
        joblib.dump(model, RESULTS / "models" / f"{safe_name}.joblib")
        model_importance(model).to_csv(RESULTS / "metrics" / f"importancia_{safe_name}.csv", index=False)
    print("Execucao concluida.")
    print(comparison.to_string(index=False))
    print(f"Inconsistencias do target original: {quality['target_inconsistencies']}")


if __name__ == "__main__":
    main()
