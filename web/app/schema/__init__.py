from graphene import ObjectType, Schema, List, Boolean
from . import device

class Query(device.Query):
    pass

class Mutation(ObjectType):
    create_device = device.CreateDeviceMutation.Field()

schema = Schema(query=Query, mutation=Mutation)
