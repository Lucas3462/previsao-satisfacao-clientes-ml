# Integrantes: Alan Ribeiro do Carmo (10428496), Jean Pazzini Domingues (10428555) e Wendell Rodrigues da Costa (10420319).
# Docente/orientador: Leandro Zerbinatti (leandro.zerbinatti@mackenzie.br).
# Síntese: validação cruzada, métricas e interpretação dos modelos.
# Histórico:
# Data | Autor | Alteração
# 2026-09-15 | GitHub Copilot | Implementação das métricas, validação e interpretação.

from pathlib import Path
import json
import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from sklearn.model_selection import StratifiedKFold, cross_validate


def cross_validate_models(models, x_train, y_train, random_state=42) -> pd.DataFrame:
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=random_state)
    rows = []
    scoring = {"accuracy": "accuracy", "precision": "precision", "recall": "recall", "f1": "f1"}
    for name, model in models.items():
        scores = cross_validate(model, x_train, y_train, cv=cv, scoring=scoring, n_jobs=-1)
        row = {"modelo": name}
        for metric in scoring:
            row[f"cv_{metric}_media"] = scores[f"test_{metric}"].mean()
            row[f"cv_{metric}_desvio"] = scores[f"test_{metric}"].std()
        rows.append(row)
    return pd.DataFrame(rows)


def evaluate_models(models, x_train, x_test, y_train, y_test):
    results, fitted, reports = [], {}, {}
    for name, model in models.items():
        estimator = clone(model).fit(x_train, y_train)
        prediction = estimator.predict(x_test)
        results.append({
            "modelo": name,
            "accuracy": accuracy_score(y_test, prediction),
            "precision": precision_score(y_test, prediction, zero_division=0),
            "recall": recall_score(y_test, prediction, zero_division=0),
            "f1": f1_score(y_test, prediction, zero_division=0),
        })
        fitted[name] = estimator
        reports[name] = {
            "confusion_matrix": confusion_matrix(y_test, prediction).tolist(),
            "classification_report": classification_report(y_test, prediction, target_names=["Nao-Satisfeito", "Satisfeito"], zero_division=0, output_dict=True),
        }
    return pd.DataFrame(results), fitted, reports


def transformed_feature_names(model) -> np.ndarray:
    return model.named_steps["preprocessor"].get_feature_names_out()


def model_importance(model) -> pd.DataFrame:
    classifier = model.named_steps["classifier"]
    names = transformed_feature_names(model)
    if hasattr(classifier, "coef_"):
        values = classifier.coef_[0]
        column = "coeficiente"
    else:
        values = classifier.feature_importances_
        column = "importancia"
    return pd.DataFrame({"feature": names, column: values}).sort_values(column, key=np.abs, ascending=False)


def save_json(value, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
