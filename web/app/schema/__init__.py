from graphene import ObjectType, Schema, List, Boolean
from .device import CreateDeviceMutation

class Query(ObjectType):
    retrieve_devices = Boolean()

    # TODO: Extract me
    def resolve_retrieve_devices(root, info):
        return True

class Mutation(ObjectType):
    create_device = CreateDeviceMutation.Field()

schema = Schema(query=Query, mutation=Mutation)
