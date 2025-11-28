# api/models.py

from pydantic import BaseModel, Field, conlist
from typing import List

class AdherenceItem(BaseModel):
    """
    Define a estrutura para um item individual da matriz de aderência.
    """
    keyword: str = Field(..., min_length=1, description="Palavra-chave para buscar a aderência.")

    # Correção: removemos o argumento 'description' do conlist
    weight: float = Field(..., gt=0, le=1, description="Peso da aderência (deve ser > 0 e <= 1).")

class SearchRequest(BaseModel):
    """
    Define a estrutura completa da requisição de busca do frontend.
    """
    title: str = Field(..., min_length=5, description="Título descritivo do projeto/sistema.")

    # O conlist valida a lista sem o argumento 'description'
    adherence_matrix: conlist(AdherenceItem, min_length=1)