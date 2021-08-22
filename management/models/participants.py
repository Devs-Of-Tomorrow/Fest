from django.db import models
# Create your models here.


class Participants(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=11, default=False)
    email = models.EmailField(default=False)
    password = models.CharField(max_length=254, default=False)
