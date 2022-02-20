from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class user_name(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name