from django.db import models


class Device(models.Model):

    class Meta:
        db_table = 'devices'

    class DeviceType(models.TextChoices):
        PRODUCTION = 'production'
        CONSUMPTION = 'consumption'
        STORAGE = 'storage'

    class DeviceStatus(models.IntegerChoices):
        OFFLINE = 0
        ONLINE = 1

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=20)

    device_type = models.CharField(
        max_length=20,
        choices=DeviceType.choices,
        help_text="The type of device (production, consumption, storage)"
    )

    status = models.IntegerField(
        choices=DeviceStatus.choices,
        help_text="The status of the device (0 = OFFLINE, 1 = ONLINE)"
    )
