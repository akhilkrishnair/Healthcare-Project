from django.shortcuts import render



def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def enquery(request):
    return render(request, 'enquery.html')




def appointment(request):
    return render(request, 'appointment.html')


def doctors(request):
    return render(request, 'doctors.html')


def departments(request):
    return render(request, 'departments.html')