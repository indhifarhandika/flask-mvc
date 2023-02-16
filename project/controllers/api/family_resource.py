from project import api
from flask import request
from flask_restx import reqparse, marshal


from project.controllers.api.base_resource import BaseResource
from project.models.family import db, Family, family_model


@api.route("/api/family")
class FamilyResource(BaseResource):
    @api.param("id", "If set, get only 1 family. If not set, get many families.")
    @api.param("limit", "max number of families.")
    @api.param("offset", "offset to get families.")
    @api.response(200, "Succeed")
    @api.response(404, "Not found")
    def get(self):
        if "id" in request.args:
            parser = reqparse.RequestParser()
            parser.add_argument("id", type=int)
            args = parser.parse_args()

            id = args["id"]
            api.logger.info(f"get_family id={id}")
            family = Family.query.get(id)
            if not family:
                return self.format_response(None, 404, "Not found")

            return self.format_response(marshal(family, family_model), 200, "Succeed")

        parser = reqparse.RequestParser()
        parser.add_argument("limit", type=int, default=10)
        parser.add_argument("offset", type=int, default=0)
        args = parser.parse_args()

        limit = args["limit"]
        offset = args["offset"]
        api.logger.info(f"get_families offset={offset} limit={limit}")
        families = Family.query.order_by(Family.id).limit(limit).offset(offset).all()
        total = Family.query.count()
        return self.format_response(
            {"data": marshal(families, family_model), "total": total}, 200, "Succeed"
        )

    @api.expect(family_model)
    @api.response(200, "Succeed")
    def post(self):
        if not api.payload or "name" not in api.payload:
            return self.format_response(None, 400, "Bad Request")

        name = api.payload.get("name")
        chief_person_id = api.payload.get("chief_person_id")
        api.logger.info(f"create_family")
        family = Family(name=name, chief_person_id=chief_person_id)
        db.session.add(family)
        db.session.commit()
        return self.format_response(marshal(family, family_model), 200, "Succeed")

    @api.expect(family_model)
    @api.response(200, "Succeed")
    @api.response(404, "Not found")
    def put(self):
        if not api.payload or "id" not in api.payload:
            return self.format_response(None, 400, "Bad Request")

        id = api.payload.get("id")
        api.logger.info(f"edit_family id={id}")
        family = Family.query.get(id)
        if not family:
            return self.format_response(None, 404, "Not found")

        if "name" in api.payload:
            family.name = api.payload.get("name")
        if "chief_person_id" in api.payload:
            family.chief_person_id = api.payload.get("chief_person_id")
        db.session.commit()
        return self.format_response(marshal(family, family_model), 200, "Succeed")

    @api.param("id", "id of family to delete.")
    @api.response(200, "Succeed")
    @api.response(404, "Not found")
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int)
        args = parser.parse_args()

        id = args["id"]
        if not id:
            return self.format_response(None, 400, "Bad Request")

        api.logger.info(f"delete_family id={id}")
        family = Family.query.get(id)
        if not family:
            return self.format_response(None, 404, "Not found")

        db.session.delete(family)
        db.session.commit()
        return self.format_response(marshal(family, family_model), 200, "Succeed")
