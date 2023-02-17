from flask import request
from flask_restx import reqparse, marshal


from src.resources import api
from src.resources.base_resource import BaseResource
from src.models.person import Person
from src.view_models.simple_person import simple_person_model
from src.view_models.person import person_model


class PersonResource(BaseResource):
    @api.param("id", "If set, get only 1 person. If not set, get many persons.")
    @api.param("limit", "max number of persons.")
    @api.param("offset", "offset to get persons.")
    @api.response(200, "Succeed")
    @api.response(404, "Not found")
    def get(self):
        if "id" in request.args:
            parser = reqparse.RequestParser()
            parser.add_argument("id", type=int)
            args = parser.parse_args()

            id = args["id"]
            api.logger.info(f"get_person id={id}")
            person = Person.query.filter(Person.id == id).first()
            if not person:
                return self.bad_request(None)

            return self.succeed(marshal(person, person_model))

        parser = reqparse.RequestParser()
        parser.add_argument("limit", type=int, default=10)
        parser.add_argument("offset", type=int, default=0)
        args = parser.parse_args()

        limit = args["limit"]
        offset = args["offset"]
        api.logger.info(f"get_persons offset={offset} limit={limit}")
        persons = Person.query.order_by(Person.id).limit(limit).offset(offset).all()
        total = Person.query.count()
        return self.succeed({"data": marshal(persons, person_model), "total": total})

    @api.expect(simple_person_model)
    @api.response(200, "Succeed")
    @api.response(400, "Bad Request")
    def post(self):
        if not api.payload or "name" not in api.payload:
            return self.bad_request(None)

        name = api.payload.get("name")
        family_id = api.payload.get("family_id")
        gender = api.payload.get("gender")
        api.logger.info(f"create_person")
        person = Person(
            name=name,
            family_id=family_id,
            gender=gender,
        )
        Person.session.add(person)
        Person.session.commit()
        return self.succeed(marshal(person, person_model))

    @api.expect(simple_person_model)
    @api.response(200, "Succeed")
    @api.response(400, "Bad Request")
    @api.response(404, "Not found")
    def put(self):
        if not api.payload or "id" not in api.payload:
            return self.bad_request(None)

        id = api.payload.get("id")
        api.logger.info(f"edit_person id={id}")
        person = Person.query.filter(Person.id == id).first()
        if not person:
            return self.not_found(None)

        if "name" in api.payload:
            person.name = api.payload.get("name")
        if "family_id" in api.payload:
            person.family_id = api.payload.get("family_id")
        if "gender" in api.payload:
            person.gender = api.payload.get("gender")
        if "join_person_id" in api.payload:
            person.join_person_id = api.payload.get("join_person_id")
        Person.session.commit()
        return self.succeed(marshal(person, person_model))

    @api.param("id", "id of person to delete.")
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

        api.logger.info(f"delete_person id={id}")
        person = Person.query.filter(Person.id == id).first()
        if not person:
            return self.not_found(None)

        Person.session.delete(person)
        Person.session.commit()
        return self.succeed(None)
