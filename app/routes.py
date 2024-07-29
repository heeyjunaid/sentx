from uuid import uuid4
from flask import Blueprint, request, jsonify


from app.utils import init_logger
from app.types import DetectSentimentRequest, BatchDetectSentimentResponse
from app.detect import predict_sentiment

logger=init_logger(__name__)
sentx_app = Blueprint("sentx_app", __name__)


@sentx_app.get("/")
def root():
    return {"message": "Hello from sentx"}


@sentx_app.get("/healthz")
def health_check():
    return {"response": "ok"}


@sentx_app.post("/detect")
def detect_sentiment():
    req = request.json
    req = DetectSentimentRequest(**req)
    res = predict_sentiment(req.text)
    return jsonify(res)


@sentx_app.post("/batch/detect")
def batch_detect_sentiment():
    job_id = uuid4()
    req = request.json
    # TODO: add to queue

    return BatchDetectSentimentResponse(job_id)

@sentx_app.get("/batch/result/<job_id>")
def get_batch_results(job_id):
    # TODO: get result from redis queue
    pass