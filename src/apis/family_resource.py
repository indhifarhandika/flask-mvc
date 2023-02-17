from src import api
from flask import request
from flask_restx import reqparse, marshal


from src.apis.base_resource import BaseResource
from src.models.family import Family
from src.view_models.simple_family import simple_family_model
from src.view_models.family import family_model


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
                return self.not_found(None)

            return self.succeed(marshal(family, family_model))

        parser = reqparse.RequestParser()
        parser.add_argument("limit", type=int, default=10)
        parser.add_argument("offset", type=int, default=0)
        args = parser.parse_args()

        limit = args["limit"]
        offset = args["offset"]
        api.logger.info(f"get_families offset={offset} limit={limit}")
        families = Family.query.order_by(Family.id).limit(limit).offset(offset).all()
        total = Family.query.count()
        return self.succeed({"data": marshal(families, family_model), "total": total})

    @api.expect(simple_family_model)
    @api.response(200, "Succeed")
    @api.response(400, "Bad Request")
    def post(self):
        if not api.payload or "name" not in api.payload:
            return self.bad_request(None)

        name = api.payload.get("name")
        chief_person_id = api.payload.get("chief_person_id")
        api.logger.info(f"create_family")
        family = Family(name=name, chief_person_id=chief_person_id)
        Family.session.add(family)
        Family.session.commit()
        return self.succeed(marshal(family, family_model))

    @api.expect(simple_family_model)
    @api.response(200, "Succeed")
    @api.response(400, "Bad Request")
    @api.response(404, "Not found")
    def put(self):
        if not api.payload or "id" not in api.payload:
            return self.bad_request(None)

        id = api.payload.get("id")
        api.logger.info(f"edit_family id={id}")
        family = Family.query.get(id)
        if not family:
            return self.not_found(None)

        if "name" in api.payload:
            family.name = api.payload.get("name")
        if "chief_person_id" in api.payload:
            family.chief_person_id = api.payload.get("chief_person_id")
        Family.session.commit()
        return self.succeed(marshal(family, family_model))

    @api.param("id", "id of family to delete.")
    @api.response(200, "Succeed")
    @api.response(400, "Bad Request")
    @api.response(404, "Not found")
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int)
        args = parser.parse_args()

        id = args["id"]
        if not id:
            return self.bad_request(None)

        api.logger.info(f"delete_family id={id}")
        family = Family.query.get(id)
        if not family:
            return self.not_found(None)

        Family.session.delete(family)
        Family.session.commit()
        return self.succeed(marshal(family, family_model))
