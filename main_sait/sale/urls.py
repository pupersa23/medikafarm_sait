from django.urls import path

from . import views

app_name = 'sale'

urlpatterns = [
    path('', views.sale, name='sale'),
]
