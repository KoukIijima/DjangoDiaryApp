from logging import getLogger

_logger = getLogger(__name__)


class RoutingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/api/v1.0/auth/token/login':
            request.session.flush()
        _logger.info(request)
        response = self.get_response(request)
        return response
