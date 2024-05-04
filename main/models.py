from django.db import models
from datetime import timezone, datetime

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    active = models.BooleanField(default=False)
    
    
class Project(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    link = models.URLField()
    
class ContactInfo(models.Model):
    dets = models.TextField(max_length=40)
    icon = models.ImageField(upload_to='pics')
    
class SubscribedUser(models.Model):
    email= models.EmailField(unique=True, max_length=100)
    created_date = models.DateField('Date created', default=datetime.now)
    
    def __str__(self):
        return self.email