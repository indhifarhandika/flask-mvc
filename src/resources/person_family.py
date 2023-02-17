from flask import request
from flask_restx import reqparse, marshal


from src.resources import api
from src.resources.base_resource import BaseResource
from src.models.person import Person
from src.view_models.simple_person import simple_person_model
from src.view_models.person import person_model


class PersonFamilyResource(BaseResource):
    @api.expect(simple_person_model)
    @api.response(200, "Succeed")
    @api.response(400, "Bad Request")
    @api.response(404, "Not found")
    def put(self):
        if not api.payload or "id" not in api.payload or "family_id" not in api.payload:
            return self.bad_request(None)

        id = api.payload.get("id")
        api.logger.info(f"change_family_for_person id={id}")
        person = Person.query.get(id)
        if not person:
            return self.not_found(None)

        person.family_id = api.payload.get("family_id")
        Person.session.commit()
        return self.succeed(marshal(person, person_model))

    @api.response(200, "Succeed")
    @api.response(400, "Bad Request")
    @api.response(404, "Not found")
    def delete(self):
        if not api.payload or "id" not in api.payload:
            return self.bad_request(None)

        api.logger.info(f"remove_family_for_person id={id}")
        person = Person.query.get(id)
        if not person:
            return self.not_found(None)

        person.family_id = None
        Person.session.commit()
        return self.succeed(marshal(person, person_model))
