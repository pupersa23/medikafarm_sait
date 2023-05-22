from django.contrib import admin

from .models import Sale


class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'choice',
        'board_choice',
        'text',
        'pub_date',
        'image',
    )


admin.site.register(Sale, SaleAdmin)
