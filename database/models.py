from django.db import models

# Create your models here.
class Pulsar(models.Model):
    name =  models.CharField(max_length=200, verbose_name='Pulsar name.  The B name if exists, otherwise the J name')
