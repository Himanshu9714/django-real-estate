from django.db import models
import uuid


class IdMixinModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=False)

    class Meta:
        abstract = True


class TimeStampedUUIDModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DefaultMixinModel(IdMixinModel, TimeStampedUUIDModel):

    class Meta:
        abstract = True
