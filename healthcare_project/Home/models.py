from django.db import models




class Departments(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField()

    def __str__(self):
        return self.name


class Doctors(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to='doctors/images')
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}  ( {self.department} department )' 



class Appointments(models.Model):
    patient_name = models.CharField(max_length= 100, null=False, blank=False)
    patient_phone = models.CharField(max_length=10, null=False, blank=False)
    patient_email = models.EmailField(blank=False, null=False)
    patient_age = models.IntegerField(blank=False,null=False)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE,default = 1)
    date = models.CharField(max_length=50)

    def __str__(self):
        return self.patient_name + " " + str(self.patient_age) + " ( Dr. " + str(self.doctor.name) + " )"
