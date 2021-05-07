from django import forms
from django.contrib.auth.models import User
from . models import employee


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model=User
        fields=('username', 'email', 'password')

class employeeform(forms.ModelForm):
    
    class Meta:
        model=employee
        fields=('Employee_id', 'Employee_name')