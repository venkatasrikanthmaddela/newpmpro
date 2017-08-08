from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class CustomModel(models.Model):
    createdAt = models.DateTimeField(default=datetime.utcnow())
    modifiedAt = models.DateTimeField(default=datetime.utcnow())
    isDeleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
