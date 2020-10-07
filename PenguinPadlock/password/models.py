from django.db import models
from django.contrib.auth.models import User

class Passowrd(models.Model):
	name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	owner = model.ForeignKey(User, on_delet=models.CASCADE)
