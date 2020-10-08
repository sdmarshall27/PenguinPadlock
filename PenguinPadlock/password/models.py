from django.db import models
from django.contrib.auth.models import User

class Password(models.Model):
	description = models.CharField(max_length=250)
	password = models.CharField(max_length=50)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
