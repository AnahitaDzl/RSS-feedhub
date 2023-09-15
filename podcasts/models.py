from django.db import models
from accounts.models import User

# Create your models here.
class XML(models.Model):
    link = models.URLField(max_length=255, unique=True)
    name = models.CharField(max_length=50, unique=True, default="Untitled")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=70)

class Podcast(models.Model):
    title = models.CharField(max_length=100)
    description=models.TextField(null=True, blank=True)
    language = models.CharField(max_length=5, null=True, blank=True)
    author = models.CharField(max_length=50, null=True)
    image = models.URLField(max_length=255, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    xml=models.ForeignKey(XML,on_delete=models.PROTECT,null=True, blank=True)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,null=True, blank=True)

    def __str__(self):
        return self.title

class Episode(models.Model):
    title = models.CharField(max_length=50,null=True, blank=True)
    link=models.URLField(max_length=255, null=True, blank=True)
    release_date = models.CharField(max_length=100)
    author = models.CharField(max_length=50, null=True)
    duration = models.CharField(max_length=25)
    description = models.TextField(null=True, blank=True)
    image = models.URLField(max_length=255, null=True, blank=True)
    podcast = models.ForeignKey(Podcast, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
