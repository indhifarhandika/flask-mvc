import os, glob


__all__ = [
    os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")
]

from flask_restx import Api

api = Api(prefix="/api/v1")


def add_resources():
    from src.resources.family_resource import FamilyResource
    from src.resources.person_resource import PersonResource
    from src.resources.relationship_type_resource import RelationshipTypeResource
    from src.resources.family_chief_resource import FamilyChiefResource
    from src.resources.person_family import PersonFamilyResource

    api.add_resource(FamilyResource, "/family")
    api.add_resource(PersonResource, "/person")
    api.add_resource(RelationshipTypeResource, "/relationship_type")
    api.add_resource(FamilyChiefResource, "/family_chief")
    api.add_resource(PersonFamilyResource, "/person_family")
