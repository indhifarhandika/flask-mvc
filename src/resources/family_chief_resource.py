from flask import request
from flask_restx import reqparse, marshal


from src.resources import api
from src.resources.base_resource import BaseResource
from src.models.family import Family
from src.view_models.simple_family import simple_family_model
from src.view_models.family import family_model


class FamilyChiefResource(BaseResource):
    @api.expect(simple_family_model)
    @api.response(200, "Succeed")
    @api.response(400, "Bad Request")
    @api.response(404, "Not found")
    def put(self):
        if (
            not api.payload
            or "id" not in api.payload
            or "chief_person_id" not in api.payload
        ):
            return self.bad_request(None)

        id = api.payload.get("id")
        api.logger.info(f"change_chief_of_family id={id}")
        family = Family.query.filter(Family.id == id).first()
        if not family:
            return self.not_found(None)

        family.chief_person_id = api.payload.get("chief_person_id")
        Family.session.commit()
        return self.succeed(marshal(family, family_model))
