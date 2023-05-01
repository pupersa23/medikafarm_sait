from django.urls import path

from . import views

app_name = 'spravki'

urlpatterns = [
    path('003-wy/', views.gibdd, name='gibdd'),
    path('gims/', views.gims, name='gims'),
    path('001-gsy/', views.gsy, name='gsy'),
    path('989n/', views.gstayna, name='gstayna'),
    path('spravki-086y/', views.spravki_086, name='spravki_086'),
    path('spravki-095y/', views.student_095, name='student_095'),
    path('spravki-bassein/', views.bassein, name='bassein'),
]
