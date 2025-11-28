from pydantic import BaseModel
from typing import List


class AdherenceItem(BaseModel):
keyword: str
weight: float


class SearchRequest(BaseModel):
title: str
adherence_matrix: List[AdherenceItem]