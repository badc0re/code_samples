from flask_restful import reqparse
from flask import g
from solver import funcs


AVAILIBLE_FUNCTIONS = {
    "fibbonaci": funcs.fibbonaci,
    "fibbonaci_recursive": funcs.fibbonaci_recursive,
    "factorial": funcs.factorial,
    "factorial_recursive": funcs.factorial_recursive,
    "ackermann_recursive": funcs.ackermann_recursive
}


class FunctionNotSupported(Exception):
    pass


class SolverAPI(object):
    def __init__(self, cache_client):
        """The server API for calculating the result.
        """
        self.arg_parser = reqparse.RequestParser()

        arg_conf = {
            "function": {
                "default": "fibbonaci", "type": str
            },
            "arguments": {
                "default": [10], "action": "append", "type": int
            }
        }
        for param_name, param_conf in arg_conf.items():
            self.arg_parser.add_argument(param_name,
                                         **param_conf)
        self.cache_client = cache_client

    def _generate_cache_key(self, function_name: str, arguments):
        """Key for caching the results in Redis.
        """
        merged_arguments = "_".join(map(str, arguments))
        return f"{function_name}_{merged_arguments}"

    def calculate(self, function_name: str, arguments):
        """Get a value for a specific function.
        """
        cache_key = self._generate_cache_key(function_name, arguments)

        # can be a decorator
        g.function_name = function_name
        g.arguments = arguments

        response = {
            "response": {
                "status_type": "DONE",
                "message": ""
            }
        }
        if function_name not in AVAILIBLE_FUNCTIONS:
            raise FunctionNotSupported

        result = self.cache_client.get(cache_key)
        if result:
            result = int(result.decode())
        else:
            function = AVAILIBLE_FUNCTIONS[function_name]
            result = function(*arguments)
            self.cache_client.set(cache_key, result, nx=True)

        response["response"]["result"] = result
        return response
