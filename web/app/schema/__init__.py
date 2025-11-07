from graphene import ObjectType, Schema, List, Boolean
from . import device

class Query(device.Query):
    pass

class Mutation(device.Mutation):
    pass

schema = Schema(query=Query, mutation=Mutation)
