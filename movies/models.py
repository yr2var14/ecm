from django.db import models

# Create your models here.

class Movies(models.Model):
	title = models.CharField(max_length=200)
	director = models.CharField(max_length=200)
        cast = models.CharField(max_length=200)
	price = models.CharField(max_length=5)
  
	def __unicode__(self):
            return self.title + "/" + self.director + "/" + self.cast + "/" + self.price





