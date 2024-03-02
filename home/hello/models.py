from django.db import models


# Create your models here.
class Contect(models.Model):
    name=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
    address=models.CharField(max_length=122)
    
