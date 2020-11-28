from django.db import models

# Create your models here.
class Recipes(models.Model):
	title = models.CharField(max_length=220)
	ingredients = models.TextField(null=True, blank=True)
	directions = models.TextField(null=True, blank=True)
	content = models.TextField(null=True, blank=True)