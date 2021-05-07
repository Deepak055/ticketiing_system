from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class employee(models.Model):
    Employee_id=models.IntegerField(primary_key=True)
    Employee_name=models.CharField(max_length=30)
  
    
    

def __str__(self):
    return self.Employee_name


    
  