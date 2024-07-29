from flask import Flask

from app.routes import sentx_app

API_VERSION_PREFIX = "/api/v1"



app = Flask(__name__)
app.register_blueprint(sentx_app, url_prefix=API_VERSION_PREFIX+"/sentx")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5213)