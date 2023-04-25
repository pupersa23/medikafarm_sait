from django.urls import path

from . import views

app_name = 'services'

urlpatterns = [
    path('ultrasound/', views.ultrasound, name='ultrasound'),
    path('rentgen/', views.rentgen, name='rentgen'),
    path('analisi/', views.analisi, name='analisi'),
    path('fluromobil/', views.fluromobil, name='fluromobil'),
]
