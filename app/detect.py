import re
from flask import abort
from typing import Optional, List

from app.config import ENCODER_MODEL, SENTIMENT_MODEL, get_class_from_prediction
from app.types import SetimentScore, DetectSentimentRequest, DetectSentimentResponse

regex_url_matching = "https?://\S+|www.\S+"
regex_userid_matching = "@\S+"
regex_extra_spaces = "\s{2,}"
regex_hashtag = "#\S+"
regex_non_chars_line = "^[\W_]+$"

def clean_text(text:str) -> Optional[str]:
    text = re.sub(regex_url_matching, ' ', text)
    text = re.sub(regex_userid_matching, ' ', text)
    text = re.sub(regex_hashtag, " ", text)
    text = re.sub(regex_non_chars_line, " ", text)
    text = re.sub(regex_extra_spaces, " ", text)
    text = text.strip()   

    if not text:
        return None
    
    return text

def handle_batch_result(texts, clean_texts, pred_batch):
    batch_response = []
    for text, clean_text, pred in zip(texts, clean_texts, pred_batch):
        result = [
            SetimentScore("negative", pred[0]),
            SetimentScore("positive", pred[1]),
            SetimentScore("neutral", pred[2])
        ]
        
        batch_response.append(DetectSentimentResponse(
            text=text,
            processed_text=clean_text,
            sentiment_results=result
        ))

    return batch_response


def predict_sentiment_one(text):
    if not text:
        abort(400, description="no valid text for sentiment detection found")

    ctext = clean_text(text)

    if ctext is None:
        abort(400, description="no valid text for sentiment detection found")
    
    try:
        text_emb = ENCODER_MODEL.encode([ctext])
        pred = SENTIMENT_MODEL.predict_proba(text_emb)
    except Exception as error:
        abort(500, description="something went wrong with while calculating sentiment of text")

    result = [
                SetimentScore(label="negative", score=round(pred[0][0], 4)),
                SetimentScore(label="positive", score=round(pred[0][1], 4)),
                SetimentScore(label="neutral", score=round(pred[0][2], 4))
            ]
    
    return DetectSentimentResponse(
            text=text,
            processed_text=ctext,
            sentiment_results=result
        )


def predict_sentiment(texts : str | List[str]) -> List[DetectSentimentResponse]:
    
    if isinstance(texts, str):
        texts = [texts]

    clean_texts = []

    for t in texts:
        r = clean_text(t)
        if r:
            clean_texts.append(r)
    

    text_emb = ENCODER_MODEL.encode(clean_texts)
    pred = SENTIMENT_MODEL.predict_proba(text_emb)
    return handle_batch_result(texts, clean_texts, pred)