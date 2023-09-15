from django.db import models

# Create your models here.
class XML(models.Model):

    link = models.URLField(max_length=255, unique=True)
    name = models.CharField(max_length=50, unique=True, default="Untitled")

    def __str__(self):
        return self.name

