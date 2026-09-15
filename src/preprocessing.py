# Integrantes: Alan Ribeiro do Carmo (10428496), Jean Pazzini Domingues (10428555), Wendell Rodrigues da Costa (10420319) e Leandro Zerbinatti (RA não informado no ambiente).
# Síntese: construção dos preprocessadores e pipelines dos três modelos.
# Histórico:
# Data | Autor | Alteração
# 2026-09-15 | GitHub Copilot | Implementação dos preprocessadores e pipelines.

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from .data_loader import FEATURES

NUMERIC_FEATURES = ["Tempo_de_espera_minutos", "Facilidade_para_resolver_1_a_5"]
CATEGORICAL_FEATURES = [feature for feature in FEATURES if feature not in NUMERIC_FEATURES]


def make_preprocessor(scale_numeric: bool) -> ColumnTransformer:
    numeric_transformer = Pipeline([("scaler", StandardScaler())]) if scale_numeric else "passthrough"
    try:
        encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    except TypeError:
        encoder = OneHotEncoder(handle_unknown="ignore", sparse=False)
    return ColumnTransformer([
        ("numeric", numeric_transformer, NUMERIC_FEATURES),
        ("categorical", encoder, CATEGORICAL_FEATURES),
    ])


def make_pipelines(random_state: int = 42) -> dict[str, Pipeline]:
    """Cria pipelines com ajuste do preprocessing restrito ao treino."""
    return {
        "Logistic Regression": Pipeline([
            ("preprocessor", make_preprocessor(True)),
            ("classifier", LogisticRegression(max_iter=1000, random_state=random_state)),
        ]),
        "Decision Tree": Pipeline([
            ("preprocessor", make_preprocessor(False)),
            ("classifier", DecisionTreeClassifier(max_depth=4, random_state=random_state)),
        ]),
        "Random Forest": Pipeline([
            ("preprocessor", make_preprocessor(False)),
            ("classifier", RandomForestClassifier(n_estimators=300, random_state=random_state, n_jobs=-1)),
        ]),
    }
