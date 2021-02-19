from django.db import models

class myUser(models.Model):
	photo = models.ImageField(upload_to='photos')
	username = models.CharField(max_length=100)