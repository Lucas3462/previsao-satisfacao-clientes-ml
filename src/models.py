# Integrantes: Alan Ribeiro do Carmo (10428496), Jean Pazzini Domingues (10428555), Wendell Rodrigues da Costa (10420319) e Leandro Zerbinatti (RA não informado no ambiente).
# Síntese: interface pública para construção dos modelos de classificação do projeto.
# Histórico:
# Data | Autor | Alteração
# 2026-09-15 | GitHub Copilot | Inclusão do módulo de modelos conforme estrutura da disciplina.

from sklearn.pipeline import Pipeline

from .preprocessing import make_pipelines


def build_models(random_state: int = 42) -> dict[str, Pipeline]:
    """Retorna os três pipelines obrigatórios com preprocessamento integrado."""
    return make_pipelines(random_state)
