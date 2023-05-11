from django.contrib import admin

from .models import Predvaritelnie


class Predvaritelnie_UlizaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'price',)


admin.site.register(Predvaritelnie, Predvaritelnie_UlizaAdmin)
