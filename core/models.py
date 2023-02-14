from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField(auto_created=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

