from django.shortcuts import render
from django.urls import reverse
from ticketapp.forms import UserForm,EndUser
from ticketapp.forms import employeeform
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'ticketapp/home.html')
@login_required
def special(request):
    return HttpResponse('YOU LOGGED IN')


def index(request):
    
    
    registered=False

    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        employee_form=employeeform(data=request.POST)
        

        if user_form.is_valid() and employee_form.is_valid():
            
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            employee=employee_form.save(commit=False)
            employee.user=user
            employee.save()
            

            registered=True
            
            
        else:
            print(user_form.errors,employee_form.errors)
    else:
        user_form=UserForm()
        employee_form=employeeform()
    return render(request,'ticketapp/users.html',{'user_form':user_form,'employee_form':employee_form,'registered':registered})


   

def pro(request):
    
    
    registered=False

    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=EndUser(data=request.POST)
        

        if user_form.is_valid() and profile_form.is_valid():
            
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            

            registered=True
            
            
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=EndUser()
    return render(request,'ticketapp/users1.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

   


def user_login(request):
   
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Account non active')
        else:
            
            print("username:{} and password{}".format(username, password))
            return HttpResponse('invalid login')
    else:
        return render(request,'ticketapp/login.html',{})