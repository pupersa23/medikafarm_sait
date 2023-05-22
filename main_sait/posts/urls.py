from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('vse-statii/', views.posts_all, name='posts_all'),
    path('vse-statii/<int:post_id>/', views.post_detail, name='post_detail'),
]
