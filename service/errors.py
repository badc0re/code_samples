import sys
import traceback

from flask import make_response, jsonify
from werkzeug.exceptions import HTTPException


CONFLICT = 'Conflict'
NOT_FOUND = 'Not found'
BAD_REQUEST = 'Bad request'
INTERNAL_SERVER_ERROR = 'Internal server error'

# 4xx CLIENT ERRORS
HTTP_400_BAD_REQUEST = 400
HTTP_404_NOT_FOUND = 404
HTTP_409_CONFLICT = 409

# 5xx SERVER ERRORS
HTTP_500_INTERNAL_SERVER_ERROR = 500


class ApiExceptions:
    NOT_FOUND_EXCEPTIONS = (Exception, AttributeError)
    BAD_REQUEST_EXCEPTIONS = (Exception)
    CONFLICT_EXCEPTIONS = (Exception)
    INTERNAL_SERVER_ERROR_EXCEPTIONS = (Exception)


def get_traceback():
    """Get the stack.
    """
    _, _, tb = sys.exc_info()
    return traceback.format_tb(tb)


def get_message(message, exception, exception_type, tb):
    """Get the api stacktrace and propagate it back to the client
    """
    if not exception:
        return message
    if not isinstance(exception, HTTPException):
        return '{}: {}'.format(message, str(exception))
    if not hasattr(exception, 'data'):
        return exception.description
    exception.data['exception_type'] = exception_type
    exception.data['traceback'] = tb
    raise


def error_json(message, exception, **kwargs):
    """Format the stacktrace.
    """
    exception_type = type(exception).__name__ if exception else ''
    tb = get_traceback() if exception else []
    msg = get_message(message, exception, exception_type, tb)
    return jsonify(message=msg, exception_type=exception_type, traceback=tb,
                   **kwargs)


def not_found_response(message=NOT_FOUND, exception=None, **kwargs):
    return make_response(error_json(message, exception, **kwargs),
                         HTTP_404_NOT_FOUND)


def internal_server_error_response(message=INTERNAL_SERVER_ERROR,
                                   exception=None, **kwargs):
    return make_response(error_json(message, exception, **kwargs),
                         HTTP_500_INTERNAL_SERVER_ERROR)


def bad_request_response(message=BAD_REQUEST, exception=None, **kwargs):
    return make_response(error_json(message, exception, **kwargs),
                         HTTP_400_BAD_REQUEST)


def conflict_response(message=CONFLICT, exception=None, **kwargs):
    return make_response(error_json(message, exception, **kwargs),
                         HTTP_409_CONFLICT)
