from django.contrib import admin
from .models import employee
from .models import EndUser
# Register your models here.
admin.site.register(employee)
admin.site.register(EndUser)