import os
import pickle
from typing import List, Optional
from sklearn. base import BaseEstimator
from sentence_transformers import SentenceTransformer

from app.utils import init_logger

logger = init_logger(__name__)


def safeGetWithDefault(key:str, default:str, ignore_warning=True):
    value = os.environ.get(key)
    if value is None:
        if not ignore_warning:
            logger.warning(f"ENV NOT FOUND for key: {key}, using default value")
        return default
    else:
        return value

def load_model(path:str) -> BaseEstimator:
    if not os.path.exists(path):
        raise ValueError(f"model path: {path} does not exists!")
    
    # can be loaded from s3 in future
    with open(path, "rb") as f:
        model = pickle.load(f)

    return model

def get_class_from_prediction(label:int) -> Optional[str]:
    label_mapping = {
        0 : "negative",
        1 : "positive",
        2 : "neutral"
    }
    return label_mapping.get(label, None)



ENCODER_MODEL_NAME = safeGetWithDefault("ENCODER_MODEL_NAME", "thenlper/gte-base")
SENTIMENT_MODEL_NAME = safeGetWithDefault("SENTIMENT_MODEL_NAME", "./models/sentiment-classifier-lr.pkl")

SENTIMENT_MODEL = load_model(SENTIMENT_MODEL_NAME)
ENCODER_MODEL = SentenceTransformer(ENCODER_MODEL_NAME)