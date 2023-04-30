from django.urls import path

from . import views

app_name = 'spravki'

urlpatterns = [
    path('003-wy/', views.gibdd, name='gibdd'),
    path('gims/', views.gims, name='gims'),
    path('001-gsy/', views.gsy, name='gsy'),
    path('989n/', views.gstayna, name='gstayna'),
]
