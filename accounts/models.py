from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from podcasts.models import Podcast

# Create your models here.
class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Subscription(models.Model):
        subscription_date = models.DateField()
        user = models.ForeignKey(User, on_delete=models.PROTECT)
        podcast = models.ForeignKey(Podcast, on_delete=models.PROTECT)