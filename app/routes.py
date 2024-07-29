from uuid import uuid4
from flask import Blueprint, request, jsonify


from app.utils import init_logger
from app.types import DetectSentimentRequest, BatchDetectSentimentResponse
from app.detect import predict_sentiment_one
from werkzeug.exceptions import HTTPException


logger=init_logger(__name__)
sentx_app = Blueprint("sentx_app", __name__)

@sentx_app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        response = {
            "error": e.description,
            "code": e.code
        }
    else:
        response = {
            "error": str(e),
            "code": 500
        }
    return jsonify(response), response["code"]


@sentx_app.get("/")
def root():
    return {"message": "Hello from sentx"}


@sentx_app.get("/healthz")
def health_check():
    return {"response": "ok"}


@sentx_app.post("/detect")
def detect_sentiment():
    req = request.json
    text = req.get("text", None)
    res = predict_sentiment_one(text)
    return jsonify(res.model_dump())


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