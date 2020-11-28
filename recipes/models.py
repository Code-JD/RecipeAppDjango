from django.db import models

# Create your models here.
class Recipes(models.Model):
	# id = models.AutoField()
	title = models.CharField(max_length=220)
	ingredients = models.CharField(max_length=220)
	directions = models.CharField(max_length=220)
	content = models.TextField(null=True, blank=True)