from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    date_register = timezone.now()
    date_modify = timezone.now()

    def __str__(self):
        return '{} {}'.format(self.name, self.lastname)



