from django.urls import path

from . import views

app_name = 'profi'

urlpatterns = [
    path('predvaritelnie/', views.predvaritelnie, name='predvaritelnie'),
    path('pereodicheskiy/', views.pereodicheskiy, name='pereodicheskiy'),
    path('vneocherednoy/', views.vneocherednoy, name='vneocherednoy'),
    path('psihiatricheskoe/', views.psihiatricheskoe, name='psihiatricheskoe'),
    path('predsmenniy/', views.predsmenniy, name='predsmenniy'),
]
