from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('politika-konfidencialnosti/', views.konfiden, name='konfiden'),
    path('normativno-pravovie-documenti/', views.documents, name='documents'),
    path('kontacti/', views.contact, name='contact'),
    path('katalog/', views.price, name='price'),
]
