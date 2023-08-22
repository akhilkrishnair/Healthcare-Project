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


