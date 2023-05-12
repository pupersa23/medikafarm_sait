from django.contrib import admin

from .models import Predvaritelnie, Pereodik, Psixushka, Predsmena


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
