from pydantic import BaseModel
from typing import List


class PredictRequest(BaseModel):
    sentences: List[str]


class PredictResponse(BaseModel):
    results: List[dict]
