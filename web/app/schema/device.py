from graphene import List, Enum, ObjectType, Mutation, Int, String
from graphene_django import DjangoObjectType
from app.models import Device


class DeviceObjectType(DjangoObjectType):
    class Meta:
        model = Device
        fields = ['id']

DeviceTypeEnum   = Enum.from_enum(Device.DeviceType)
DeviceStatusEnum = Enum.from_enum(Device.DeviceStatus)


class Query(ObjectType):

    retrieve_devices = List(DeviceObjectType)

    # TODO: Filter by user id via jwt token
    def resolve_retrieve_devices(root, info):
        return Device.objects.all()


class CreateDeviceMutation(Mutation):

    id = Int()

    class Arguments:
        # TODO: Implement me, get via jwt token
        # user_id = graphene.Int(required=True)
        name = String(required=True)
        device_type = DeviceTypeEnum(required=True)
        status = DeviceStatusEnum(required=True)
    
    @classmethod
    def mutate(cls, root, info, name, device_type, status):
        # TODO: Validate jwt token

        created = Device(
            name=name,
            device_type=device_type,
            status=status
        )

        created.save()

        return CreateDeviceMutation(id=created.id)
