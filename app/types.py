from typing import List
from pydantic import BaseModel
from uuid import UUID


class DetectSentimentRequest(BaseModel):
    text : str
    config : None

class BatchDetectSentimentRequest(BaseModel):
    req : List[DetectSentimentRequest]

class SetimentScore(BaseModel):
    label : str
    score : float

class DetectSentimentResponse(BaseModel):
    text : str
    config : None
    job_id: UUID
    sentiment_results : List[SetimentScore]

class BatchDetectSentimentResponse(BaseModel):
    job_id: UUID



