from django.db import models

# Create your models here.
class Profile(models.Model):
	content = models.TextField(null=True, blank=True)
	username = models.CharField(max_length=20)
	userEmail = models.EmailField()
