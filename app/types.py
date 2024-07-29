from typing import List, Optional
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
    processed_text:str
    config : dict = None
    job_id: Optional[UUID] = None
    sentiment_results : List[SetimentScore]

class BatchDetectSentimentResponse(BaseModel):
    job_id: UUID



