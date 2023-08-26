from django.contrib import admin
from .models import Departments,Doctors,Appointments


admin.site.register([Departments,Doctors,Appointments])