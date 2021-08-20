from flask_restful import Api
from flask import Blueprint, request
from service.api import SolverAPI
from service.decorators import handle_api_exceptions
import redis


cacher = redis.Redis(host="klarna_redis", port=6379, db=0)
solver_blueprint = Blueprint("solver_api", __name__)
api = Api(solver_blueprint)
solver_api = SolverAPI(cacher)

# NOTE: this can be done in different ways
# PUT or GET, hard to choose from
@solver_blueprint.route("/solver", methods=["GET"])
@handle_api_exceptions
def solver():
    args = solver_api.arg_parser.parse_args()
    return solver_api.calculate(args.function, args.arguments)
