from service.log import getLogger
from service.endpoint import solver_blueprint
from flask import Blueprint, request
from flask import Flask, g
import time

log = getLogger(__name__)

app = Flask(__name__)
cursor_blueprint = Blueprint("cursor_api", __name__)
app.register_blueprint(solver_blueprint, url_prefix="/api")


@app.before_request
def before_request():
    g.request_start_time = time.time()


@app.after_request
def after_request(response):
    calc_time = time.time() - g.request_start_time
    log.info(f"Function:{g.function_name}, arguments:{g.arguments}, time {calc_time}")
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
