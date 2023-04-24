from django.contrib import admin

from .models import UltraSound


class UltraSoundAdmin(admin.ModelAdmin):
    list_display = ('pk', 'description', 'price',)


admin.site.register(UltraSound, UltraSoundAdmin)
