from django.urls import path

from . import views

app_name = 'knigki'

urlpatterns = [
    path('medknizhki/', views.medknizhki, name='medknizhki'),
]
