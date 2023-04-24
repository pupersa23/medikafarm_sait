from django.urls import path

from . import views

app_name = 'services'

urlpatterns = [
    path('ultrasound/', views.ultrasound, name='ultrasound'),
]
