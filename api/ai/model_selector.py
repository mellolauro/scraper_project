from typing import List, Dict, Any


# Este selector é um placeholder: escolhe um modelo de embeddings/texto
# Para produção, substitua por lógica real (checar recursos, GPU, etc.)


class DummyModel:
    """Wrapper mínimo usando sentence-transformers quando disponível."""
    def __init__(self, model_name_or_obj):
        self.model = model_name_or_obj


    def encode(self, *args, **kwargs):
        return self.model.encode(*args, **kwargs)




def select_optimal_model(project_title: str, matrix: List[Dict[str, Any]], scraped_data: List[Dict[str, Any]]):
    """Retorna uma instância leve do SentenceTransformer (padrão)."""

    try:
        from sentence_transformers import SentenceTransformer
    except Exception:
        raise RuntimeError("sentence-transformers não está instalado no ambiente")


# lógica simples: se matriz longa (muitos termos) usa modelo maior — aqui apenas exemplo
matrix_len = sum(len(item['keyword'].split()) for item in matrix)
if matrix_len > 40:
    name = 'sentence-transformers/all-mpnet-base-v2'
else:
    name = 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'


    print(f"[AUTO-MODEL] Selecionado: {name} (matrix_len={matrix_len})")
    base = SentenceTransformer(name)
    return DummyModel(base)