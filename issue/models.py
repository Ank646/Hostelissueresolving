
# Create your models here.
from pickle import FALSE
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    auth_token = models.CharField(max_length=100 )
    pwd= models.CharField(max_length=10)
    em=models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    ##user = models.OneToOneField(User,on_delete=models.CASCADE)
    usernm=models.CharField(max_length=100)
    room= models.CharField(max_length=10)
    hostelname= models.CharField(max_length=10)
    floor= models.CharField(max_length=10)
    mobno= models.CharField(max_length=10)
    name= models.CharField(max_length=10)

class issueee(models.Model):
    complain=models.CharField(max_length=100)
    description= models.CharField(max_length=2000)
    hostelname= models.CharField(max_length=10)
    floor= models.CharField(max_length=10)
    room= models.CharField(max_length=10)
    name= models.CharField(max_length=100)
    date= models.DateTimeField(auto_now_add=True)
    count=models.CharField(max_length=100)
    status=models.BooleanField(default=False)

    
    
     


