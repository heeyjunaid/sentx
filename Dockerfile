FROM python:3.10-slim

WORKDIR /app

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml
COPY ./app ./app
COPY ./models/sentiment-classifier-lr.pkl ./models/sentiment-classifier-lr.pkl
COPY server.py server.py
COPY README.md README.md

RUN pip3 install poetry
RUN poetry install --without dev

ARG encder_name="thenlper/gte-base"

# download and cache model
RUN poetry run python3 -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('${encder_name}')"

ENV ENCODER_MODEL_NAME=$encder_name
CMD ["poetry", "run","gunicorn", "--bind","0.0.0.0:5213", "-w", "2", "server:app"]