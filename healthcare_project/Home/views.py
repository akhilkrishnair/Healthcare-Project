from django.shortcuts import render
from .models import Departments,Doctors


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def enquery(request):
    return render(request, 'enquery.html')




def appointment(request):
    return render(request, 'appointment.html')


def doctors(request):
    doctors = Doctors.objects.all()
    return render(request, 'doctors.html',{'doctors':doctors})


def departments(request):
    departments = Departments.objects.all()
    return render(request, 'departments.html', {'departments':departments})