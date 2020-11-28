from django.db import models

# Create your models here.
class Profile(models.Model):
	content = models.TextFiels(null=True, blank=True)
	username = models.CharField(max_length=20, min_length=3)
	userEmail = models.EmailField()
	