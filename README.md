# sentx

## Build Docker Image
Run following command to build docker image. This will take couple of minutes to build.
```shell
$ docker build -t sentx
```
Once image is build, run following command to run image.
```shell
$ docker run -p 5213:5213 sentx
```

## Setup Locally for development
1. create venv 
```shell
$ python3 -m venv .env
```
2. activate venv
```shell
$ source .env/bin/activate
```
3. install poetry
```shell
$ pip3 install poetry
```
4. install dependecies
```shell
$ poetry install
```
5. run app
```shell
$ python3 server.py
```

## APIs
This app exposes API to do sentiment analysis. Once you run the server. You can run following curl

```shell
curl --location 'http://localhost:5213/api/v1/sentx/detect' \
--header 'Content-Type: application/json' \
--data '{
    "text": "hello world!"
}'
```
this will return following response
```json
{
    "config": null,
    "job_id": null,
    "processed_text": "hello world!",
    "sentiment_results": [
        {
            "label": "negative",
            "score": 0.0
        },
        {
            "label": "positive",
            "score": 1.0
        },
        {
            "label": "neutral",
            "score": 0.0
        }
    ],
    "text": "hello world!"
}
```