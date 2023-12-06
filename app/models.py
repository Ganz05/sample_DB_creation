from django.db import models

# Create your models here.
class Topic(models.Model):
    Topic_Name=models.CharField( max_length=50)
    
class Webpage(models.Model):
    Topic_Name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    url=models.URLField()
    
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField( max_length=50)
