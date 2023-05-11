from django.contrib import admin

from .models import (Bassein, Gibdd, Gims, Gstayna, Gsy, Spravka086_1,
                     Spravka095_1, Travel, Bolnichnij)


class GibdddAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price',)


class GimsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price',)


class GsyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price',)


class GstaynaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price',)


class Spravka086_1_Admin(admin.ModelAdmin):
    list_display = ('pk', 'choice', 'title', 'price',)


class Spravka095_1_Admin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price',)


class BasseinAdmin(admin.ModelAdmin):
    list_display = ('pk', 'choice', 'title', 'price',)


class TravelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'choice', 'title', 'price',)


class BolnichnijAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price',)


admin.site.register(Gibdd, GibdddAdmin)
admin.site.register(Gims, GimsAdmin)
admin.site.register(Gsy, GsyAdmin)
admin.site.register(Gstayna, GstaynaAdmin)
admin.site.register(Spravka086_1, Spravka086_1_Admin)
admin.site.register(Spravka095_1, Spravka095_1_Admin)
admin.site.register(Bassein, BasseinAdmin)
admin.site.register(Travel, TravelAdmin)
admin.site.register(Bolnichnij, BolnichnijAdmin)
