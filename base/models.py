from django.db import models
import uuid

class BaseModel(models.Model):
    uuid = models.UUIDField('ID', primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True