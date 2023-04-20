from django.contrib import admin

from .models import HomeTopInfo


class HomeTopInfoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'work_time', 'phone_number',)


admin.site.register(HomeTopInfo, HomeTopInfoAdmin)
