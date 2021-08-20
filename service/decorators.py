from functools import wraps
import service.errors as errors


def handle_api_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except errors.ApiExceptions.BAD_REQUEST_EXCEPTIONS as e:
            return errors.bad_request_response(exception=e)
        except errors.ApiExceptions.NOT_FOUND_EXCEPTIONS as e:
            return errors.not_found_response(exception=e)
        except errors.ApiExceptions.CONFLICT_EXCEPTIONS as e:
            return errors.conflict_response(exception=e)
        except errors.ApiExceptions.INTERNAL_SERVER_ERROR_EXCEPTIONS as e:
            return errors.internal_server_error_response(exception=e)
    return wrapper
