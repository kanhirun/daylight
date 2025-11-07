from graphene import List, Enum, ObjectType, Mutation, Int, String, InputObjectType, NonNull, Field
from graphql import GraphQLError
from graphene_django import DjangoObjectType
from app.models import Device


class DeviceObjectType(DjangoObjectType):
    class Meta:
        model = Device
        fields = ('id', 'name', 'status', 'device_type')

# Note: 'graphene' does not support InputObjectTypes derived from Django
# (https://github.com/graphql-python/graphene-django/issues/121)
#
# I will manually type them for now, but this should really be cleaned up.

DeviceTypeEnum   = Enum.from_enum(Device.DeviceType)
DeviceStatusEnum = Enum.from_enum(Device.DeviceStatus)

class CreateDeviceInput(InputObjectType):
    name = String(required=True)
    device_type = DeviceTypeEnum(required=True)
    status = DeviceStatusEnum(required=True)

class UpdateDeviceInput(CreateDeviceInput):
    name = String(required=False)
    device_type = DeviceTypeEnum(required=False)
    status = DeviceStatusEnum(required=False)


class Query(ObjectType):

    retrieve_devices = List(NonNull(DeviceObjectType))

    # TODO: Filter by user id via jwt token
    def resolve_retrieve_devices(root, info):
        return Device.objects.all()


class CreateDeviceMutation(Mutation):

    device = Field(DeviceObjectType, required=False)

    class Arguments:
        data = CreateDeviceInput(required=True)
    
    @classmethod
    def mutate(cls, root, info, id, data):
        # TODO: Validate jwt token at higher level

        created = Device(**data)
        created.save()

        return CreateDeviceMutation(device=created)


class UpdateDeviceMutation(Mutation):

    device = Field(DeviceObjectType, required=False)

    class Arguments:
        id = Int(required=True)
        data = UpdateDeviceInput(required=True)

    @classmethod
    def mutate(cls, root, info, id, data):
        updated = Device.objects.get(id=id)

        for k, v in data.items():
            setattr(updated, k, v)

        updated.save()
        
        return UpdateDeviceMutation(device=updated)


class Mutation(ObjectType):

    create_device = CreateDeviceMutation.Field()
    update_device = UpdateDeviceMutation.Field()

