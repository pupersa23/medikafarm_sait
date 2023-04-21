from django.contrib import admin

from .models import HomeTopInfo, HomeBord, HomePriceCorp, HomeDoctor


class HomeTopInfoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'work_time', 'phone_number',)


class HomeBordAdmin(admin.ModelAdmin):
    list_display = ('pk', 'choice', 'title', 'description', 'url_for_button',)


class HomePriceCorpAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'price',
        'quantity',
        'description',
        'url_for_button',)


class HomeDoctorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'image', 'fio', 'job_title',)


admin.site.register(HomeTopInfo, HomeTopInfoAdmin)
admin.site.register(HomeBord, HomeBordAdmin)
admin.site.register(HomePriceCorp, HomePriceCorpAdmin)
admin.site.register(HomeDoctor, HomeDoctorAdmin)
