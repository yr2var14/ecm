from django.db import models

# Create your models here.

class Books(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	rate = models.CharField(max_length=5)
  
	def __unicode__(self):
            return self.title + "/" + self.author + "/" + self.rate
