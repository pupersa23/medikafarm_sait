from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('services/', include('services.urls', namespace='services')),
    path('spravki/', include('spravki.urls', namespace='spravki')),
    path('profosmotri/', include('profi.urls', namespace='profi')),
    path('knigki/', include('knigki.urls', namespace='knigki')),
    path('akzii/', include('sale.urls', namespace='sale')),
    path('statii/', include('posts.urls', namespace='posts')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
