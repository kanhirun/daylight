import graphene
from graphene_django import DjangoObjectType
from app.models import Device

DeviceTypeEnum   = graphene.Enum.from_enum(Device.DeviceType)
DeviceStatusEnum = graphene.Enum.from_enum(Device.DeviceStatus)

class CreateDeviceMutation(graphene.Mutation):

    id = graphene.Int()

    class Arguments:
        # TODO: Implement me, get via jwt token
        # user_id = graphene.Int(required=True)
        name = graphene.String(required=True)
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
