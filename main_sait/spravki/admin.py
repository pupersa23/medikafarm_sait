from django.contrib import admin


from .models import Gibdd, Gims, Gsy, Gstayna


class GibdddAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price',)


class GimsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price',)


class GsyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price',)


class GstaynaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price',)


admin.site.register(Gibdd, GibdddAdmin)
admin.site.register(Gims, GimsAdmin)
admin.site.register(Gsy, GsyAdmin)
admin.site.register(Gstayna, GstaynaAdmin)
