from django.contrib import admin

from .models import Knigki


class KnigkiAdmin(admin.ModelAdmin):
    list_display = ('pk', 'choice', 'title', 'description', 'price',)


admin.site.register(Knigki, KnigkiAdmin)
