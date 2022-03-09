from django.db import models

# Create your models here.

class App2Model(models.Model):
    desc = models.CharField(max_length=2)