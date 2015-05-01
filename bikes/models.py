from django.db import models

# Create your models here.

class Bikes(models.Model):
	model = models.CharField(max_length=200)
	manufacturer = models.CharField(max_length=200)
	price = models.CharField(max_length=5)
  
	def __unicode__(self):
            return self.model + "/" + self.manufacturer + "/" + self.price
