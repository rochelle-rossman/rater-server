from django.db import models

class Player(models.Model):
  uid = models.CharField(max_length=50)
  bio = models.CharField(max_length=300)
  name = models.CharField(max_length=50)
