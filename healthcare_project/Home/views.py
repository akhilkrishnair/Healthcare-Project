from django.shortcuts import render,redirect
from .models import Departments,Doctors,Appointments
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def enquery(request):
    return render(request, 'enquery.html')




def appointment(request):
    
    our_doctors = Doctors.objects.all()

    if request.method == 'POST':
        patient_name = request.POST['patientname']
        patient_phone = request.POST['patientphone']
        patient_email = request.POST['patientemail']
        patient_age = request.POST['patientage']
        doctor = request.POST['select-doctor']
        date = request.POST['appointmentdate']

        appointment = Appointments.objects.create(patient_name=patient_name, patient_phone=patient_phone, patient_email=patient_email, patient_age=patient_age, doctor_id = doctor , date=date)
        appointment.save()
        messages.info(request,"Your appointment has been booked")
        return redirect('home')

    return render(request, 'appointment.html', {'doctors_list':our_doctors})


def doctors(request):
    doctors = Doctors.objects.all()
    return render(request, 'doctors.html',{'doctors':doctors})


def departments(request):
    departments = Departments.objects.all()
    return render(request, 'departments.html', {'departments':departments})