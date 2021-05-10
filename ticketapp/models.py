from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class employee(models.Model):
    
    Employee_id=models.IntegerField(primary_key=True)
    Employee_name=models.CharField(max_length=30)
    
  
    
    

def __str__(self):
    return self.user.username



class EndUser(models.Model):
    user= models.OneToOneField(User,on_delete=models.DO_NOTHING)
    image =models.ImageField(upload_to='profile_pics',blank=True)


def __str__(self):
    return self.user.username


    
  