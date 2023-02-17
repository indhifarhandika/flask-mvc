from flask_restx import Resource


class BaseResource(Resource):
    def _format_response(self, data, status, message):
        return {"data": data, "status": status, "message": message}

    def succeed(self, data):
        return self._format_response(data, 200, "Succeed")

    def bad_request(self, data):
        return self._format_response(data, 400, "Bad Request")

    def not_found(self, data):
        return self._format_response(data, 404, "Not found")
