from flask_restx import Resource


class BaseResource(Resource):
    def format_response(self, data, status, message):
        return {"data": data, "status": status, "message": message}
