from flask import request
from flask_restx import reqparse, marshal


from src.resources import api
from src.resources.base_resource import BaseResource
from src.models.relationship_type import RelationshipType
from src.view_models.relationship_type import relationship_type_model


class RelationshipTypeResource(BaseResource):
    @api.param(
        "id",
        "If set, get only 1 relationship type. If not set, get many relationship types.",
    )
    @api.param("limit", "max number of relationship_types.")
    @api.param("offset", "offset to get relationship_types.")
    @api.response(200, "Succeed")
    @api.response(404, "Not found")
    def get(self):
        if "id" in request.args:
            parser = reqparse.RequestParser()
            parser.add_argument("id", type=int)
            args = parser.parse_args()

            id = args["id"]
            api.logger.info(f"get_relationship_type id={id}")
            relationship_type = RelationshipType.query.filter(
                RelationshipType.id == id
            ).first()
            if not relationship_type:
                return self.not_found(None)

            return self.succeed(marshal(relationship_type, relationship_type_model))

        parser = reqparse.RequestParser()
        parser.add_argument("limit", type=int, default=10)
        parser.add_argument("offset", type=int, default=0)
        args = parser.parse_args()

        limit = args["limit"]
        offset = args["offset"]
        api.logger.info(f"get_families offset={offset} limit={limit}")
        relationship_types = (
            RelationshipType.query.order_by(RelationshipType.id)
            .limit(limit)
            .offset(offset)
            .all()
        )
        total = RelationshipType.query.count()
        return self.succeed(
            {
                "data": marshal(relationship_types, relationship_type_model),
                "total": total,
            }
        )

    @api.expect(relationship_type_model)
    @api.response(200, "Succeed")
    @api.response(400, "Bad Request")
    def post(self):
        if not api.payload or "name" not in api.payload:
            return self.bad_request(None)

        name = api.payload.get("name")
        api.logger.info(f"create_relationship_type")
        relationship_type = RelationshipType(name=name)
        RelationshipType.session.add(relationship_type)
        RelationshipType.session.commit()
        return self.succeed(marshal(relationship_type, relationship_type_model))

    @api.expect(relationship_type_model)
    @api.response(200, "Succeed")
    @api.response(400, "Bad Request")
    @api.response(404, "Not found")
    def put(self):
        if not api.payload or "id" not in api.payload:
            return self.bad_request(None)

        id = api.payload.get("id")
        api.logger.info(f"edit_relationship_type id={id}")
        relationship_type = RelationshipType.query.filter(
            RelationshipType.id == id
        ).first()
        if not relationship_type:
            return self.not_found(None)

        if "name" in api.payload:
            relationship_type.name = api.payload.get("name")
        RelationshipType.session.commit()
        return self.succeed(marshal(relationship_type, relationship_type_model))

    @api.param("id", "id of relationship_type to delete.")
    @api.response(200, "Succeed")
    @api.response(404, "Not found")
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int)
        args = parser.parse_args()

        id = args["id"]
        if not id:
            return self.bad_request(None)

        api.logger.info(f"delete_relationship_type id={id}")
        relationship_type = RelationshipType.query.filter(
            RelationshipType.id == id
        ).first()
        if not relationship_type:
            return self.not_found(None)

        RelationshipType.session.delete(relationship_type)
        RelationshipType.session.commit()
        return self.succeed(None)
