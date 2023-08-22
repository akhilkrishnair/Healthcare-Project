from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('enquery',views.enquery, name='enquery'),
    path('appointment',views.appointment, name='appointment'),
    path('doctors',views.doctors, name='doctors'),
    path('departments',views.departments, name='departments'),
]