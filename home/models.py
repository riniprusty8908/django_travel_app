from unicodedata import name
from django.db import models


# Create your models here.
class Destination(models.Model):
   
    name=models.CharField(max_length=122)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

    











class Contact(models.Model):
    name=models.CharField(max_length=122)
    EmailAddress=models.CharField(max_length=122)
    phone=models.IntegerField()
    desc=models.TextField()
    
    def __str__(self):
       return self.name
   

    

    
