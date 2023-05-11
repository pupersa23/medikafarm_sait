from django.urls import path

from . import views

app_name = 'profi'

urlpatterns = [
    path('predvaritelnie/', views.predvaritelnie, name='predvaritelnie'),

]
