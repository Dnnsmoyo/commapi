from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='media')
 
class Community(models.Model):
    name = models.TextField(max_length=500, blank=True)
    description = models.TextField(max_length=500, blank=True)
    members = models.ForeignKey(User,on_delete=models.CASCADE)
    
class Post(models.Model):
    text = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='media',blank=True)
    member = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    community = models.ForeignKey(Community,on_delete=models.CASCADE,null=True)
    
class Product(models.Model):
    text = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='media',blank=True)
    member = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   
class Store(models.Model):
    name = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='media',blank=True)
    description = models.TextField(max_length=100)
    products= models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    member = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
