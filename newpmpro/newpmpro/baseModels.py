from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class CustomModel(models.Model):
    createdAt = models.DateTimeField(default=datetime.utcnow())
    modifiedAt = models.DateTimeField(default=datetime.utcnow())
    isDeleted = models.BooleanField(default=False)

    @classmethod
    def get_field_names(cls):
        field_names = list()
        for field in CustomModel._meta.fields:
            field_names.append(field.attname)
        return field_names

    class Meta:
        abstract = True
