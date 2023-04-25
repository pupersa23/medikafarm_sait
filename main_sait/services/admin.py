from django.contrib import admin

from .models import UltraSound, Rentgen, Analisi, Fluromobil


class UltraSoundAdmin(admin.ModelAdmin):
    list_display = ('pk', 'description', 'price',)


class RentgenAdmin(admin.ModelAdmin):
    list_display = ('pk', 'description', 'price',)


class AnalisiAdmin(admin.ModelAdmin):
    list_display = ('pk', 'file',)


class FluromobilAdmin(admin.ModelAdmin):
    list_display = ('pk', 'description', 'distance', 'price',)


admin.site.register(UltraSound, UltraSoundAdmin)
admin.site.register(Rentgen, RentgenAdmin)
admin.site.register(Analisi, AnalisiAdmin)
admin.site.register(Fluromobil, FluromobilAdmin)
