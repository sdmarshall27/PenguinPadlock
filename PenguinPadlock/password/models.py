from django.db import models
from django.contrib.auth.models import User

class PasswordTable(models.Model):
	description = models.CharField(max_length=255)
	password = models.CharField(max_length=50)
	owner = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.description