import requests
import urllib3
from urllib.parse import urljoin
import json

from solver.funcs import assert_integer

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class ApiOperationException(Exception):
    pass


def merge_exception_message(exception_type, traceback, message):
    merge_traceback = "".join(traceback)
    exception_message = "\n".join([exception_type, message, merge_traceback])
    return exception_message


class RequestHandler(object):
    def __init__(self, session):
        self.session = session

    def put(self, url: str, body: dict):
        response_raw = self.session.put(url, json=body, verify=False)
        return self._parse_response(response_raw)

    def get(self, url: str, body: dict):
        response_raw = self.session.get(url, json=body, verify=False)
        return self._parse_response(response_raw)

    def _parse_response(self, response_raw: dict):
        response = response_raw.json()
        if "exception_type" in response:
            message = merge_exception_message(response["exception_type"],
                                              response["traceback"],
                                              response["message"])
            raise ApiOperationException(message)
        return response["response"]["result"]


def construct_url(host: str, port: int, secure: bool):
    if not port:
        url = host
    else:
        url = f"{host}:{port}"

    if secure:
        return f"https://{url}"

    return f"http://{url}"


class SolverClient:
    def __init__(self, host: str = "localhost", port: int = 5000,
                 secure: bool = False):
        """
        Usage:

        client = SolverClient("localhost", 5000)
        client.fibbonachi(10)
        """
        endpoint = "api/solver"
        self.api_url = construct_url(host, port, secure)
        self.api_endpoint = urljoin(self.api_url, endpoint)
        self.request_handler = RequestHandler(requests.Session())

    # NOTE: explicit better than implicit?
    # can be one function instead, but i wanted to be readable
    def fibbonachi(self, number: int) -> int:
        assert_integer(number)

        body = {
            "function": "fibbonaci",
            "arguments": [number]
        }
        return self.request_handler.get(self.api_endpoint,
                                        body=body)

    def fibbonachi_recursive(self, number: int) -> int:
        assert_integer(number)

        body = {
            "function": "fibbonaci_recursive",
            "arguments": [number]
        }
        return self.request_handler.get(self.api_endpoint,
                                        body=body)

    def factorial(self, number: int) -> int:
        assert_integer(number)

        body = {
            "function": "factorial",
            "arguments": [number]
        }
        return self.request_handler.get(self.api_endpoint,
                                        body=body)

    def factorial_recursive(self, number: int) -> int:
        assert_integer(number)

        body = {
            "function": "factorial_recursive",
            "arguments": [number]
        }
        return self.request_handler.get(self.api_endpoint,
                                        body=body)

    def ackermann_recursive(self, argument_n: int, argument_m: int) -> int:
        assert_integer(argument_n)
        assert_integer(argument_m)

        body = {
            "function": "ackermann_recursive",
            "arguments": [argument_n, argument_m]
        }
        return self.request_handler.get(self.api_endpoint,
                                        body=body)
