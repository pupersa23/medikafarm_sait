from django.contrib import admin

from .models import Pereodik, Predsmena, Predvaritelnie, Psixushka


class PredvaritelnieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'price',)


class PereodikAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'price',)


class PsixushkaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'price',)


class PredsmenaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'price',)


admin.site.register(Predvaritelnie, PredvaritelnieAdmin)
admin.site.register(Pereodik, PereodikAdmin)
admin.site.register(Psixushka, PsixushkaAdmin)
admin.site.register(Predsmena, PredsmenaAdmin)
