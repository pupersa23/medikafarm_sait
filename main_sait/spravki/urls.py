from django.urls import path

from . import views

app_name = 'spravki'

urlpatterns = [
    path('003-wy/', views.gibdd, name='gibdd'),
    path('gims/', views.gims, name='gims'),
    path('001-gsy/', views.gsy, name='gsy'),
    path('989n/', views.gstayna, name='gstayna'),
    path('spravki-086y/', views.spravki_086, name='spravki_086'),
    path(
        'spravki-086y/<slug:choice>',
        views.spravki_086_datail,
        name='spravki_086_datail'
    ),
    path('spravki-095y/', views.student_095, name='student_095'),
    path('spravki-sport/', views.spravki_sport, name='spravki_sport'),
    path(
        'spravki-sport/<slug:choice>',
        views.spravki_sport_datail,
        name='spravki_sport_datail'
    ),
    path('spravki-puteshestvij/', views.spravki_travel, name='spravki_travel'),
    path(
        'spravki-puteshestvij/<slug:choice>',
        views.spravki_travel_datail,
        name='spravki_travel_datail'
    ),
    path('bolnichnyj-list/', views.bolnichnij, name='bolnichnij'),
]
