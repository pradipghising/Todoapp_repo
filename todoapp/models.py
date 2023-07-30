from django.db import models
from todoapp import views
# Create your models here.
class todomodel(models.Model):
    task=models.CharField(max_length=50)