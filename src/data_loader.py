# Integrantes: Alan Ribeiro do Carmo (10428496), Jean Pazzini Domingues (10428555) e Wendell Rodrigues da Costa (10420319).
# Docente/orientador: Leandro Zerbinatti (leandro.zerbinatti@mackenzie.br).
# Síntese: carregamento, validação e criação do target a partir do dataset.
# Histórico:
# Data | Autor | Alteração
# 2026-09-15 | GitHub Copilot | Implementação e auditoria do carregamento e target do N1.

from pathlib import Path
from typing import Dict, Tuple
import pandas as pd

TARGET = "Satisfacao"
RATING = "Nota_para_o_atendimento_1_a_5"
FEATURES = [
    "Faixa_etaria", "Canal_de_atendimento", "Tempo_de_espera_minutos",
    "Problema_foi_resolvido", "Precisou_contato_novamente",
    "Atendimento_foi_cordial", "Facilidade_para_resolver_1_a_5",
]
EXCLUDED = ["ID_Resposta", RATING, TARGET, "Voltaria_a_comprar"]
REQUIRED_COLUMNS = ["ID_Resposta", *FEATURES, RATING, "Voltaria_a_comprar", TARGET]


def load_dataset(path: str | Path) -> pd.DataFrame:
    """Carrega o CSV e verifica a presença das colunas previstas."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset não encontrado: {path}")
    data = pd.read_csv(path)
    missing = [column for column in REQUIRED_COLUMNS if column not in data.columns]
    if missing:
        raise ValueError(f"Colunas ausentes no dataset: {missing}")
    return data


def expected_target(rating: pd.Series) -> pd.Series:
    """Converte notas 1-3 em 0 e notas 4-5 em 1."""
    numeric = pd.to_numeric(rating, errors="coerce")
    if numeric.isna().any() or not numeric.isin([1, 2, 3, 4, 5]).all():
        raise ValueError("A nota deve conter somente valores inteiros de 1 a 5.")
    return numeric.map(lambda value: 1 if value >= 4 else 0).astype("int64")


def validate_and_create_target(data: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, object]]:
    """Valida qualidade básica e cria o target oficial sem usar a coluna original."""
    result = data.copy()
    derived = expected_target(result[RATING])
    expected_labels = derived.map({0: "Nao-Satisfeito", 1: "Satisfeito"})
    inconsistencies = result[TARGET].astype(str).ne(expected_labels)
    report = {
        "shape": list(result.shape),
        "missing_values": result.isna().sum().to_dict(),
        "duplicate_rows": int(result.duplicated().sum()),
        "duplicate_ids": int(result["ID_Resposta"].duplicated().sum()),
        "target_inconsistencies": int(inconsistencies.sum()),
        "target_original_values": sorted(result[TARGET].dropna().unique().tolist()),
    }
    result[TARGET] = derived
    return result, report


def split_features_target(data: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    """Retorna somente as features autorizadas e o target derivado."""
    x = data[FEATURES].copy()
    y = data[TARGET].copy()
    forbidden = set(EXCLUDED).intersection(x.columns)
    if forbidden:
        raise AssertionError(f"Data leakage detectado: {forbidden}")
    if set(y.unique()) != {0, 1}:
        raise AssertionError("O target deve possuir exatamente as classes 0 e 1.")
    return x, y
