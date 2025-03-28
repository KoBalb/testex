from django.db import models
from django.db.models import Model


# Create your models here.
# база данных
class Text(models.Model):
    text = models.TextField('')

    def __str__(self):
        return self.text
