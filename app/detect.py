import re
from typing import Optional, List

from app.config import ENCODER_MODEL, SENTIMENT_MODEL, get_class_from_prediction
from app.types import SetimentScore

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


def predict_sentiment(texts : str | List[str]) -> List[SetimentScore]:
    
    if isinstance(texts, str):
        texts = [texts]

    clean_texts = []

    for t in texts:
        r = clean_text(t)
        if r:
            clean_texts.append(r)
    

    text_emb = ENCODER_MODEL.encode(clean_texts)
    pred = SENTIMENT_MODEL.predict(text_emb)
    results = []

    for p in pred:
        label = get_class_from_prediction(p)
        s = SetimentScore(label, score=0)
        results.append(s)

    return results
